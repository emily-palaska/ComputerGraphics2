import numpy as np

def rasterize(pts_2d: np.ndarray, plane_w: int, plane_h: int, res_w: int, res_h: int) -> np.ndarray:
# Rasterize the incoming 2d points from the camera plane (middle axis) to image pixel coordinates (bottom left axis)
#  Input:
#    pts__2d: Nx2 np array of the 2d projected points in the camera plane
#    plane_w: the width of the camera plane
#    plane_h: the height of the camera plane
#    res_w: the width of the image in pixels
#    res_h: the height of the image in pixels
#  Output:
#    pts_rast: Nx2 np array of the points with pixel coordinates

    # Handle exception of points outside of plane
    if np.any((pts_2d[0] < -plane_w/2) | (pts_2d[0] > plane_w/2)) or np.any((pts_2d[1] < -plane_h/2) | (pts_2d[1] > plane_h/2)):
        print("Invalid points, out of plane")
        return None
    
    # Calculate rasterization ratio and offset
    ratio = np.array([[(res_w - 1) / plane_w], [(res_h - 1) / plane_h]])
    offset = np.array([[plane_w / 2], [plane_h / 2]])
    
    # Apply and return points with pixel coordinates
    return np.round((pts_2d + offset) * ratio).astype(int)
