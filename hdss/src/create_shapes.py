# Apr-21-2025
# create_shapes.py

import cv2 as cv
import numpy as np
from pathlib import Path

from hdss.src import cfg
from hdss.src.bezier_image import bezier_image
from hdss.src.fill_color import fill_color
from hdss.src.set_persp_transform import set_persp_transform, point_persp_transform
from hdss.src.random_noise import random_noise


def create_shapes(dir_name, shape_name, *curves):

    for n_shape in range(cfg.n_shapes):
        create_shape(dir_name, n_shape, shape_name, *curves)


def create_shape(dir_name, n_shape, shape_name, *curves):
    # ---------------------------------------------------------
    height = cfg.image_size
    width = cfg.image_size
    channels = 3
    # ---------------------------------------------------------
    canvas = np.empty((height, width, channels), dtype=np.uint8)
    canvas.fill(255)
    # ---------------------------------------------------------
    matrix_persp = (3, 3)
    matrix_persp = np.zeros(matrix_persp, dtype=np.float32)

    if cfg.perspective_flag:
        matrix_persp = set_persp_transform()
    # ---------------------------------------------------------

    # fill point
    # -----------------------------------------------------
    x_in_scale = cfg.scale_factor * cfg.x_fill_point_in
    y_in_scale = cfg.scale_factor * cfg.y_fill_point_in

    if cfg.perspective_flag:

        x_out, y_out = \
                point_persp_transform(matrix_persp, x_in_scale, y_in_scale)

        cfg.x_fill_point_out = int(x_out)
        cfg.y_fill_point_out = int(y_out)
    else:
        cfg.x_fill_point_out = int(x_in_scale)
        cfg.y_fill_point_out = int(y_in_scale)

    cfg.fill_point_out = (cfg.x_fill_point_out, cfg.y_fill_point_out)
    # -----------------------------------------------------

    # ---------------------------------------------------------
    x_list = []
    y_list = []

    for path_curve in curves:

        control_points = np.loadtxt(path_curve, delimiter=',')
        n_control_points = control_points.shape[0]

        control_points = cfg.scale_factor * control_points

        # Perspective Transform
        # -----------------------------------------------------
        if cfg.perspective_flag:

            for n in range(n_control_points):
                x_in = control_points[n, 0]
                y_in = control_points[n, 1]

                x_out, y_out = \
                    point_persp_transform(matrix_persp, x_in, y_in)

                control_points[n, 0] = x_out
                control_points[n, 1] = y_out
        # -----------------------------------------------------

        # -----------------------------------------------------

        # Random Noise
        # -----------------------------------------------------
        if cfg.bezier_noise_param != 0:

            # random_noise не затрагивает две конечные точки
            for n in range(1, n_control_points - 1):
                control_points[n, 0] \
                    = control_points[n, 0] + random_noise(cfg.scale_factor)
                control_points[n, 1] \
                    = control_points[n, 1] + random_noise(cfg.scale_factor)
        # -----------------------------------------------------

        bezier_image(canvas, control_points)

        for n in range(n_control_points):
            x_list.append(control_points[n, 0])
            y_list.append(control_points[n, 1])

    if cfg.flag_fill:
        seed_fill = (cfg.y_fill_point_out, cfg.x_fill_point_out)
        fill_color(canvas, seed_fill, cfg.fill_color)

    if cfg.show_fill_point:
        draw_fill_point(canvas)

    temp = shape_name + '_' + str(n_shape) + '.png'
    path_shape = str(Path.cwd() / dir_name / temp)
    cv.imwrite(path_shape, canvas)


def draw_fill_point(canvas):

    size: int = 2

    x1 = cfg.x_fill_point_out - size
    y1 = cfg.y_fill_point_out - size
    x2 = cfg.x_fill_point_out + size
    y2 = cfg.y_fill_point_out + size

    color = cfg.black
    thickness = 1

    cv.line(canvas, (x1, y1), (x2, y2), color, thickness)
    cv.line(canvas, (x1, y2), (x2, y1), color, thickness)
