import pygame

# Warna
PUTIH = (255, 255, 255)
ABU = (200, 200, 200)
HITAM = (0, 0, 0)
HIJAU_TUA = (20, 50, 20)
MERAH = (255, 150, 150)
MERAH_TUA = (75, 30, 30)
BIRU = (150, 150, 255)
BIRU_TUA = (30, 30, 75)


class Interface:
    def __init__(self, diameter=100, tinggi=200):
        # variabel pokok
        self.diameter = diameter
        self.tinggi = tinggi
        self.ui = pygame.Rect((0, 350), (400, 200))

        # silinder
        posisi = (40, 40)
        tinggi_kotak1 = 20
        self.kotak = pygame.Rect(posisi, (diameter, tinggi))
        self.kotak_atas = pygame.Rect((posisi[0], posisi[1] - (tinggi_kotak1 / 2)), (diameter, tinggi_kotak1))
        self.kotak_bawah = pygame.Rect((posisi[0], posisi[1] + tinggi - (tinggi_kotak1 / 2)), (diameter, tinggi_kotak1))

        # Garis ukur
        self.p_garis = 50
        self.l_garis = 10

        # garis ukur Y
        self.pos_awalY = [10, 40]
        self.pos_dinamisY = self.pos_awalY.copy()
        self.pos_dinamisY[1] = self.pos_awalY[1] - self.p_garis
        self.garis = None
        self.garis2 = None

        # garis ukur X
        self.pos_awalX = [40, 10]
        self.pos_dinamisX = self.pos_awalX.copy()
        self.pos_dinamisX[0] = self.pos_awalX[0] - self.p_garis
        self.garis3 = None
        self.garis4 = None

    def gambar(self, screen):
        # gambar silinder
        pygame.draw.rect(screen, PUTIH, self.kotak)
        pygame.draw.ellipse(screen, ABU, self.kotak_atas)
        pygame.draw.ellipse(screen, PUTIH, self.kotak_bawah)

        # gambar garis ukur
        for x in range(3):
            self.buat_kotak_ukurx()
            self.buat_kotak_ukury()

            pygame.draw.rect(screen, MERAH_TUA, self.garis)
            pygame.draw.rect(screen, PUTIH, self.garis2)
            pygame.draw.rect(screen, BIRU_TUA, self.garis3)
            pygame.draw.rect(screen, PUTIH, self.garis4)

        # reset posisi garis ukur
        self.pos_dinamisY[1] = self.pos_awalY[1] - self.p_garis
        self.pos_dinamisX[0] = self.pos_awalX[0] - self.p_garis

        # gambar kotak UI bawah
        pygame.draw.rect(screen, HIJAU_TUA, self.ui)

    def buat_kotak_ukurx(self):
        self.pos_dinamisX[0] += self.p_garis
        self.garis3 = pygame.Rect(self.pos_dinamisX, (self.p_garis, self.l_garis))
        self.pos_dinamisX[0] += self.p_garis
        self.garis4 = pygame.Rect(self.pos_dinamisX, (self.p_garis, self.l_garis))

    def buat_kotak_ukury(self):
        self.pos_dinamisY[1] += self.p_garis
        self.garis = pygame.Rect(self.pos_dinamisY, (self.l_garis, self.p_garis))
        self.pos_dinamisY[1] += self.p_garis
        self.garis2 = pygame.Rect(self.pos_dinamisY, (self.l_garis, self.p_garis))
