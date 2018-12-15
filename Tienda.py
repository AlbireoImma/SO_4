from threading import BoundedSemaphore as Sem
from threading import Thread
import time

class Cliente(Thread):
    def __init__(self,val):
        Thread.__init__(self)
        self.id = val
        self.estado = 0
    def run(self):
        while(self.estado < 3):
            time.sleep(3)
            print("[Cliente ",self.id,"] En estado: ",self.estado)
        return

class Tienda(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.espacio = 30
    def run(self):
        while (len(Clientes_Afuera) > 0):
            while (self.espacio > 0):
                i = 0
                j = 0
                minimal = 1000
                for meson in Atencion:
                    if len(meson.clientes) <= minimal:
                        minimal = len(meson.clientes)
                        j = i
                    i+=1
                Atencion[j].clientes.append(Clientes_Afuera[0])
                Atencion[j].clientes[-1].estado += 1
                del Clientes_Afuera[0]
                self.espacio -= 1
            time.sleep(5)
        return


class Atender(Thread):
    def __init__(self,val):
        Thread.__init__(self)
        self.clientes = list()
        self.atendidos = 0
        self.baño = 0
        self.numero = val
    def run(self):
        while(len(Clientes_Afuera) > 0):
            pass
        return



Atencion = list()
for a in range(5):
    Atencion.append(Atender(a+1))
Clientes_Afuera = list()
for a in range(50):
    Clientes_Afuera.append(Cliente(a+1))