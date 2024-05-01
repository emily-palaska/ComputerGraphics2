import numpy as np

def world2view(pts: np.ndarray, R: np.ndarray, c0: np.ndarray) -> np.ndarray:
# Implements a world-to-view transform, i.e. transforms the specified
# points to the coordinate frame of a camera. The camera coordinate frame
# is specified rotation (w.r.t. the world frame) and its point of reference
# (w.r.t. to the world frame).
    # Translate points to be relative to camera reference point
    pts_rel = pts - c0
    
    # Apply rotation to points
    pts_rotated = np.dot(R, pts_rel.T).T
    
    return np.round(pts_rotated, decimals=3)

# Example usage
if __name__=="__main__":
    # Define points in the world coordinate system
    pts_world = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])

    # Example rotation matrix (3x3)
    # Assuming R is a valid rotation matrix
    R = np.array([[0.8, -0.6, 0.0], 
                  [0.6, 0.8, 0.0], 
                  [0.0, 0.0, 1.0]]) 

    # Example camera reference point
    c0 = np.array([1, 1, 1])

    # Transform points to camera coordinate system
    pts_camera = world2view(pts_world, R, c0)

    print("Points in camera coordinate system:")
    print(pts_camera)