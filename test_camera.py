import requests
import pygame

url = "http://100.66.148.19/capture"

# Download image
response = requests.get(url, timeout=10)
with open("esp32_image.jpg", "wb") as f:
    f.write(response.content)

print("Image saved as esp32_image.jpg")

# Show fullscreen
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

img = pygame.image.load("esp32_image.jpg")
img = pygame.transform.scale(img, screen.get_size())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            running = False

    screen.blit(img, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()