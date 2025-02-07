import random

from hdss.src import cfg


def random_noise(scale_factor):

    half = scale_factor * cfg.bezier_noise_param / 2.0

    return random.uniform(-half, half)
