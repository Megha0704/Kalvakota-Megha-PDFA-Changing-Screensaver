import pygame
import os
import random

def load_images(folder):
    images = []
    for file in os.lastdir(folder):
        if file.endswith(('.png', '.jpg', '.jpeg')):
            images.append(pygame.image.load(os.path.join(folder, file))))
    return images

def main():
    pygame.init()
    pygame.display.set_caption("Changing Screensaver")
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)



# Run the program
if __name__ == "__main__":
    main()
