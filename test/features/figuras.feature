Feature: Calculo de areas de figuras
    Como usuario del sistema de figuras
    deseo obtener el area de una figura
    para saber el resultado
    
    Scenario: Area de un circulo
        Dado que escogo la figura "1"
        cuando le paso al sistema los valores "2"
        entonces el sistema da el area del circulo "12.566370614359172"
        
    Scenario: Area de un cuadrado
        Dado que escogo la figura "2"
        cuando le paso al sistema los valores "2,4"
        entonces el sistema da el area del rectangulo "8"
        
    Scenario: Area de un cuadrado
        Dado que escogo la figura "3"
        cuando le paso al sistema los valores "2"
        entonces el sistema da el area del cuadrado "4"
        
    Scenario: Area de un trapecio
        Dado que escogo la figura "4"
        cuando le paso al sistema los valores "2,4,5"
        entonces el sistema da el area del trapecio "15"
        