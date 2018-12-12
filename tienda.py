from threading import BoundedSemaphore as Sem
from threading import Thread
import time

lock = Sem(1)
bano = Sem(1)
Fila_Clientes = []
Clientes_Tienda = 0
numero = 1

class Meson(Thread):
    def __init__(self, val):
        # Constructor
        Thread.__init__(self)
        self.nro_meson = val
        self.clientes = []
        self.atendidos = 0
        self.en_cola = 0

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
            print("[Thread {}] Clientes atendidos: {}, Cliente actual: {}".format(self.nro_meson,self.atendidos,self.clientes[0]))
            del self.clientes[0]
            print("[Thread "+str(self.nro_meson)+"] Clientes esperando -> ",self.clientes)
        print("[Thread %d] Trabajo cumplido" % self.nro_meson)
        return

# Clase representativa de un cliente
class Cliente():
    def __init__(self,val):
        self.nro_cliente = val
        self.estado = 0 # 0:Espera 1:Eligiendo 2:Pagando 3:Saliendo

# Clase representativa de la tienda
class Tienda():
    def __init__(self):
        self.clientes = []
        self.espacio = 30
        self.abierta = 0
    def addCliente(cliente):
        self.clientes.append(cliente)
        self.espacio -= 1

def main():
    mesones = list()
    for i in range(5):
        mesones.append(Meson(i+1))
    print("[Main] Iniciando mesones")
    for meson in mesones:
        meson.start()
    for meson in mesones:
        meson.join()
    print("[Main] All join")
    return


if __name__ == "__main__":
    main()
    pass
