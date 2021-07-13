

class ParseXYZ(object):
    """
    xyz parser takes ...
    """

    def __init__(self):
        """
        constructor
        :param filepath:
        """
        # line 1
        self.number_of_atoms = []
        # line 2
        self.gdb9_tag = []
        self.identifier = []
        self.rotational_const_a = []
        self.rotational_const_b = []
        self.rotational_const_c = []
        self.dipole_moment = []
        self.isotropic_polarizability = []
        self.energy_homo = []
        self.energy_lumo = []
        self.gap #lumo - humo
        self.electronic_spatial_extent = []
        self.zero_point_vibrational_energy = []
        self.internal_energy_0k = []
        self.internal_energy_298k = [] #25C
        self.enthalpy_298k = [] #25C
        self.free_energy_298k = [] #25C
        self.heat_capacity_298k = [] #25C
        # line 3...n_a+2
        self.element_symbol = []
        self.coordinate_x = []
        self.coordinate_y = []
        self.coordinate_z = []
        self.mulliken_charge = []
        # third to the last line (string of values - split?)
        self.harmonic_vibrational_frequencies = {}
        # second to the last line (string)
        self.smiles = {}
        # last line (string)
        self.inchi = {}

    @property
    def number_of_atoms(self):
        return self.number_of_atoms

    @property
    def gdb9_tag(self):
        return self.gdb9_tag

    @property
    def identifier(self):
        return self.identifier

    @property
    def rotational_const_a(self):
        return self.rotational_const_a

    @property
    def rotational_const_b(self):
        return self.rotational_const_b

    @property
    def rotational_const_c(self):
        return self.rotational_const_c

    @property
    def dipole_moment(self):
        return self.dipole_moment

    @property
    def isotropic_polarizability(self):
        return self.isotropic_polarizability

    @property
    def energy_homo(self):
        return self.energy_homo

    @property
    def energy_lumo(self):
        return self.energy_lumo

    @property
    def gap(self):
        return self.energy_lumo - self.energy_homo

    @property
    def electronic_spatial_extent(self):
        return self.electronic_spatial_extent

    @property
    def zero_point_vibrational_energy(self):
        return self.zero_point_vibrational_energy

    @property
    def internal_energy_0k(self):
        return self.internal_energy_0k

    @property
    def internal_energy_298k(self):
        return self.internal_energy_298k

    @property
    def enthalpy_298k(self):
        return self.enthalpy_298k

    @property
    def free_energy_298k(self):
        return self.free_energy_298k

    @property
    def heat_capacity_298k(self):
        return self.heat_capacity_298K

    @property
    def element_symbol(self):
        return self.element_symbol

    @property
    def coordinate_x(self):
        return self.coordinate_x

    @property
    def coordinate_y(self):
        return self.coordinate_y

    @property
    def coordinate_z(self):
        return self.coordinate_z

    @property
    def mulliken_charge(self):
        return self.mulliken_charge

    @property
    def harmonic_vibrational_frequencies(self):
        self.harmonic_vibrational_frequencies

    @property
    def smiles(self):
        return self.smiles

    @property
    def inchi(self):
        self.inchi


