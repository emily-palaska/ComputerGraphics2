import numpy as np
from render_object import render_object

data = np.load('hw2.npy', allow_pickle=True).item()
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
print(res_w)