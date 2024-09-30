from pico2d import *

open_canvas(1280, 1024)
grass = load_image('TUK_GROUND.png')
character = load_image('pngwing.com.png')


def handle_events():
    global running
    global xdir
    global ydir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                xdir += 1
            elif event.key ==SDLK_LEFT:
                xdir -= 1
            elif event.key == SDLK_UP:
                ydir += 1
            elif event.key == SDLK_DOWN:
                ydir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                xdir -= 1
            elif event.key == SDLK_LEFT:
                xdir += 1
            elif event.key == SDLK_UP:
                ydir -= 1
            elif event.key == SDLK_DOWN:
                ydir += 1

running = True
x = 1280 // 2
y= 150
frame = 0
xdir = 0
ydir = 0

# fill here
while running:
    clear_canvas()
    grass.draw(640, 512)
    if frame < 3:
        row = 1
        col = frame
        width = 240
        hight = 322
    elif frame == 3:
        row = 1
        col = frame
        width = 256
        hight = 322
    else:
        row = 0 #행
        col = frame - 4
        width = 240
        hight = 345

    character.clip_draw(col * 240, row * 320, width, hight, x, y)
    update_canvas()
    handle_events()

    frame = (frame + 1) % 6

    if 120 <= x + xdir * 10 <= 1280-(120):
        x += xdir * 10

    if 100 <= y + ydir * 10 <= 1024 -(150):
        y += ydir * 10

    delay(0.07)

close_canvas()

