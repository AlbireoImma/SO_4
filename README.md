# Tarea 4 Sistemas Operativos 2018-2

> Tarea donde se desarrollan threads y semaforos para cumplir el funcionamiento de una tienda

[![Python Version][python-image]][python-url]

El repositorio cumple con las especificaciones proporcionadas en el archivo pdf explicativo sobre la tarea

## Correr el codigo

Distribuciones Unix
```
$ python3 Tienda.py
```

## Funcionamiento del Código

El codigo corresponde de 5 clases; tienda, baño, cliente, atencion y caja.<br>
Cada clase funciona representando una parte de la tienda.<br>
Tienda: Esta clase es un hilo que hace de portero, en donde maneja dos listas globales de clientes que se encuentran adentro y afuera, con esto se asegura que la condición de espacio de la tienda se cumpla en totalidad.<br>
Baño: esta es una clase simple que contiene una cola, esto es para tener en cuenta el orden de los funcionarios que quieren acceder al baño y poder mantener quien sigue.<br>
Cliente: esta es una clase con funcionamineto de hilo, la cual se mantiene viva en el intervalo desde obtener un producto, pagarlo e irse de la tienda.<br>

