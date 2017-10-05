# -*- coding: utf-8 -*-
"""
    Autor: Esteban García de Santiago
"""
from lettuce import step, world
from areas import AreaCalculator


@step(u'Dado que escogo la figura "([^"]*)"')
def dado_que_escogo_la_figura_group1(step, opcion):
    world.areas = AreaCalculator()
    opcion = int(opcion)
    # probamos las opciones
    esFigura = False
    mensaje = world.areas.choose_figure(opcion)
    esFigura = esFigura or mensaje == 'Escogiste el circulo'
    esFigura = esFigura or mensaje == 'Escogiste el rectangulo'
    esFigura = esFigura or mensaje == 'Escogiste el cuadrado'
    esFigura = esFigura or mensaje == 'Escogiste el trapecio'
    assert esFigura, 'Error mensaje: ' + mensaje


@step(u'cuando le paso al sistema los valores "([^"]*)"')
def cuando_le_paso_al_sistema_los_valores_group1(step, valores):
    world.valores = valores.split(",")
    world.valores = map(int, world.valores)


@step(u'entonces el sistema da el area del circulo "([^"]*)"')
def entonces_el_sistema_da_el_area_del_circulo_group1(step, areaEsperada):
    world.areas.calculate_area_circle(world.valores[0])
    areaCalculada = world.areas.get_area()
    assert areaCalculada == float(areaEsperada), 'Area esperada: ' + \
        areaEsperada + " area calculada: " + str(areaCalculada)


@step(u'entonces el sistema da el area del rectangulo "([^"]*)"')
def entonces_el_sistema_da_el_area_del_rectangulo_group1(step, areaEsperada):
    world.areas.calculate_area_rectangle(world.valores)
    areaCalculada = world.areas.get_area()
    assert areaCalculada == int(areaEsperada), 'Area esperada: ' + \
        areaEsperada + " area calculada: " + str(areaCalculada)


@step(u'entonces el sistema da el area del cuadrado "([^"]*)"')
def entonces_el_sistema_da_el_area_del_cuadrado_group1(step, areaEsperada):
    world.areas.calculate_area_square(world.valores[0])
    areaCalculada = world.areas.get_area()
    assert areaCalculada == int(areaEsperada), 'Area esperada: ' + \
        areaEsperada + " area calculada: " + str(areaCalculada)


@step(u'entonces el sistema da el area del trapecio "([^"]*)"')
def entonces_el_sistema_da_el_area_del_trapecio_group1(step, areaEsperada):
    world.areas.calculate_area_trapeze(world.valores)
    areaCalculada = world.areas.get_area()
    assert areaCalculada == int(areaEsperada), 'Area esperada: ' + \
        areaEsperada + " area calculada: " + str(areaCalculada)
