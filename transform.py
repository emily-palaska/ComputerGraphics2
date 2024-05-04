import numpy as np

class Transform:
# Interface to implement an Affine Transformation (rotation + translation)
    def __init__(self):
        # Initialize a Transform object.
        self.mat = np.eye(4)

    def rotate(self, theta: float, u: np.ndarray) -> None:
    # Perform a rotation by an angle along an axis
    #  Input:
    #    theta: the angle of rotation (clockwise and in rads)
    #    u: the normalized vector of the rotation axis
    
        # Extract cosine, sine and coordinates of u
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
        # Rotate the transformation matrix
        self.mat = R @ self.mat

    def translate(self, t: np.ndarray) -> None:
    # Perform a translation by a vector
    #  Input:
    #    t: the np vector of translation with form [x, y, z]
        
        # Update the translation part of the matrix
        self.mat[:3, 3] += t.T

    def transform_pts(self, pts: np.ndarray) -> np.ndarray:
    # Apply the Affine transformation to certain points
    #  Input:
    #    pts: the points to be transformed as a Nx3 np array
    #  Output:
    #    transformed_pts: the points after applying the transformation as an Nx3 np array
    
        # Turn to homogeneous coordinates by adding a row of ones to the points.
        ones_row = np.ones((1, pts.shape[1]))
        pts_homo = np.vstack([pts, ones_row])
        # Transform the specified points according to our current matrix and return the result.
        tranformed_pts = self.mat @ pts_homo
        return tranformed_pts[:3, :]

if __name__ == "__main__":
    trans = Transform()
    trans.translate(np.array([0,0,1]))
    pts = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    print(trans.transform_pts(pts))