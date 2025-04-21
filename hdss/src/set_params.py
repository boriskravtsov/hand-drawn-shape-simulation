# Apr-21-2025
# set_params.py

from hdss.src import cfg


def set_params(
        scale_factor,
        number_of_shapes,
        perspective_flag,
        bezier_noise_param,
        line_thickness):

    cfg.scale_factor = scale_factor
    cfg.image_size = int(scale_factor * cfg.SIZE)
    cfg.n_shapes = number_of_shapes
    cfg.perspective_flag = perspective_flag
    cfg.bezier_noise_param = bezier_noise_param
    cfg.line_thickness = line_thickness
