# Feb-07-2025
# main_6stars.py

from pathlib import Path

from hdss.src import cfg
from hdss.src.utils import init_directory
from hdss.src.set_params import set_params
from hdss.src.create_shapes import create_shapes
import colors


dir_name = 'data_6stars'
init_directory(dir_name)

set_params(
        200,             # shape_size
        3,         # number_of_shapes
        True,        # perspective_flag
        6,        # bezier_noise_param
        3)            # line_thickness

cfg.flag_fill = True
cfg.fill_color = colors.teal
cfg.contour_color = colors.ocean

shape_name = '6star'
dir_curves = Path.cwd() / '_CURVES_'
path_curve = dir_curves / '6star_curve.txt'

create_shapes(dir_name, shape_name, path_curve)
