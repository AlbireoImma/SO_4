from threading import Thread
import time

class Meson(Thread):
    def __init__(self, val):
        # Constructor
        Thread.__init__(self)
        self.nro_meson = val
        self.clientes = 0
    
    def run(self):
        while(self.clientes < 5):
            print("[Thread %d] Clientes atendidos" % self.clientes)
            time.sleep(2)
            self.clientes += 1
        print("[Thread %d] Trabajo cumplido" % self.nro_meson)
        return
    