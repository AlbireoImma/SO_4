from threading import BoundedSemaphore as Sem
from threading import Thread
import time

class Cliente(Thread):
    def __init__(self,val):
        Thread.__init__(self)
        self.id = val
        self.estado = 0 # 0: Afuera; 1: En cola de inf; 2: En cola de caja; 3: Libre de irse
    def run(self):
        while(self.estado < 3):
            time.sleep(4)
            # print("[Cliente "+str(self.id)+"] En estado: "+str(self.estado))
        # print("[Cliente "+str(self.id)+"] Se retira de la tienda")
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
                print("[Tienda] Cliente "+str(Clientes_Afuera[0].id)+" asignado a meson "+str(Atencion[j].numero))
                Clientes_Adentro.append(Clientes_Afuera[0])
                Clientes_Adentro[-1].estado += 1
                Atencion[j].clientes.append(Clientes_Afuera[0])
                del Clientes_Afuera[0]
                Clientes_Adentro[-1].start()
                self.espacio = 30 - len(Clientes_Adentro)
            self.espacio = 30 - len(Clientes_Adentro)
            print("[Tienda] Durmiendo...")
            print("[Tienda] Espacio disponible en la tienda: "+str(self.espacio))
            print("[Tienda] Gente esperando afuera: "+str(len(Clientes_Afuera)))
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
            while(len(self.clientes) > 0):
                ident = self.clientes[0].id
                # print("[Meson "+str(self.numero)+"] Atendiendo a cliente "+str(ident))
                i = 0
                j = 0
                for a in Clientes_Adentro:
                    if ident == a.id:
                        j = i
                        break
                    i +=1
                Clientes_Adentro[j].estado += 1
                self.atendidos += 1
                print("[Meson "+str(self.numero)+"] Cliente "+str(ident)+" atendido")
                print("[Meson "+str(self.numero)+"] Clientes atendidos: "+str(self.atendidos))
                print("[Meson "+str(self.numero)+"] Clientes por atender: "+str(len(self.clientes)))
                mov_caja.acquire()
                if len(Cajas[0].clientes) > len(Cajas[1].clientes):
                    Clientes_Adentro[j].estado += 1
                    Cajas[1].clientes.append(Clientes_Adentro[j])
                else:
                    Clientes_Adentro[j].estado += 1
                    Cajas[0].clientes.append(Clientes_Adentro[j])
                mov_caja.release()
                del self.clientes[0]
                time.sleep(3)
        return

class Caja(Thread):
    def __init__(self,val):
        Thread.__init__(self)
        self.clientes = list()
        self.atendidos = 0
        self.baño = 0
        self.numero = val
    def run(self):
        while(len(Clientes_Afuera) > 0):
            # print("[Caja"+str(self.numero)+"] Tiene "+str(len(self.clientes))+" en cola")
            while len(self.clientes) > 0:
                print("[Caja "+str(self.numero)+"] Tiene "+str(len(self.clientes))+" en cola")
                time.sleep(2)
                ident = self.clientes[0].id
                i = 0
                j = 0
                for a in Clientes_Adentro:
                    if a.id == ident:
                        j = i
                        break
                    i += 1
                Clientes_Adentro[j].estado += 10
                mov_afuera.acquire()
                del self.clientes[0]
                del Clientes_Adentro[j]
                mov_afuera.release()
        return



Atencion = list()
for a in range(5):
    Atencion.append(Atender(a+1))
Cajas = list()
for a in range(2):
    Cajas.append(Caja(a+1))
Clientes_Afuera = list()
for a in range(50):
    Clientes_Afuera.append(Cliente(a+1))
Clientes_Adentro = list()
mov_caja = Sem(1)
mov_meson = Sem(1)
mov_afuera = Sem(1)
lock_print = Sem(1)

def main():
    print("Main")
    tienda = Tienda()
    tienda.start()
    time.sleep(2)
    for meson in Atencion:
        meson.start()
    for caja in Cajas:
        caja.start()
    for meson in Atencion:
        meson.join()
    for caja in Cajas:
        caja.join()
    tienda.join()
    print("All join")
    return

main()