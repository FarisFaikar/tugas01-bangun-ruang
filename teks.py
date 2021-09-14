import pygame
import math

chary_font = 'chary___.ttf'

# Warna
PUTIH = (255, 255, 255)
ABU = (200, 200, 200)
HITAM = (0, 0, 0)
HIJAU_TUA = (20, 50, 20)
MERAH = (255, 150, 150)
MERAH_TUA = (75, 30, 30)
BIRU = (150, 150, 255)
BIRU_TUA = (30, 30, 75)


class Teks:
    def __init__(self, diameter=100, tinggi=200):
        # operasi matematika yang pentingnya di sini
        self.diameter = diameter
        self.tinggi = tinggi
        jari2 = diameter / 2
        pi = 3.14159265359

        # πr^2t = rumus volume silinder
        self.volume = pi * pow(jari2, 2) * tinggi
        # 2πr(r+t) = rumus luas permukaan silinder
        self.l_permukaan = 2 * pi * jari2 * (jari2 + tinggi)

        # variabel text
        self.text_spasi = 20
        self.textX = 10  # posisi x awal
        self.textY = 355  # posisi y awal
        self.textY_dinamis = self.textY - self.text_spasi
        self.screen = None

    def gambar(self, screen):
        self.screen = screen

        # tambahkan text berurutan
        jari2 = str(math.trunc(self.diameter / 2))
        self.tambah_text_berurutan(f"Diameter: {str(self.diameter)} cm / Jari-jari: {jari2} cm", BIRU)
        self.tambah_text_berurutan(f"Tinggi: {str(self.tinggi)} cm", MERAH)
        volume = str(math.trunc(self.volume))
        self.tambah_text_berurutan(f"Volume: {volume} cm^3", ABU)
        l_permukaan = str(math.trunc(self.l_permukaan))
        self.tambah_text_berurutan(f"Luas permukaan: {l_permukaan} cm^2", PUTIH)

        # tambah text dengan posisi sendiri
        self.tambah_text("50cm", PUTIH, 0, 10)

        # reset textY position
        self.textY_dinamis = self.textY - self.text_spasi

    def tambah_text_berurutan(self, text, color):
        kalimat = self.render_font(text, color)
        self.textY_dinamis = self.textY_dinamis + self.text_spasi
        self.screen.blit(kalimat, (self.textX, self.textY_dinamis))

    def tambah_text(self, text, color, x, y):
        kalimat = self.render_font(text, color)
        self.screen.blit(kalimat, (x, y))

    @staticmethod
    def render_font(text, color):
        # charydbis font
        chary = pygame.font.Font(chary_font, 20)
        return chary.render(text, True, color)
