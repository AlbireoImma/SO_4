from threading import BoundedSemaphore as Sem
from threading import Thread
import time

def get_posmin(atencion):
    i = 0
    min = len(atencion[0].clientes)
    for item in atencion:
        if min > len(item.clientes):
            min = len(item.clientes)
            i = item.nro_meson - 1
    return i

class Atencion(Thread):
    def __init__(self, val, tienda):
        # Constructor
        Thread.__init__(self)
        self.nro_meson = val
        self.clientes = []
        self.atendidos = 0
        self.en_cola = 0
        self.tienda = tienda

    def insertCliente(self,cliente):
        self.clientes.append(cliente)
        self.en_cola += 1

    def get_cola(self):
        return self.en_cola

    def run(self):
        while(len(Clientes_Esperando) > 0):
            while(len(self.clientes) > 0):
                time.sleep(2)
                self.atendidos += 1
                print("[Thread {}] Clientes atendidos: {}, Cliente actual: {}".format(self.nro_meson,self.atendidos,self.clientes[0]))
                to_erase = self.clientes[0]
                del self.clientes[0]
                print("[Thread " + str(self.nro_meson) + "] Clientes esperando -> ",self.clientes)
                print("[Thread %d] Trabajo cumplido" % self.nro_meson)
                time.sleep(3)
                remover.acquire()
                self.tienda.clientes.remove(to_erase)
                remover.release()
        print("[Thread %d] Meson Cerrado" % self.nro_meson)
        return

# Clase representativa de un cliente
class Cliente():
    def __init__(self,val):
        self.nro_cliente = val
        self.estado = 0 # 0:Espera 1:Eligiendo 2:Pagando 3:Saliendo

# Clase representativa de la tienda
class Tienda(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.clientes = []
        self.espacio = 30
        self.abierta = 0
        self.id = 0
        self.cajas = []
        self.atencion = []
        self.bano = True
    def run(self):
        print("[Tienda] Espacio: ",self.espacio)
        while (len(Clientes_Esperando) > 0):
            while self.espacio > 0:
                print("[Tienda] Espacio: ",self.espacio)
                self.clientes.append(Clientes_Esperando[0].nro_cliente)
                min = 100
                self.atencion[get_posmin(self.atencion)].clientes.append(Clientes_Esperando[0].nro_cliente)
                self.espacio -= 1
                del Clientes_Esperando[0]
            time.sleep(2)
            print("[Tienda] Espacio: ",self.espacio)
            print("[Tienda] Clientes: ",self.clientes)
            print("[Tienda] Clientes Esperando: ",len(Clientes_Esperando))
            self.espacio = 30 - len(self.clientes)
            if Clientes_Esperando == 0:
                self.abierta = 0
        print("[Tienda] Listo")
        return

lock = Sem(1)
bano = Sem(1)
remover = Sem(1)
Clientes_Esperando = list()

for i in range(50):
    Clientes_Esperando.append(Cliente(i))

def main():
    tienda = Tienda()
    atencion = list()
    for i in range(5):
        atencion.append(Atencion(i+1,tienda))
    print("[Main] Abriendo Tienda")
    tienda.abierta = 1
    print("[Main] Iniciando mesones")
    for meson in atencion:
        meson.start()
    print("[Main] Iniciando Entrada de clientes")
    tienda.atencion = atencion
    tienda.start()
    print("[Main] All join")
    return


if __name__ == "__main__":
    main()
    pass
