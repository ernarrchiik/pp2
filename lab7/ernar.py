import datetime
import pygame as pg
#display
screen = pg.display.set_mode((800,800))
pg.display.set_caption("Chasiki Mickey")
clock = pg.time.Clock()
#images
chasiki = pg.image.load("/Users/ernarberenbaj/python/lab7/mickey.png")
chasiki = pg.transform.scale(chasiki,(600,600))

minute_hand = pg.image.load("/Users/ernarberenbaj/python/lab7/righthand.png")
minute_hand = pg.transform.scale(minute_hand,(800,700))

second_hand = pg.image.load("/Users/ernarberenbaj/python/lab7/lefthand.png")
second_hand = pg.transform.scale(second_hand,(40,500))
#begin
done  = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    #times
    my_time = datetime.datetime.now()
    minuteRN = int(my_time.strftime("%M"))
    secondRN = int(my_time.strftime("%S"))
    #angles
    angleM = minuteRN * 7 * -1 - 10
    angleS = secondRN * 6 * -1 - 5
    #rotate
    minute = pg.transform.rotate(minute_hand,angleM)
    second = pg.transform.rotate(second_hand,angleS)
    #screens
    screen.fill((255,255,255))
    screen.blit(chasiki,(100,100))
    screen.blit(minute,(399 - int(minute.get_width() / 2),400 - int(minute.get_height() / 2)))
    screen.blit(second,(399 - int(second.get_width() / 2),400 - int(second.get_height() / 2)))
    pg.display.flip()
    clock.tick(120)
pg.quit()