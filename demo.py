from scipy.io import loadmat


def read_data(file_dir, file_name):
    file = loadmat(file_dir)
    file_load = None

    # 读取PU数据

    file_keys = file.keys()
    for key in file_keys:
        if file_name.startswith(key):
            file_load = file[key][0][0][2][0][6][2].ravel()

    return file_load

file_dir = "PU/N09_M07_F10"
file_name = "N09_M07_F10_KA04_1.mat"
file_load = read_data(file_dir, file_name)

