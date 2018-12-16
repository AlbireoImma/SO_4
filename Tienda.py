from threading import BoundedSemaphore as Sem
from threading import Thread
import time
from time import gmtime, strftime

def getTime():
    return strftime("[%d-%m-%Y %H:%M:%S]", gmtime())

class Cliente(Thread):
    def __init__(self,val):
        Thread.__init__(self)
        self.id = val
        self.estado = 0 # 0: Afuera; 1: En cola de inf; 2: En cola de caja; 3: Libre de irse
    def run(self):
        while(self.estado < 3):
            time.sleep(4)
            # print("[Cliente "+str(self.id)+"] En estado: "+str(self.estado))
        log_clientes.write(getTime()+"[Cliente "+str(self.id)+"] Se retira de la tienda\n")
        return

class Tienda(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.espacio = 30
    def run(self):
        while (len(Clientes_Afuera) > 0):
            while (self.espacio > 0 and len(Clientes_Afuera) > 0):
                i = 0
                j = 0
                minimal = 1000
                for meson in Atencion:
                    if len(meson.clientes) <= minimal:
                        minimal = len(meson.clientes)
                        j = i
                    i+=1
                log_funcionarios.write(getTime()+"[Tienda] Cliente "+str(Clientes_Afuera[0].id)+" asignado a meson "+str(Atencion[j].numero)+"\n")
                Clientes_Adentro.append(Clientes_Afuera[0])
                Clientes_Adentro[-1].estado += 1
                Atencion[j].clientes.append(Clientes_Afuera[0])
                del Clientes_Afuera[0]
                Clientes_Adentro[-1].start()
                log_clientes.write(getTime()+"[Cliente "+str(Clientes_Adentro[-1].id)+"] Ha entrado a la tienda\n")
                self.espacio = 30 - len(Clientes_Adentro)
            self.espacio = 30 - len(Clientes_Adentro)
            print(getTime()+"[Tienda] Espacio disponible en la tienda: "+str(self.espacio))
            print(getTime()+"[Tienda] Gente esperando afuera: "+str(len(Clientes_Afuera)))
            time.sleep(5)
        return


class Atender(Thread):
    def __init__(self,val,val2):
        Thread.__init__(self)
        self.clientes = list()
        self.atendidos = 0
        self.cola_baño = 0
        self.numero = val
        self.id = val2
    def run(self):
        while(len(Clientes_Afuera) > 0):
            while(len(self.clientes) > 0):
                ident = self.clientes[0].id
                # print("[Meson "+str(self.numero)+"] Atendiendo a cliente "+str(ident))
                i = 0
                j = 0
                mov_caja.acquire()
                for a in Clientes_Adentro:
                    if ident == a.id:
                        j = i
                        break
                    i +=1
                Clientes_Adentro[j].estado += 1
                log_funcionarios.write(getTime()+"[Meson "+str(self.numero)+"] Cliente "+str(self.clientes[0].id)+" siendo atendido\n")
                log_clientes.write(getTime()+"[Cliente "+str(self.clientes[0].id)+"] En meson de informacion numero "+str(self.numero)+"\n")
                # print("[Meson "+str(self.numero)+"] Clientes atendidos: "+str(self.atendidos))
                print(getTime()+"[Meson "+str(self.numero)+"] Clientes por atender: "+str(len(self.clientes)))
                if len(Cajas[0].clientes) > len(Cajas[1].clientes):
                    Cajas[1].clientes.append(Clientes_Adentro[j])
                else:
                    try:
                        Cajas[0].clientes.append(Clientes_Adentro[j])
                    except:
                        pass
                mov_caja.release()
                del self.clientes[0]
                time.sleep(3)
                if self.atendidos == 4:
                    log_funcionarios.write(getTime()+"[Meson "+str(self.numero)+"] Revisando disponibilidad baño\n")
                    if self.id not in baño.cola:
                        baño.cola.append(self.id)
                    if baño.cola[0] == self.id:
                        log_funcionarios.write(getTime()+"[Meson "+str(self.numero)+"] Usando baño\n")
                        time.sleep(2)
                        del baño.cola[0]
                        self.atendidos = 0
                else:
                    self.atendidos += 1

        return

class Caja(Thread):
    def __init__(self,val,val2):
        Thread.__init__(self)
        self.clientes = list()
        self.atendidos = 0
        self.cola_baño = 0
        self.numero = val
        self.id = val2
    def run(self):
        while(len(Clientes_Afuera) > 0):
            # print("[Caja"+str(self.numero)+"] Tiene "+str(len(self.clientes))+" en cola")
            while len(self.clientes) > 0:
                # print("[Caja "+str(self.numero)+"] Clientes atendidos: "+str(self.atendidos))
                print(getTime()+"[Caja "+str(self.numero)+"] Tiene "+str(len(self.clientes))+" en cola")
                log_funcionarios.write(getTime()+"[Caja "+str(self.numero)+"] Atendiendo a cliente "+str(self.clientes[0].id)+"\n")
                time.sleep(5)
                ident = self.clientes[0].id
                i = 0
                j = 0
                mov_afuera.acquire()
                for a in Clientes_Adentro:
                    if a.id == ident:
                        j = i
                        break
                    i += 1
                Clientes_Adentro[j].estado += 10
                log_funcionarios.write(getTime()+"[Caja "+str(self.numero)+"] Cliente "+str(self.clientes[0].id)+" atendido\n")
                log_clientes.write(getTime()+"[Cliente "+str(self.clientes[0].id)+"] Actualmente en caja\n")
                del self.clientes[0]
                del Clientes_Adentro[j]
                mov_afuera.release()
                if self.atendidos == 4:
                    log_funcionarios.write(getTime()+"[Caja "+str(self.numero)+"] Revisando disponibilidad baño\n")
                    if self.id not in baño.cola:
                        baño.cola.append(self.id)
                    if baño.cola[0] == self.id:
                        log_funcionarios.write(getTime()+"[Caja "+str(self.numero)+"] Usando baño\n")
                        time.sleep(2)
                        del baño.cola[0]
                        self.atendidos = 0
                else:
                    self.atendidos += 1
        return

class Baño():
    def __init__(self):
        self.cola = list()



ident = 1
Atencion = list()
for a in range(5):
    Atencion.append(Atender(a+1,ident))
    ident += 1
Cajas = list()
for a in range(2):
    Cajas.append(Caja(a+1,ident))
    ident += 1
Clientes_Afuera = list()
for a in range(50):
    Clientes_Afuera.append(Cliente(a+1))
Clientes_Adentro = list()
mov_caja = Sem(1)
mov_meson = Sem(1)
mov_afuera = Sem(1)
lock_print = Sem(1)
lock_baño = Sem(1)
baño = Baño()
log_funcionarios = open("funcionarios.txt","a")
log_clientes = open("clientes.txt","a")

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
    print(getTime()+"[Tienda] Todos los clientes atendidos")
    print(getTime()+"[Tienda] Cerrando tienda...")
    print(getTime()+"[Tienda] Tienda cerrada")
    exit()

if __name__ == "__main__":
    main()