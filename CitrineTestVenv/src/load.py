"""
Created on July 3, 2019

@author: Joselle Abagat Barnett
"""
import pandas as pd
import glob
import os


def get_data_directory(folder_name="dsgdb9nsd.xyz"):
    """
    for the GDB-9 molecule, folder name = "dsgdb9nsd.xyz"
    :param folder_name: string of folder name
    :return: file path to data collection within this package
    """
    return os.path.join(os.getcwd() + os.sep + os.pardir, "data", folder_name)


def list_files(pattern="/*.xyz"):
    """
    creates a list of files from the directory; for the GDB-9 molecule, pattern = "/*.xyz"
    :param pattern: string of file pattern to include in the list
    :return: file list
    """
    directory = get_data_directory()
    ls_files = glob.glob(directory + pattern)
    ls_files.sort()
    return ls_files


def read_all_elements_coordinates_mulliken_charge(ls_files: list, file_count=100):
    """
    :param ls_files: load using list_files method
    :param file_count: length or number of files to be read and loaded
    :return: data frame or data table containing read files
    """
    ls_files = ls_files[0:file_count]

    ls_data = []
    for filename in ls_files:
        # read atoms, coordinates, mulliken partial charge
        atom_data = pd.read_csv(filename, sep='\t', engine='python', skiprows=2, skipfooter=3,
                                names=['element_symbol', 'coordinate_x', 'coordinate_y', 'coordinate_z',
                                       'mulliken_charge'])

        # read number of atoms (line 1) and add to df
        atom_data['number_of_atoms'] = get_number_of_atoms(filename)

        # add "atom number"
        atom_data.index += 1
        atom_data.insert(loc=len(atom_data.columns), column='atom_number', value=list(atom_data.index))

        # add a unique lookup (tag-identifier)
        scalar_data = read_scalar_properties(filename)
        atom_data.insert(loc=len(atom_data.columns), column='unique_id', value=scalar_data['unique_id'].iloc[0])

        ls_data.append(atom_data)

    df = pd.concat(ls_data, axis=0, ignore_index=True)
    assert isinstance(df, pd.DataFrame)
    return df


def read_all_scalar_properties(ls_files: list, file_count=100):
    """
    loop through files in the file list and obtain the scalar properties in line 2
    :param ls_files: load using list_files method
    :param file_count: length or number of files to be read and loaded
    :return: data frame or data table containing read files
    """
    ls_files = ls_files[0:file_count]

    ls_data = []
    for filename in ls_files:
        # all other scalar properties
        scalar_data = read_scalar_properties(filename)

        ls_data.append(scalar_data)

    df = pd.concat(ls_data, axis=0, ignore_index=True)
    assert isinstance(df, pd.DataFrame)
    return df


def read_all_vibrational_frequencies(ls_files: list, file_count=100):
    """
    vibrational frequencies are located in the n_a + 3 line of the file; store all frequencies in an array?
    :param ls_files:
    :param file_count:
    :return:
    """
    ls_files = ls_files[0:file_count]

    ls_data = []
    for filename in ls_files:
        # get number of atoms and add 3 for correct location
        line = get_number_of_atoms(filename) + 3

        vib_data = pd.read_csv(filename, sep='\t', engine='python', skiprows=line-1, skipfooter=2, header=None)
        vib_data = vib_data.rename(columns=lambda x: 'vibrational_frequency_' + str(x+1))

        # add unique_id
        scalar_data = read_scalar_properties(filename)
        vib_data.insert(loc=len(vib_data.columns), column='unique_id', value=scalar_data['unique_id'].iloc[0])

        ls_data.append(vib_data)

    df = pd.concat(ls_data, axis=0, ignore_index=True, sort=False)
    assert isinstance(df, pd.DataFrame)
    return df


def read_all_smiles_strings(ls_files: list, file_count=100):
    """
    SMILES strings are located in the n_a + 4 line of the file
    :param ls_files:
    :param file_count:
    :return:
    """
    ls_files = ls_files[0:file_count]

    ls_data = []
    for filename in ls_files:
        # get number of atoms and add 4 for correct location
        line = get_number_of_atoms(filename) + 4

        # last \t creates an unnecessary NAN third row; only use first two columns
        smiles_data = pd.read_csv(filename, sep='\t', engine='python', skiprows=line - 1, skipfooter=1, header=None,
                                  usecols=[0, 1], names=['smiles_gdb17', 'smiles_b3lyp'])

        # add unique_id
        scalar_data = read_scalar_properties(filename)
        smiles_data.insert(loc=len(smiles_data.columns), column='unique_id', value=scalar_data['unique_id'].iloc[0])

        ls_data.append(smiles_data)

    df = pd.concat(ls_data, axis=0, ignore_index=True)
    assert isinstance(df, pd.DataFrame)
    return df


def read_all_inchi_strings(ls_files: list, file_count=100):
    """
    InChI strings are the last line of the file: n_a + 5
    :param ls_files:
    :param file_count:
    :return:
    """
    ls_files = ls_files[0:file_count]

    ls_data = []
    for filename in ls_files:
        # get number of lines
        line = get_line_count(filename)

        # all other scalar properties
        inchi_data = pd.read_csv(filename, sep='\t', engine='python', skiprows=line - 1, header=None,
                                 names=['inchi_corina', 'inchi_b3lyp'])

        # add unique_id
        scalar_data = read_scalar_properties(filename)
        inchi_data.insert(loc=len(inchi_data.columns), column='unique_id', value=scalar_data['unique_id'].iloc[0])

        ls_data.append(inchi_data)

    df = pd.concat(ls_data, axis=0, ignore_index=True)

    # strip "InChI="
    df['inchi_corina'] = df['inchi_corina'].map(lambda x: x.lstrip('InChI='))
    df['inchi_b3lyp'] = df['inchi_b3lyp'].map(lambda x: x.lstrip('InChI='))

    assert isinstance(df, pd.DataFrame)
    return df


def read_scalar_properties(filename: str):
    """
    obtain the scalar properties in line 2 of the file
    :param filename: string filepath of file
    :return: data frame or data table containing read files
    """
    scalar_data = pd.read_csv(filename, sep='\t', nrows=1, skiprows=1, index_col=False,
                              names=['unique_id', 'rotational_constant_a', 'rotational_constant_b',
                                     'rotational_constant_c', 'dipole_moment', 'isotropic_polarizability',
                                     'energy_homo', 'energy_lumo', 'gap', 'electronic_spatial_extent',
                                     'zero_point_vibrational_energy', 'internal_energy_0k', 'internal_energy_298k',
                                     'enthalpy_298k', 'free_energy_298k', 'heat_capacity_298k'])
    return scalar_data


def get_number_of_atoms(filename: str):
    """
    :param filename: filepath of file
    :return: number of atoms
    """
    # read number of atoms (line 1)
    number_of_atoms = pd.read_csv(filename, nrows=1, header=None)
    return int(number_of_atoms[0])


def get_line_count(filename: str):
    """
    :param filename: string filepath of file
    :return: total number of lines in the file
    """
    return get_number_of_atoms(filename)+5


def dictionary_units():
    """
    :return: dictionary of properties and their respective units
    """
    dict = {
        'unique_id': '-',
        'rotational_constant_a': 'GHz',
        'rotational_constant_b': 'GHz',
        'rotational_constant_c': 'GHz',
        'dipole_moment': 'D',
        'isotropic_polarizability': 'a_0^3',
        'energy_homo': 'Ha',
        'energy_lumo': 'Ha',
        'gap': 'Ha',
        'electronic_spatial_extent': 'a_0^2',
        'zero_point_vibrational_energy': 'Ha',
        'internal_energy_0k': 'Ha',
        'internal_energy_298k': 'Ha',
        'enthalpy_298k': 'Ha',
        'free_energy_298k': 'Ha',
        'heat_capacity_298k': 'cal/molK',
        'element_symbol': '-',
        'coordinate_x': 'A',
        'coordinate_y': 'A',
        'coordinate_z': 'A',
        'mulliken_charge': 'e'
    }
    return dict


