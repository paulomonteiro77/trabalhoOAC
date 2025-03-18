import threading
import time

def processo(nome, duracao):
    print(f"{nome} Iniciado")
    time.sleep(duracao)
    print(f"{nome} Finalizado")

def main():
    thread1 = threading.Thread(target=processo, args=("processo 1", 2))
    thread2 = threading.Thread(target=processo, args=("processo 2", 4))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Esse processo foi finalizado!!")

if __name__ == "__main__":
    main()
