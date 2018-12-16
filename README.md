# Tarea 4 Sistemas Operativos 2018-2

> Tarea donde se desarrollan threads y semaforos para cumplir el funcionamiento de una tienda
<br>
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

El repositorio cumple con las especificaciones proporcionadas en el archivo pdf explicativo sobre la tarea

## Correr el codigo

Distribuciones Unix
```Unix
$ python3 Tienda.py
```

## Funcionamiento del Código

El codigo corresponde de 5 clases; tienda, baño, cliente, atencion y caja.<br>
Cada clase funciona representando una parte de la tienda.<br><br>
Tienda<br>
Esta clase es un hilo que hace de portero, en donde maneja dos listas globales de clientes que se encuentran adentro y afuera, con esto se asegura que la condición de espacio de la tienda se cumpla en totalidad, además ingresa a los clientes en el mesón de atención menos poblado.<br><br>
Baño<br>
Esta es una clase simple que contiene una cola, esto es para tener en cuenta el orden de los funcionarios que quieren acceder al baño y poder mantener quien sigue.<br><br>
Cliente<br>
Esta es una clase con funcionamineto de hilo, la cual se mantiene viva en el intervalo desde obtener un producto, pagarlo e irse de la tienda.<br><br>
Atencion<br>
Esta es una clase con funcionamiento de hilo, la cual maneja a los clientes que entran y los deriva a la caja menos poblada segun corresponda.<br><br>
Caja<br>
Esta es una clase con funcionamiento de hilo, la cual maneja a los clientes que llegan para terminar su ciclo dentro de la tienda.<br><br>

#### Link Github

[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://github.com/AlbireoImma/SO_4)

