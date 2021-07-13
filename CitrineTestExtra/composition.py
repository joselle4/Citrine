"""
Created on July 13, 2019

@author: Joselle Abagat Barnett
"""
from pypif import pif


class Composition2(pif.Composition):

    def __init__(self):
        self.element_symbol = []
        self.coordinate_x = []
        self.coordinate_y = []
        self.coordinate_z = []
        self.mulliken_charge = []

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