import pygame

pygame.init()

screen_width=480
screen_height=640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("게임")

background = pygame.image.load("C:/Users/82106/OneDrive/바탕 화면/pygame_basic/background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    pygame.display.update()


pygame.quit()