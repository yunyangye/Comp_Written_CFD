import numpy as np

# Unit: in
wall = [[0,0],[14,0],[14,120],[0,120]]
core = range(6,120,12)
thickness = 2
rotation = 10

node = []
for y in core:
    temp = []
    
    x_len = 6.*np.sin(float(rotation)/180.*np.pi)
    y_len = 6.*np.cos(float(rotation)/180.*np.pi)
    x_min_len = float(thickness)/2.*np.cos(float(rotation)/180.*np.pi)
    y_min_len = float(thickness)/2.*np.sin(float(rotation)/180.*np.pi)
    
    temp.append([7-x_len+x_min_len,y-y_len-y_min_len])
    temp.append([7+x_len+x_min_len,y+y_len-y_min_len])
    temp.append([7+x_len-x_min_len,y+y_len+y_min_len])
    temp.append([7-x_len-x_min_len,y-y_len+y_min_len])
    
    node.append(temp)

lines = ['Item,x1,y1,x2,y2,x3,y3,x4,y4\n']

temp = 'wall'
for row in wall:
    for x in row:
        temp += ','
        temp += str(x)
temp += '\n'
lines.append(temp)

for ind,row in enumerate(node):
    temp = 'node'+str(ind+1)
    for row1 in row:
        for x in row1:
            temp += ','
            temp += str(x)
    temp += '\n'
    lines.append(temp)
    
f = open('./node_result.csv','wb')
for x in lines:
    f.writelines(x)
f.close()
