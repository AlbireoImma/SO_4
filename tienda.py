from atencion import Meson

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