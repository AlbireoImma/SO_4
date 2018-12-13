from threading import BoundedSemaphore as Sem
from threading import Thread
import time

lock = Sem(1)
bano = Sem(1)
Clientes_Esperando = list()
tienda = Tienda()

for i in range(50):
    Clientes_Esperando.append(Cliente(i))


class Atencion(Thread):
    def __init__(self, val):
        # Constructor
        Thread.__init__(self)
        self.nro_meson = val
        self.clientes = []
        self.atendidos = 0
        self.en_cola = 0

    def insertCliente(self,cliente):
        self.clientes.append(cliente)
        self.en_cola += 1

    def get_cola(self):
        return self.en_cola

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
class Tienda(Thread):
    def __init__(self):
        self.clientes = []
        self.espacio = 30
        self.abierta = 0
        self.id = 0
    def run(self):
        while Clientes_Esperando > 0:
            while espacio > 0:
                self.clientes.append(id)
                Clientes_Esperando -= 1
                min = 100
                for meson in atencion:
                    if min > meson.get_cola:
                        min = meson.nro_meson - 1
                atencion[min].insertCliente(id)
                id += 1
            time.sleep(2)

    def addCliente(cliente):
        if espacio > 0:
            self.clientes.append(cliente)
            self.espacio -= 1
    def removeCliente(id):
        if id in self.clientes:
            self.clientes.remove(id)


def main():
    atencion = list()
    for i in range(5):
        atencion.append(Atencion(i+1))
    print("[Main] Iniciando mesones")
    for meson in atencion:
        meson.start()
    for meson in atencion:
        meson.join()
    print("[Main] All join")
    return


if __name__ == "__main__":
    main()
    pass
