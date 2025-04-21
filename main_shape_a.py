# Apr-21-2025
# main_shape_a.py

from pathlib import Path

from hdss.src import cfg
from hdss.src.utils import init_directory
from hdss.src.set_params import set_params
from hdss.src.set_fill_point import set_fill_point
from hdss.src.create_shapes import create_shapes


dir_name = 'data_shape_a'
init_directory(dir_name)

set_params(
        2.0,
        3,
        True,
        4,
        1)

cfg.flag_fill = True
cfg.show_fill_point = True
cfg.fill_color = cfg.lemon
cfg.contour_color = cfg.black

shape_name = 'shape_a'
dir_curves = Path.cwd() / '_CURVES_'
path_curve1 = dir_curves / 'shape_a_1.txt'
path_curve2 = dir_curves / 'shape_a_2.txt'

set_fill_point(49, 24)

create_shapes(dir_name, shape_name,path_curve1, path_curve2)
