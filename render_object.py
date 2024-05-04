import numpy as np
from lookat import lookat
from perspective_project import perspective_project
from rasterize import rasterize
from render_img import render_img

def render_object(v_pos, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target) -> np.ndarray:
# Render the specified object from the specified camera.
#  Input:
#    v_pos: Nx3 np array of the 3d points in WCS
#    v_clr: Nx3 np array of the RGB color codes of the points
#    t_pos_idx: Fx3 np array of triangle vertices by indexing of v_pos
#    plane_w: the width of the camera plane
#    plane_h: the height of the camera plane
#    res_w: the width of the image in pixels
#    res_h: the height of the image in pixels
#    focal: float number of camera lense distance ratio
#    eye: 1x3 np vector specifying the point of the camera
#    up: 1x3 np vector for the up vector
#    target: 1x3 np vector for the 
#  Output:
#    img: plane_w x plane_h nparray of the rendered image's pixels with Gouraud shading

    # Get the rotation matrix and translation vector
    (R, t) = lookat(eye, up, target)

    # Project the points onto the camera plane
    (pts_2d, depth) = perspective_project(v_pos, focal, R, t)

    # Convert the plane to image pixels
    vertices = rasterize(pts_2d, plane_w, plane_h, res_w, res_h).T
    
    # Render the image with Gouraud shading
    return render_img(t_pos_idx, vertices, v_clr, depth, 'g')