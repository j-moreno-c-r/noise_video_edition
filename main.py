import pygame
import numpy as np
# Initialize pygame
pygame.init()

# Set up the audio
sample_rate = 44100
duration = 0.1  # Duration of the noise in seconds
frequency = 880  # Frequency of the high-pitched noise in Hz

# Function to generate a high-pitched noise
def generate_noise(duration, frequency, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    noise = 0.5 * np.sin(2 * np.pi * frequency * t)
    return np.int16(noise * 32767).tobytes()

# Create a pygame sound object
def create_sound(duration, frequency, sample_rate):
    noise = generate_noise(duration, frequency, sample_rate)
    return pygame.mixer.Sound(buffer=noise)

# Create the sound
noise_sound = create_sound(duration, frequency, sample_rate)

# Set up the display (not really needed for audio, but pygame requires a window)
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Noise Generator")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL:
                noise_sound.play()

    pygame.display.flip()

# Quit pygame
pygame.quit()