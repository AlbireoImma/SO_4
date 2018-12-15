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
                
