import numpy as np

def rasterize(pts_2d: np.ndarray, plane_w: int, plane_h: int, res_w: int, res_h: int) -> np.ndarray:
# Rasterize the incoming 2d points from the camera plane to image pixel coordinates
    # Handle exception of points outside of plane
    if np.any((pts_2d[0] < -plane_w/2) | (pts_2d[0] > plane_w/2)) or np.any((pts_2d[1] < -plane_h/2) | (pts_2d[1] > plane_h/2)):
        print("Invalid points, out of plane")
        return None
    
    # Calculate ratio and offset
    ratio = np.array([[(res_w - 1) / plane_w], [(res_h - 1) / plane_h]])
    offset = np.array([[plane_w / 2], [plane_h / 2]])
    
    # Apply and return rasterization
    return np.round((pts_2d + offset) * ratio).astype(int)

# Example usage
if __name__ == "__main__":
    pts_2d = np.array([[4, 3.9], [4, 4]])
    pts_ras = rasterize(pts_2d, 10, 10, 5, 5)
    print(pts_ras)
