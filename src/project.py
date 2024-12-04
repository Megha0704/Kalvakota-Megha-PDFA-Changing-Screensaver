import pygame
import os
import random

def load_images(folder):
    images = []
    for file in os.listdir(folder):
        if file.endswith(('.png', '.jpg', '.jpeg')):
            images.append(pygame.image.load(os.path.join(folder, file)))
    return images

def scale_image(image, screen_size):
    img_width, img_height = image.get_size()
    screen_width, screen_height = screen_size
    if img_width == 0 or img_height == 0:
        raise ValueError("Invalid image dimensions")
    scale_factor = min(screen_width / img_width, screen_height / img_height)
    new_width = int(img_width * scale_factor)
    new_height = int(img_height * scale_factor)
    scaled_image = pygame.transform.scale(image, (new_width, new_height))
    return scaled_image

def main():
    pygame.init()
    pygame.display.set_caption("Changing Screensaver")
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    folder_path = "artworks"
    artworks = load_images(folder_path)
    current_image = 0 
    running = True
    Auto_Cycle = pygame.USEREVENT + 1
    pygame.time.set_timer(Auto_Cycle, 3500)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_RIGHT:
                    current_image = (current_image + 1) % len(artworks)
                elif event.key == pygame.K_LEFT:
                    current_image = (current_image - 1) %len(artworks)
        screen.fill ((0, 0, 0))
        image = scale_image(artworks[current_image], screen.get_size())
        x = (screen.get_width() - image.get_width()) // 2
        y = (screen.get_height() - image.get_height()) // 2
        screen.blit(image, (x, y))
        pygame.display.flip()
    pygame.QUIT

if __name__ == "__main__":
    main()
