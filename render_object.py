import numpy as np
from lookat import lookat
from perspective_project import perspective_project
from rasterize import rasterize
from render_img import render_img

def render_object(v_pos, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target) -> np.ndarray:
# render the specified object from the specified camera.
    # Get  the rotation matrix and translation vector
    (R, t) = lookat(eye, up, target)
    # Project the points onto the plane
    (pts_2d, depth) = perspective_project(v_pos, focal, R, t)
    # Convert the plane to image pixels
    faces = rasterize(pts_2d, plane_w, plane_h, res_w, res_h).T
    # Redner the image with Gouraud shading
    img = render_img(faces, t_pos_idx, v_clr, depth, 'g')
    return img