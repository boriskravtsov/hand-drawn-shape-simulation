# Apr-21-2025
# main_4stars.py

from pathlib import Path

from hdss.src import cfg
from hdss.src.utils import init_directory
from hdss.src.set_params import set_params
from hdss.src.set_fill_point import set_fill_point
from hdss.src.create_shapes import create_shapes


dir_name = 'data_4stars'
init_directory(dir_name)

set_params(
        2.0,
        3,
        True,
        4,
        2)

cfg.flag_fill = False
cfg.show_fill_point = False
cfg.fill_color = cfg.magenta
cfg.contour_color = cfg.magenta

shape_name = '4star'
dir_curves = Path.cwd() / '_CURVES_'
path_curve = dir_curves / '4star_curve.txt'

set_fill_point(50, 50)

create_shapes(dir_name, shape_name, path_curve)
