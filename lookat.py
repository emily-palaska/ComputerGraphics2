import numpy as np

def lookat(eye: np.ndarray, up: np.ndarray, target: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
# Calculate the camera's view matrix (i.e., its coordinate frame transformation specified
# by a rotation matrix R, and a translation vector t).
# :return a tuple containing the rotation matrix R (3 x 3) and a translation vector t (1 x 3)
    
    # Calculate the three normalized camera vectors
    zc = target - eye
    zc = zc / np.linalg.norm(zc)
    yc = up - np.dot(up, zc) * zc
    yc = yc / np.linalg.norm(yc)
    xc = np.cross(yc, zc)
    xc = xc / np.linalg.norm(xc)

    # Add them to the rotation matrix and return the resutls
    R = np.array([xc, yc, zc])
    return (R.T, eye)

# Exmaple usage
if __name__ == "__main__":
    eye = np.array([15, 15, 1.5])
    target = np.array([30, 30, 4])
    up = np.array([0, 0, 1])
    
    (R, t) = lookat(eye, up, target)
    print(t)
    print(R)