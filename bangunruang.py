import math
PHI = 3.14159265359


class Silinder:
    diameter = 0
    tinggi = 0

    def __init__(self, diameter, tinggi):
        Silinder.diameter = diameter
        Silinder.tinggi = tinggi

    def jalankan(self):
        print("Menghitung volume dan luas permukaan silinder:")
        print(f"Diameter: {self.diameter} cm")
        print(f"Tinggi: {self.tinggi} cm")
        print("-----------------------------------")
        self.kalkulasi_volume()
        self.kalkulasi_luas_permukaan()
        print("")

    def kalkulasi_volume(self):
        # Rumus volume silinder = πr^2t
        jari2 = self.diameter / 2
        volume = PHI * pow(jari2, 2) * self.tinggi
        print(f"Volume silinder adalah: {round(volume)} cm^3")

    def kalkulasi_luas_permukaan(self):
        # Rumus luas permukaan silinder = 2πr(r+t)
        jari2 = self.diameter / 2
        luas_permukaan = 2 * PHI * (jari2 + self.tinggi)
        print(f"Luas permukaan silinder adalah: {round(luas_permukaan)} cm^2")


class Bola:
    def __init__(self, diameter):
        self.diameter = diameter

    def jalankan(self):
        print("Menghitung volume dan luas permukaan bola")
        print(f"Diameter: {self.diameter} cm")
        print("-----------------------------------")
        self.kalkulasi_volume()
        self.kalkulasi_luas_permukaan()
        print("")

    def kalkulasi_volume(self):
        # Rumus volume bola = 4/3πr^3
        jari2 = self.diameter / 2
        volume = 4 / 3 * PHI * pow(jari2, 3)
        print(f"Volume bola: {round(volume)} cm^3")

    def kalkulasi_luas_permukaan(self):
        # Rumus luas permukaan bola = 4πr^2
        jari2 = self.diameter / 2
        luas_permukaan = 4 * PHI * pow(jari2, 2)
        print(f"Luas permukaan bola: {round(luas_permukaan)} cm^2")


class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def jalankan(self):
        print("Menghitung volume dan luas permukaan balok")
        print(f"Panjang: {self.panjang} cm")
        print(f"Lebar: {self.lebar} cm")
        print(f"Tinggi: {self.tinggi} cm")
        print("-----------------------------------")
        self.kalkulasi_volume()
        self.kalkulasi_luas_permukaan()
        print("")

    def kalkulasi_volume(self):
        # Rumus volume balok = plt
        volume = self.panjang * self.lebar * self.tinggi
        print(f"Volume balok: {round(volume)} cm^3")

    def kalkulasi_luas_permukaan(self):
        # Rumus luas permukaan balok = 2(pl + pt + lt)
        luas_permukaan = 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)
        print(f"Luas permukaan balok: {round(luas_permukaan)} cm^2")


class Piramida(Balok):
    def jalankan(self):
        print("Menghitung volume dan luas permukaan piramida")
        print(f"Panjang: {self.panjang} cm")
        print(f"Lebar: {self.lebar} cm")
        print(f"Tinggi: {self.tinggi} cm")
        print("-----------------------------------")
        self.kalkulasi_volume()
        self.kalkulasi_luas_permukaan()
        print("")

    def kalkulasi_volume(self):
        # Rumus volume piramida = (plt)/3
        volume = (self.panjang * self.lebar * self.tinggi) / 3
        print(f"Volume piramida: {round(volume)} cm^3")

    def kalkulasi_luas_permukaan(self):
        # Rumus luas permukaan piramida = pl+l(√(l/2)^2+l)+l√(1/2)^2+t^2
        l_ = self.panjang
        w = self.lebar
        h = self.tinggi
        luas_permukaan = (l_ * w) + (l_ * math.sqrt(pow(w / 2, 2) + pow(h, 2))) + (
                    w * math.sqrt(pow(l_ / 2, 2) + pow(h, 2)))
        print(f"Luas permukaan piramida: {round(luas_permukaan)} cm^2")
