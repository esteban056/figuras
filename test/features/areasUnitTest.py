#! /usr/bin/python
# -*-coding: utf-8 -*

"""
    Autor: Esteban García de Santiago
    Autor: Pablo César Rodríguez Aguayo
"""

import unittest
from areas import AreaCalculator

class AreasUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.area = AreaCalculator()
        
    def test_escoge_circulo(self):
        self.assertEquals(self.area.choose_figure(1),'Escogiste el circulo')

    def test_area_circulo(self):
        self.area.calculate_area_circle(2)
        self.assertEquals(self.area.get_area(),12.566370614359172)
        
    def test_escoge_rectangulo(self):
        self.assertEquals(self.area.choose_figure(2),'Escogiste el rectangulo')
        
    def test_area_rectangulo(self):
        self.area.calculate_area_rectangle([2, 4])
        self.assertEquals(self.area.get_area(),8)

    def test_escoge_cuadrado(self):
        self.assertEquals(self.area.choose_figure(3),'Escogiste el cuadrado')

    def test_area_cuadrado(self):
        self.area.calculate_area_square(2)
        self.assertEquals(self.area.get_area(),4)
    
    
    def test_escoge_trapecio(self):
        self.assertEquals(self.area.choose_figure(4),'Escogiste el trapecio')
        
    def test_area_trapecio(self):
        self.area.calculate_area_trapeze([2, 4, 5])
        self.assertEquals(self.area.get_area(),15)


if __name__ == '__main__':# pragma: no cover
       unittest.main()   

