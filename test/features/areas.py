#! /usr/bin/python
# -*-coding: utf-8 -*

"""
    Autor: Esteban García de Santiago
    Autor: Pablo César Rodríguez Aguayo
"""

from math import pi


class AreaCalculator(object):
    """docstring for AreaCalculator"""

    def __init__(self):
        super(AreaCalculator, self).__init__()
        self.__area = 0
        self.__figures = ['Escogiste el circulo', 'Escogiste el rectangulo',
                          'Escogiste el cuadrado', 'Escogiste el trapecio']

    def choose_figure(self, figure):
        return self.__figures[figure - 1]

    def calculate_area_circle(self, radius):
        self.__area = pi * (radius**2)

    def calculate_area_rectangle(self, dimensions):
        self.__area = dimensions[0] * dimensions[1]

    def calculate_area_square(self, length):
        self.__area = length ** 2

    def calculate_area_trapeze(self, dimensions):
        self.__area = ((dimensions[0] + dimensions[1]) / 2) * dimensions[2]

    def get_area(self):
        return self.__area
