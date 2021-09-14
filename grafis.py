import pygame, sys
from interface import Interface
from teks import Teks
from bangunruang import Silinder


class Program:
    def __init__(self, screen):
        self.screen = screen

        self.interface = Interface(Silinder.diameter, Silinder.tinggi)
        self.teks = Teks(Silinder.diameter, Silinder.tinggi)

    def jalankan(self):
        self.interface.gambar(self.screen)
        self.teks.gambar(self.screen)


class Grafis:
    @staticmethod
    def jalankan():
        # Inisialisasi pygame
        pygame.init()
        screen_width = 400
        screen_height = 500
        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        icon = pygame.image.load('Cilinder Icon.png')

        # Set caption, icon, color
        pygame.display.set_caption("Tugas 1: Bangun Ruang")
        pygame.display.set_icon(icon)

        # Inisialisasi program
        program = Program(screen)

        # Loop utama -------------------------------------------------
        while True:
            # Kode Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Updates
            pygame.display.flip()
            screen.fill((50, 100, 50))

            # Kode program
            program.jalankan()

            # Jam
            clock.tick(60)
