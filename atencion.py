from threading import Thread, Lock
import time

lock = Lock()
numero = 1

class Meson(Thread):
    def __init__(self, val):
        # Constructor
        Thread.__init__(self)
        self.nro_meson = val
        self.clientes = []
        self.atendidos = 0

    def run(self):
        for a in range(5):
            global numero
            lock.acquire()
            self.clientes.append(numero)
            numero = numero + 1
            lock.release()
        while(len(self.clientes) > 0):
            time.sleep(2)
            self.atendidos += 1
            print("[Thread {}] Clientes atendidos: {}".format(self.nro_meson,self.atendidos))
            del self.clientes[0]
        print("[Thread %d] Trabajo cumplido" % self.nro_meson)
        return
