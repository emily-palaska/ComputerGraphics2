import numpy as np

def world2view(pts: np.ndarray, R: np.ndarray, c0: np.ndarray) -> np.ndarray:
# Implements a world-to-view transform, i.e. transforms the specified points to the coordinate frame of a camera.
# The camera coordinate frame is specified rotation and its point of reference.
#  Input:
#    pts: 3xN np array of the WCS coordinates of the points
#    R: 3x3 np array of the rotation matrix
#    c0: 1x3 np vector of the camera coordinates
#  Output: the transformed points to the coordinate frame of the camera
    return R.T @ (pts.T - c0.T).T