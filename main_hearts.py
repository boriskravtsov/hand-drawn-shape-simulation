# Apr-21-2025
# main_hearts.py

from pathlib import Path

from hdss.src import cfg
from hdss.src.utils import init_directory
from hdss.src.set_params import set_params
from hdss.src.set_fill_point import set_fill_point
from hdss.src.create_shapes import create_shapes


dir_name = 'data_hearts'
init_directory(dir_name)

set_params(
        2.0,
        5,
        True,
        7,
        2)

cfg.flag_fill = False
cfg.show_fill_point = False
cfg.fill_color = cfg.maraschino
cfg.contour_color = cfg.maraschino

shape_name = 'heart'
dir_curves = Path.cwd() / '_CURVES_'
path_curve1 = dir_curves / 'heart_curve1.txt'
path_curve2 = dir_curves / 'heart_curve2.txt'

set_fill_point(50, 50)

create_shapes(dir_name, shape_name, path_curve1, path_curve2)
