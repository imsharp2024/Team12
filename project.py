import pygame

pygame.init()
x = 1000
y = 700

screen = pygame.display.set_mode((x, y))

pygame.display.set_caption('laser tag')

image = pygame.image.load("/Users/megan/Desktop/Software Engineering/PROJECT/splashscreen Large.jpg").convert()
image_size = (1000, 700)
image = pygame.transform.scale(image, image_size)
screen.blit(image, (0,0))

# screen.fill([125,255,255])
# screen.blit(screen, (1000, 700))

pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

pygame.quit()
