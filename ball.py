from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    images = {}
    image_paths = {
        21: 'ball21x21.png',
        41: 'ball41x41.png',
    }

    def __init__(self, x, y, velocity, size=21):
        if size not in self.image_paths:
            raise ValueError('Ball size must be 21 or 41 pixels')
        if size not in self.images:
            self.images[size] = load_image(self.image_paths[size])
        self.image = self.images[size]
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
