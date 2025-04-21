# Apr-21-2025
# set_persp_transform.py

import cv2 as cv
import numpy as np
import random

from hdss.src import cfg


def set_persp_transform():

    if not cfg.perspective_flag:

        cfg.x_tr_in = cfg.image_size
        cfg.y_tr_in = 0

        cfg.x_tl_in = 0
        cfg.y_tl_in = 0

        cfg.x_bl_in = 0
        cfg.y_bl_in = cfg.image_size

        cfg.x_br_in = cfg.image_size
        cfg.y_br_in = cfg.image_size

        matrix = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

        return matrix

    # Points order: top-right, top-left, bottom-left, bottom-right

    # IN
    # -----------------------------------------------------
    random.seed(None)

    cfg.x_tr_in = cfg.image_size + random_persp_shift()
    cfg.y_tr_in = -random_persp_shift()

    cfg.x_tl_in = -random_persp_shift()
    cfg.y_tl_in = -random_persp_shift()

    cfg.x_bl_in = -random_persp_shift()
    cfg.y_bl_in = cfg.image_size + random_persp_shift()

    cfg.x_br_in = cfg.image_size + random_persp_shift()
    cfg.y_br_in = cfg.image_size + random_persp_shift()
    # -----------------------------------------------------

    # OUT
    # ---------------------------------------------------------
    cfg.x_tr_out = cfg.image_size
    cfg.y_tr_out = 0

    cfg.x_tl_out = 0
    cfg.y_tl_out = 0

    cfg.x_bl_out = 0
    cfg.y_bl_out = cfg.image_size

    cfg.x_br_out = cfg.image_size
    cfg.y_br_out = cfg.image_size
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    pts1 = np.float32([[cfg.x_tr_in, cfg.y_tr_in], [cfg.x_tl_in, cfg.y_tl_in],
                       [cfg.x_bl_in, cfg.y_bl_in], [cfg.x_br_in, cfg.y_br_in]])

    pts2 = np.float32([[cfg.x_tr_out, cfg.y_tr_out], [cfg.x_tl_out, cfg.y_tl_out],
                       [cfg.x_bl_out, cfg.y_bl_out], [cfg.x_br_out, cfg.y_br_out]])

    matrix = cv.getPerspectiveTransform(pts1, pts2)
    # ---------------------------------------------------------

    return matrix


def random_persp_shift():
    return random.uniform(0.0, cfg.image_size / 2.0)


def point_persp_transform(matrix, x_in, y_in):
    x_out = matrix[0, 0] * x_in + matrix[0, 1] * y_in + matrix[0, 2]
    y_out = matrix[1, 0] * x_in + matrix[1, 1] * y_in + matrix[1, 2]
    z_out = matrix[2, 0] * x_in + matrix[2, 1] * y_in + matrix[2, 2]

    x_out = x_out / z_out
    y_out = y_out / z_out

    return x_out, y_out


def print_persp_transform(matrix):
    print()
    print(f'matrix[0, 0] = {matrix[0, 0]}')
    print(f'matrix[0, 1] = {matrix[0, 1]}')
    print(f'matrix[0, 2] = {matrix[0, 2]}')

    print()
    print(f'matrix[1, 0] = {matrix[1, 0]}')
    print(f'matrix[1, 1] = {matrix[1, 1]}')
    print(f'matrix[1, 2] = {matrix[1, 2]}')

    print()
    print(f'matrix[2, 0] = {matrix[2, 0]}')
    print(f'matrix[2, 1] = {matrix[2, 1]}')
    print(f'matrix[2, 2] = {matrix[2, 2]}')


def print_persp_rect():
    # ---------------------------------------------------------
    x1_in = cfg.x_tr_in
    y1_in = cfg.y_tr_in

    x2_in = cfg.x_tl_in
    y2_in = cfg.y_tl_in

    x3_in = cfg.x_bl_in
    y3_in = cfg.y_bl_in

    x4_in = cfg.x_br_in
    y4_in = cfg.y_br_in
    # ---------------------------------------------------------
    x1_out = cfg.x_tr_out
    y1_out = cfg.y_tr_out

    x2_out = cfg.x_tl_out
    y2_out = cfg.y_tl_out

    x3_out = cfg.x_bl_out
    y3_out = cfg.y_bl_out

    x4_out = cfg.x_br_out
    y4_out = cfg.y_br_out
    # ---------------------------------------------------------
    print(f'\nPerspective rectangles:')
    print(f'---------------------------')
    print(f'x1_in = {x1_in}\t y1_in = {y1_in}')
    print(f'x2_in = {x2_in}\t y2_in = {y2_in}')
    print(f'x3_in = {x3_in}\t y3_in = {y3_in}')
    print(f'x4_in = {x4_in}\t y4_in = {y4_in}')
    print()
    print(f'x1_out = {int(round(x1_out))}\t y1_out = {int(round(y1_out))}')
    print(f'x2_out = {int(round(x2_out))}\t y2_out = {int(round(y2_out))}')
    print(f'x3_out = {int(round(x3_out))}\t y3_out = {int(round(y3_out))}')
    print(f'x4_out = {int(round(x4_out))}\t y4_out = {int(round(y4_out))}')
    print(f'---------------------------')
    # ---------------------------------------------------------
