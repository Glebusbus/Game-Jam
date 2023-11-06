from numba import njit
import numpy as np
import pygame as pg
import math

height_map_img = pg.image.load('assets/imgs/maps/img_height_map.png')
height_map_img = pg.surfarray.array3d(height_map_img)
map_img = pg.image.load('assets/imgs/maps/img_map.png')
map_img = pg.surfarray.array3d(map_img)

map_height = len(height_map_img[0])
map_widht = len(height_map_img)


@njit(fastmath=True)
def raycasting(screen, player_pos, player_angle, player_height, player_pitch,
               screen_width, screen_height, delta_angle, ray_distance, h_fov, scale_height):
    screen[:] = np.array([0, 0, 0])
    y_bufer = np.full(screen_width, screen_height)
    ray_angle = player_angle - h_fov

    for num_ray in range(screen_width):
        first_contact = False
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)
        for depth in range(1, ray_distance):
            x = int(player_pos[0] + depth * cos_a)
            if 0 < x < map_widht:
                y = int(player_pos[1] + depth * sin_a)
            else:
                y = int(player_pos[1] + depth * sin_a)
                if x >= map_widht:
                    x %= map_widht
                else:
                    x = map_widht - ((-x) % map_widht) - 1

            if 0 < y < map_height:
                pass
            else:
                if y >= map_height:
                    y %= map_height
                else:
                    y = map_height - ((-y) % map_height) - 1
            height_on_screen = int(((player_height - height_map_img[x, y][0]) /
                                    depth / math.cos(player_angle - ray_angle) * scale_height) +5 * math.cosh(
                (depth) / 500) + player_pitch)
            if not first_contact:
                y_bufer[num_ray] = min(height_on_screen, screen_height)
                first_contact = True

                # remove mirror bug
            if height_on_screen < 0:
                height_on_screen = 0

            if height_on_screen < y_bufer[num_ray]:
                for screen_y in range(height_on_screen, y_bufer[num_ray]):
                    screen[num_ray, screen_y] = map_img[x, y]
                y_bufer[num_ray] = height_on_screen

        ray_angle += abs(
            math.atan2(screen_width / 2 - num_ray, screen_width / 2) - math.atan2(screen_width / 2 - num_ray + 1,
                                                                                  screen_width / 2))
    return screen


class VoxelRender:
    def __init__(self, App):
        cof = 4
        self.h_res, self.w_res = int(App.HEIGHT / (cof ** 0.5)), int(App.WIDHT / (cof ** 0.5))
        self.App = App
        self.camera = App.camera
        self.fov = math.pi / 2
        self.h_fov = self.fov / 2
        self.num_rays = self.w_res
        self.delta_angle = self.fov / self.num_rays
        self.ray_distance = 2000
        self.scale_height = 720
        self.screen = np.full((self.w_res, self.h_res, 3), (0, 0, 0))

    def update(self):
        self.screen = raycasting(self.screen, self.camera.pos, self.camera.angle,
                                 self.camera.height, self.camera.pitch, self.w_res,
                                 self.h_res, self.delta_angle, self.ray_distance,
                                 self.h_fov, self.scale_height)

    def draw(self):
        self.App.SC.blit(pg.transform.scale(pg.surfarray.make_surface(self.screen), (self.App.WIDHT, self.App.HEIGHT)),
                         (0, 0))
        pass
