import game_framework
from pico2d import clear_canvas, get_events, load_image, update_canvas
from sdl2 import (SDL_KEYDOWN, SDL_QUIT, SDLK_0, SDLK_1, SDLK_2,
                  SDLK_ESCAPE)


image = None
selected_item = None
ITEM_NONE = 0
ITEM_SMALL_BALL = 1
ITEM_LARGE_BALL = 2
ITEM_KEYS = {
    SDLK_0: ITEM_NONE,
    SDLK_1: ITEM_SMALL_BALL,
    SDLK_2: ITEM_LARGE_BALL,
}


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def handle_events():
    global selected_item
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
            return
        if event.type == SDL_KEYDOWN:
            if event.key in ITEM_KEYS:
                selected_item = ITEM_KEYS[event.key]


def update():
    pass


def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
