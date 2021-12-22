import pygame, sys
from random import randint
from pygame.locals import *
from Helpers import *
from Constants import *

# Это голова змеи.
snakeHead = Block(Rect(blockSize, blockSize, blockSize, blockSize), Color(50, 50, 50))

# Это тело змеи.
snakeBody = []

# Это яблоко.
# Вызов randomRect запускает яблоко в случайном месте на экране.

apple = randomBlock(Color(60, 60, 60))


def changeColor(block):
    if (block.color.r < 255 and block.color.g < 255 and block.color.b < 255):
        block.color.r = block.color.r + 1
        block.color.g = block.color.g + 1
        block.color.b = block.color.b + 1


pygame.init()
scrHeight = yBound * blockSize
scrWidth = xBound * blockSize
screen = pygame.display.set_mode((scrHeight, scrWidth))
initWalls(screen)
clock = pygame.time.Clock()


while True:
    clock.tick(10)
    changeColor(snakeHead)

    for keypress in pygame.event.get():
        if keypress.type == QUIT:
            quitGame()


        elif keypress.type == KEYDOWN:

            if keypress.key == K_UP and direction != DOWN:
                direction = UP

            elif keypress.key == K_DOWN and direction != UP:
                direction = DOWN

            elif keypress.key == K_LEFT and direction != RIGHT:
                direction = LEFT

            elif keypress.key == K_RIGHT and direction != LEFT:
                direction = RIGHT


    oldPiece = snakeHead.rect.copy()

    snakeHead.moveInDir(direction)


    for i in range(0, len(snakeBody)):
        temp = snakeBody[i].rect.copy()
        snakeBody[i].rect = moveBody(oldPiece, snakeBody[i].rect)
        oldPiece = temp

    hasHitWall = snakeHead.rect.collidelist(walls) != -1
    hasHitBody = snakeHead.collideList(snakeBody)
    hasEaten = snakeHead.rect.colliderect(apple)

    if(hasHitWall or hasHitBody):
        quitGame()

    if (hasEaten):
        apple = randomBlock(Color(40, 40, 40))
        snakeBody.append(Block(oldPiece, Color(80, 80, 80)))

    draw(oldPiece, snakeHead, snakeBody, apple, hasEaten, screen)
    pygame.display.flip()