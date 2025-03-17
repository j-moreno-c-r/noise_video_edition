import pygame
import numpy as np
pygame.init()

sample_rate = 44100
duration = 0.1  
frequency = 880  

def generate_noise(duration, frequency, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    noise = 0.5 * np.sin(2 * np.pi * frequency * t)
    return np.int16(noise * 32767).tobytes()

def create_sound(duration, frequency, sample_rate):
    noise = generate_noise(duration, frequency, sample_rate)
    return pygame.mixer.Sound(buffer=noise)

noise_sound = create_sound(duration, frequency, sample_rate)

screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Noise Generator")
imp = pygame.image.load("~/$USER_NAME/Making_noise_video/img.png").convert()
screen.blit(imp, (0, 0))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #here motherfucker you configure the key in the case the a key.
            if event.key == pygame.K_a:
                noise_sound.play()

    pygame.display.flip()

# Quit pygame
pygame.quit()