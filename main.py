from bangunruang import Silinder, Balok, Bola, Piramida
from grafis import Grafis


class Program:
    def __init__(self):
        # Inisialisasi objek beserta input variable
        self.silinder = Silinder(100, 200)
        self.bola = Bola(100)
        self.balok = Balok(100, 200, 300)
        self.piramida = Piramida(100, 200, 300)

    def main(self):
        self.silinder.jalankan()
        self.bola.jalankan()
        self.balok.jalankan()
        self.piramida.jalankan()


if __name__ == '__main__':
    program = Program()
    program.main()

    # Grafis
    grafis = Grafis()
    grafis.jalankan()
