import pygame as pg
def main():
    pg.init()
    screen = pg.display.set_mode((640,480))
    clock = pg.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    while True:
        pressed = pg.key.get_pressed()
        alt_held = pressed[pg.K_LALT] or pressed[pg.K_RALT]
        ctrl_held = pressed[pg.K_LCTRL] or pressed[pg.K_RCTRL]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and ctrl_held:
                    return
                if event.key == pg.K_F4 and alt_held:
                    return
                if event.key == pg.K_ESCAPE:
                    return
                
                if event.key == pg.K_r:
                    mode = 'red'
                if event.key == pg.K_g:
                    mode = 'green'
                if event.key == pg.K_b:
                    mode = 'blue' 
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200,radius + 1)        
                elif event.button == 3:
                    radius = max(1,radius - 1)
            if event.type == pg.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]
        screen.fill((0,0,0))
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i+=1
        pg.display.flip()
        clock.tick(60)
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255,2 * index-256))
    c2 = max(0, min(255,2 * index))
    if color_mode == 'blue':
        color = (c1,c1,c2)
    if color_mode == 'red':
        color = (c2,c1,c1)
    if color_mode == 'green':
        color = (c1,c2,c1)
    dx = start[0] - end[1]
    dy = start[1] - end[0]
    itearations = max(abs(dx), abs(dy))
    for i in range(itearations):
        progress = 1.0 * i / itearations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pg.draw.circle(screen, color, (x, y), width)

main()



