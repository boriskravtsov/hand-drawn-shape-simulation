# Apr-21-2025
# fill_color.py

"""
    https://gist.github.com/JDWarner/1158a9515c7f1b1c21f1

    Thanks, JDWarner!
"""

def fill_color(data, start_coords, fill_value):
    """
    Flood fill algorithm for RGB images.

    Parameters
    ----------
    data : (M, N, 3) ndarray of uint8 type
        Color image with flood to be filled. Modified inplace.
    start_coords : tuple
        Length-2 tuple of ints defining (row, col) start coordinates.
    fill_value : tuple
        Tuple (B, G, R) the flooded area will take after the fill.

    Returns
    -------
    None, ``data`` is modified inplace.
    """

    height, width, _ = data.shape
    orig_value = tuple(data[start_coords[0], start_coords[1]])

    stack = {(start_coords[0], start_coords[1])}

    if fill_value == orig_value:
        raise ValueError("Filling region with the same value already present is unsupported.")

    while stack:
        y, x = stack.pop()

        if tuple(data[y, x]) == orig_value:
            data[y, x] = fill_value
            if y > 0:
                stack.add((y - 1, x))
            if y < (height - 1):
                stack.add((y + 1, x))
            if x > 0:
                stack.add((y, x - 1))
            if x < (width - 1):
                stack.add((y, x + 1))
