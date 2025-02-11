# Feb-11-2025
# main_hearts.py

from pathlib import Path

from hdss.src import cfg
from hdss.src.utils import init_directory
from hdss.src.set_params import set_params
from hdss.src.create_shapes import create_shapes
import colors


dir_name = 'data_hearts'
init_directory(dir_name)

set_params(
        200,             # shape_size = 200 x 200
        5,         # number_of_shapes
        True,        # perspective_flag
        7,         # bezier_noise_param
        2)             # line_thickness

cfg.flag_fill = True
cfg.fill_color = colors.maraschino
cfg.contour_color = colors.maraschino

shape_name = 'heart'
dir_curves = Path.cwd() / '_CURVES_'
path_curve1 = dir_curves / 'heart_curve1.txt'
path_curve2 = dir_curves / 'heart_curve2.txt'

create_shapes(dir_name, shape_name, path_curve1, path_curve2)
