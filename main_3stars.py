# Apr-21-2025
# main_3stars.py

from pathlib import Path

from hdss.src import cfg
from hdss.src.utils import init_directory
from hdss.src.set_params import set_params
from hdss.src.set_fill_point import set_fill_point
from hdss.src.create_shapes import create_shapes


dir_name = 'data_3stars'
init_directory(dir_name)

set_params(
        2.0,
        3,
        True,
        4,
        2)

cfg.flag_fill = True
cfg.show_fill_point = False
cfg.fill_color = cfg.maraschino
cfg.contour_color = cfg.black

shape_name = '3star'
dir_curves = Path.cwd() / '_CURVES_'
path_curve = dir_curves / '3star_curve.txt'

set_fill_point(50, 50)

create_shapes(dir_name, shape_name, path_curve)
