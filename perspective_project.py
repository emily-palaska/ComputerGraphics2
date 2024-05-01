import numpy as np
from world2view import world2view

def perspective_project(pts: np.ndarray, focal: float, R: np.ndarray, t: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
# Project the specified 3d points pts on the image plane, according to a pinhole perspective projection model.
    # Transform points to camera coordinates using the implemented function
    pts_c = world2view(pts, R, t)
    if 0 in pts_c[:, 2]:
        print("Invalid arguments")
        return None
    # Extract depth
    depth = pts_c[-1]
    # Project them to the image plane and return the results
    pts_f = pts_c[:2, :] / depth
    return (pts_f, depth)