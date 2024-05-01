import numpy as np

def perspective_project(pts: np.ndarray, focal: float, R: np.ndarray, t: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
# Project the specified 3d points pts on the image plane, according to a pinhole perspective projection model.
    # Transform points to camera coordinates
    pts_c = R.T @ (pts.T - t.T).T
    if 0 in pts_c[:, 2]:
        print("Invalid arguments")
        return None
    # Project them to the image plane
    pts_f = pts_c[:2, :] / pts_c[-1]
    return pts_f

# Example usage
if __name__ == "__main__":
    pts = np.array([[i+4, i+3, i+2] for i in range(5)]).T
    t = np.array([1, 1, 1]).T
    R = np.eye(3)
    perspective_project(pts, 1.0, R, t)