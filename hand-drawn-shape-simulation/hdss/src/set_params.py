from hdss.src import cfg


def set_params(
        shape_size,
        number_of_shapes,
        perspective_flag,
        bezier_noise_param,
        line_thickness):

    cfg.image_size = shape_size
    cfg.n_shapes = number_of_shapes
    cfg.perspective_flag = perspective_flag
    cfg.bezier_noise_param = bezier_noise_param
    cfg.line_thickness = line_thickness
