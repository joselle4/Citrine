"""
Created on July 8, 2019

@author: Joselle Abagat Barnett
"""
from src import load
from pypif.obj import *
import pandas as pd


def ingest(file_count=100):
    """
    method to convert pandas data frames to pif objects:
    chemical system with classification, properties, composition, etc.
    :return: list of (pio's) pif objects
    """
    # load data frames
    ls_files = load.list_files()
    df_elements_coordinates_mulliken_charge = load.read_all_elements_coordinates_mulliken_charge(ls_files, file_count)
    df_scalar_properties = load.read_all_scalar_properties(ls_files, file_count)
    df_vibrational_frequencies = load.read_all_vibrational_frequencies(ls_files, file_count)
    df_smiles_strings = load.read_all_smiles_strings(ls_files, file_count)
    df_inchi_strings = load.read_all_inchi_strings(ls_files, file_count)

    # merge data frames with similar length by id
    df_all = pd.merge(df_scalar_properties, df_vibrational_frequencies, on='unique_id')
    df_all = pd.merge(df_all, df_smiles_strings, on='unique_id')
    df_all = pd.merge(df_all, df_inchi_strings, on='unique_id')
    assert isinstance(df_all, pd.DataFrame)

    ls_pif = []
    for index, row in df_all.iterrows():
        # set chemical system class
        chemical_system = ChemicalSystem()

        # call this entire 'class' as a class of GDB-9 molecule and add to chemical system
        classification = Classification()
        classification.name = "GDB-9 Molecule"
        chemical_system.classifications = classification

        # set up id and add to chemical system; set tag and name to be the same
        id = Id()
        id.name = row['unique_id']
        id.tags = id.name
        chemical_system.ids = id

        # set up references and add to chemical system
        ref = Reference()
        ref.authors = "Rupp, Matthias; Ramakrishnan, Raghunathan; Dral, Pavlo; Anatole von Lilienfeld, O."
        ref.year = "2018"
        ref.url = "https://www.nature.com/articles/sdata201422#t2"
        chemical_system.references = ref

        # list of properties within a chemical system
        # set up different scalar properties and add to chemical system
        ls_properties = get_property_list(row, df_scalar_properties)
        # this chemical system now contains a list of properties
        chemical_system.properties = ls_properties

        # add atom information as composition
        # list of atom information within a chemical system
        df_subset = df_elements_coordinates_mulliken_charge[df_elements_coordinates_mulliken_charge['unique_id'] ==
                                                            row['unique_id']]
        ls_atoms = get_atoms_list(df_subset)
        chemical_system.composition = ls_atoms

        # should we make class quantity = number of atoms in the chemical system?
        # assume that this class can function as such
        quantity = Quantity()
        quantity.tags = df_subset['number_of_atoms'].iloc[0]
        quantity.number_of_atoms = df_subset['number_of_atoms'].iloc[0]
        chemical_system.quantity = quantity

        # append to list
        ls_pif.append(chemical_system)
    return ls_pif


def get_atoms_list(df):
    """
    this method/function forms all atoms info (symbol, coords, mulliken charge
    into a list to be added to the chemical system
    :param df: data frame
    :return: list of atoms
    """
    # load units dictionary
    dict_units = load.dictionary_units()

    ls_atoms = []
    for index, row in df.iterrows():
        comp = Composition()
        comp.element = row['element_symbol']
        comp.coordinateX = row['coordinate_x']
        comp.coordinateY = row['coordinate_y']
        comp.coordinateZ = row['coordinate_z']
        comp.mulliken_charge = row['mulliken_charge']
        comp.tags = row['atom_number']
        ls_atoms.append(comp)

        # this option does not group the element composition together
        # i = 1
        # for item in row.iteritems():
        #     # print("name:" + str(item[0]))
        #     # print("value:" + str(item[1]))
        #     # print(row[item])
        #     # print(item[1])
        #     comp = Composition()
        #     if item[0] == 'element_symbol':
        #         comp.element = item[1]
        #         comp.tags = i
        #         i = i + 1
        #         ls_atoms.append(comp)
        #     elif item[0] in ['number_of_atoms', 'atom_number', 'unique_id']:
        #         pass
        #     else:
        #         comp.name = item[0]
        #         comp.scalars = item[1]
        #         comp.units = dict_units[item[0]]
        #         ls_atoms.append(comp)
    return ls_atoms


def get_property_list(row, df):
    """
    this method/function forms all properties into a list to be added to the chemical system
    :param row: data frame row
    :param df: data frame
    :return: list of properties
    """
    # load units dictionary
    dict_units = load.dictionary_units()

    ls_properties = []
    for item in df:
        if item == 'unique_id':
            pass
        else:
            # set property class
            property = Property()
            property.name = item
            property.scalars = row[item]

            # since vibrational frequencies vary by "#", just set it separately
            if 'vibrational_frequency' in item:
                property.units = 'cm^(-1)'
            # make exception for SMILES and InChI
            elif 'smiles' in item or 'inchi' in item:
                pass
            else:
                property.units = dict_units[item]

            # add property to list of properties
            ls_properties.append(property)
    return ls_properties


