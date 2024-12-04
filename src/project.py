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
    folder_path = "artworks"
    artworks = load_images(folder_path)
    current_image = 0 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running == False
                elif event.key == pygame.K_RIGHT:
                    current_image = (current_image + 1) % len(artworks)
                elif event.key == pygame.K_LEFT:
                    current_image = (current_image - 1) %len(artworks)
        screen.fill ((0, 0, 0))
        image = pygame.transform.scale(artworks[current_image], screen.get_size())
        screen.blit(image, (0, 0))
        pygame.display.flip()
    pygame.QUIT
    
if __name__ == "__main__":
    main()
