import numpy as np
import matplotlib.pyplot as plt
from transform import Transform
from render_object import render_object

# Load file
data = np.load('hw2.npy', allow_pickle=True).item()

# Extract data to vectors
v_pos = data['v_pos']
v_clr = data['v_clr']
t_pos_idx = data['t_pos_idx']
eye = data['eye']
up = data['up']
target = data['target']
focal = data['focal']
plane_w = data['plane_w']
plane_h = data['plane_h']
res_w = data['res_w']
res_h = data['res_h']
theta_0 = data['theta_0'] 
rot_axis_0 = data['rot_axis_0']
t_0 = data['t_0']
t_1 = data['t_1']

# Initialize three Transform instances
transform1 = Transform()
transform2 = Transform()
transform3 = Transform()

# Capture initial image
img0 = render_object(v_pos, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)
                     
# Rotate points and capture the first image
transform1.rotate(theta_0, rot_axis_0)
v_pos1 = transform1.transform_pts(v_pos)
img1 = render_object(v_pos1, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)

# Translate points and capture the second image
transform2.translate(t_0)
v_pos2 = transform2.transform_pts(v_pos1)
img2 = render_object(v_pos2, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)

# Translate points and capture the third image
transform3.translate(t_1)
v_pos3 = transform3.transform_pts(v_pos2)
img3 = render_object(v_pos3, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)

# Save results locally with .jpg extension
plt.imsave('result0.jpg', img0)
plt.imsave('result1.jpg', img1)
plt.imsave('result2.jpg', img2)
plt.imsave('result3.jpg', img3)