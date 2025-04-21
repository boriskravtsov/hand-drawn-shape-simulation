# Apr-21-2025
# set_fill_point.py

from hdss.src import cfg


def set_fill_point(x: int, y: int):

    cfg.x_fill_point_in = x
    cfg.y_fill_point_in = y

    cfg.fill_point_in = (cfg.x_fill_point_in, cfg.y_fill_point_in)
