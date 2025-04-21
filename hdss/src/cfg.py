# Apr-21-2025
# cfg.py

SIZE = 100

scale_factor: float = 1.0
image_size: int = SIZE
n_shapes: int = 0
perspective_flag: bool = False
bezier_noise_param: int = 0
line_thickness: int = 0

# fill point
# -----------------------------
show_fill_point: bool = False

x_fill_point_in: int = 0
y_fill_point_in: int = 0
fill_point_in = (x_fill_point_in, y_fill_point_in)

x_fill_point_out: int = 0
y_fill_point_out: int = 0
fill_point_out = (x_fill_point_out, y_fill_point_out)
# -----------------------------

# colors (BGR)
# -----------------------------------------
black = (0, 0, 0)
maraschino = (0, 38, 255)
clover = (0, 143, 0)
aqua = (255, 150, 0)
cayenne = (0, 17, 148)
blueberry = (255, 51, 4)
magenta = (255, 64, 255)
ocean = (147, 84, 0)
nickel = (146, 146, 146)
moss = (81, 144, 0)
lemon = (0, 251, 255)
teal = (147, 145, 0)
gray = (128, 128, 128)
dark_gray = (96, 96, 96)
white = (255, 255, 255)
# -----------------------------------------

flag_fill: bool = False
contour_color = black
fill_color = black

# perspective rectangles
# -----------------------------
x_tr_in: float = 0
y_tr_in: float = 0
x_tl_in: float = 0
y_tl_in: float = 0
x_bl_in: float = 0
y_bl_in: float = 0
x_br_in: float = 0
y_br_in: float = 0

x_tr_out: float = 0
y_tr_out: float = 0
x_tl_out: float = 0
y_tl_out: float = 0
x_bl_out: float = 0
y_bl_out: float = 0
x_br_out: float = 0
y_br_out: float = 0
# -----------------------------
