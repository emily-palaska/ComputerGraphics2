import numpy as np
import matplotlib.pyplot as plt

class Transform:
    # Interface for performing affine transformations.
    def __init__(self):
        # Initialize a Transform object.
        self.mat = np.eye(4)

    def rotate(self, theta: float, u: np.ndarray) -> None:
        # rotate the transformation matrix
        c = np.cos(-theta)
        s = np.sin(-theta)
        ux, uy, uz = u
        
        # Construct the rotation matrix
        R = np.array([
            [c + ux**2*(1-c), ux*uy*(1-c) - uz*s, ux*uz*(1-c) + uy*s, 0],
            [uy*ux*(1-c) + uz*s, c + uy**2*(1-c), uy*uz*(1-c) - ux*s, 0],
            [uz*ux*(1-c) - uy*s, uz*uy*(1-c) + ux*s, c + uz**2*(1-c), 0],
            [0, 0, 0, 1]
        ])
        
        self.mat = R @ self.mat

    def translate(self, t: np.ndarray) -> None:
        # translate the transformation matrix.
        translation_matrix = np.eye(4)
        translation_matrix[:3, 3] = t  # Update the translation part of the matrix
        self.mat = np.round(translation_matrix @ self.mat, decimals = 3)

    def transform_pts(self, pts: np.ndarray) -> np.ndarray:
        # transform the specified points
        # according to our current matrix.
        
        # Add homogeneous coordinates to the points
        pts_homo = np.hstack([pts, np.ones((pts.shape[0], 1))])

        # Transform the points using the current transformation matrix
        transformed_pts = np.dot(self.mat, pts_homo.T).T

        # Convert back to Cartesian coordinates
        transformed_pts[:, :-1] /= transformed_pts[:, -1][:, np.newaxis]

        return transformed_pts[:, :-1]

# Example usage
if __name__ == "__main__":
    # Initialize affine transform
    transformExample = Transform()
    theta = np.pi / 2.0
    u = [0, 0, 1]
    t = [0, 0, 0.5]
    transformExample.rotate(theta, u)
    
    
    # Initialize a
    a = np.array([[1, 1+i/10, 1] for i in range(10)])
    # Perform affine transform
    b = transformExample.transform_pts(a)
    transformExample.translate(t)
    c = transformExample.transform_pts(a)
    
    # Plotting the points
    # Extract coordinates
    x0, y0, z0 = [0, 0, 0]
    xu, yu, zu = u
    
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the points
    ax.scatter(a[:, 0], a[:, 1], a[:, 2], c='r', marker='o')
    ax.scatter(b[:, 0], b[:, 1], b[:, 2], c='g', marker='o')
    ax.scatter(c[:, 0], c[:, 1], c[:, 2], c='b', marker='o')

    # Plot the rotation vector
    ax.plot([x0, xu], [y0, yu], [z0, zu], c='y')
    
    plt.show()