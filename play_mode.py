from pico2d import *
import game_framework
import game_world
import pause_mode
import title_mode
import item_select_mode
from boy import Boy
from grass import Grass
from sdl2 import SDLK_0, SDLK_1, SDLK_2, SDLK_e, SDLK_ESCAPE

boy = None
item_window_image = None
item_window_open = False
BALL_SIZES = {
    item_select_mode.ITEM_NONE: None,
    item_select_mode.ITEM_SMALL_BALL: 21,
    item_select_mode.ITEM_LARGE_BALL: 41,
}
ITEM_KEYS = {
    SDLK_0: item_select_mode.ITEM_NONE,
    SDLK_1: item_select_mode.ITEM_SMALL_BALL,
    SDLK_2: item_select_mode.ITEM_LARGE_BALL,
}

def handle_events():
    global item_window_open
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif item_window_open:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                item_window_open = False
                return
            elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
                item_window_open = False
                return
            elif event.type == SDL_KEYDOWN and event.key in ITEM_KEYS:
                item_select_mode.selected_item = ITEM_KEYS[event.key]
                boy.ball_size = BALL_SIZES[item_select_mode.selected_item]
                item_window_open = False
                return
            continue
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            item_window_open = True
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return
        else:
            boy.handle_event(event)


def init():
    global boy, item_window_image, item_window_open
    try:
        ball_size = BALL_SIZES[item_select_mode.selected_item]
    except KeyError as error:
        raise ValueError(
            'Unknown item selection: {}'.format(item_select_mode.selected_item)
        ) from error
    boy = Boy(ball_size)
    item_window_image = load_image('item_select.png')
    item_window_open = False
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)


def pause():
    if boy is not None and boy.state == 'RUN':
        boy.pressed_keys.clear()
        boy.dir = 0
        boy.stop_run()


def resume():
    pass

def update():
    if not item_window_open:
        game_world.update()


def render():
    clear_canvas()
    game_world.render()
    if item_window_open:
        item_window_image.draw(400, 300)
    update_canvas()

def finish():
    global boy, item_window_image, item_window_open
    game_world.clear()
    boy = None
    item_window_image = None
    item_window_open = False
