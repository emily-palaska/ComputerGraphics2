import numpy as np

class Transform:
    # Interface for performing affine transformations.
    def __init__(self):
        # Initialize a Transform object.
        self.mat = np.eye(4)

    def rotate(self, theta: float, u: np.ndarray) -> None:
        # rotate the transformation matrix
        c = np.cos(theta)
        s = np.sin(theta)
        ux, uy, uz = u
        
        # Construct the rotation matrix
        R = np.array([
            [c + ux**2*(1-c), ux*uy*(1-c) - uz*s, ux*uz*(1-c) + uy*s, 0],
            [uy*ux*(1-c) + uz*s, c + uy**2*(1-c), uy*uz*(1-c) - ux*s, 0],
            [uz*ux*(1-c) - uy*s, uz*uy*(1-c) + ux*s, c + uz**2*(1-c), 0],
            [0, 0, 0, 1]
        ])
        
        self.mat = np.round(R @ self.mat, decimals = 3)


    def translate(self, t: np.ndarray) -> None:
        # translate the transformation matrix.
        translation_matrix = np.eye(4)
        translation_matrix[:3, 3] = t  # Update the translation part of the matrix
        self.mat = np.round(translation_matrix @ self.mat, decimals = 3)

    def transform_pts(self, pts: np.ndarray) -> np.ndarray:
        # transform the specified points
        # according to our current matrix.
        return None

if __name__ == "__main__":
    transformExample = Transform()
    theta = np.pi / 2.0
    u = [1, 0, 0]
    print(transformExample.mat)
    transformExample.rotate(theta, u)
    print(transformExample.mat)