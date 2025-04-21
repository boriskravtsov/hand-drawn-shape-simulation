# Apr-21-2025
# random_noise.py

import random

from hdss.src import cfg


def random_noise(scale_factor):

    half = int(scale_factor * cfg.bezier_noise_param / 2.0)

    return random.uniform(-half, half)
