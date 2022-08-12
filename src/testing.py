from json import load
import os
import pickle
import pan_compensation as pc
import numpy as np

ROOT_DATA_DIR = os.path.join("C:\\Users\\user-pc\\Documents\\Scripts\\old\\FYP", "data", "sunday_amelia", "fte", "fte.pickle")

def load_pickle(path):
    with open(path, 'rb') as f:
        df = pickle.load(f)
    return df

enc_arr = load_pickle("C://Users//user-pc//Desktop//sunday_vals.pickle")
data = load_pickle(ROOT_DATA_DIR)
positions = data["positions"]

for i in range(len(data["positions"])):
    for j in range(len(data["positions"][i])):
        point = data["positions"][i][j]
        enc_val = int(enc_arr[i][1])
        rad_change = pc.count_to_rad(enc_val)
        point = [positions[i][j][0], positions[i][j][1], positions[i][j][2]]
        new_xyz = pc.rotate_point(point,rad_change)
        print('Rotation: {} deg'.format(rad_change*180/np.pi))
        print(new_xyz)
        data["positions"][i][j][0] = new_xyz[0]
        data["positions"][i][j][1] = new_xyz[1]
        data["positions"][i][j][2] = new_xyz[2]

    
print(data["positions"])
output_dir = "C://Users//user-pc//Desktop//new_data.pickle"
with open(output_dir, 'wb') as f:
                pickle.dump(data, f)

print("Saved")