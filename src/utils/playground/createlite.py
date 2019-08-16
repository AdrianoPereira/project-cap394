import os
import subprocess
import re

PATH_FULLY = '../../data/full/output_v2'
PATH_LITE = '../../data/lite'
TOTAL = 10

files = []
for file in os.listdir(PATH_FULLY):
    if not re.search('.gz$', file):
        files.append(file)

files = sorted(files)
files = files[::-1]

des_fam_dir = os.path.join(PATH_LITE, 'fam') 
des_mat_dir = os.path.join(PATH_LITE, 'mat')

if not os.path.exists(des_fam_dir):
    os.makedirs(des_fam_dir)
if not os.path.exists(des_mat_dir):
    os.makedirs(des_mat_dir)

fam_files = [os.path.join(PATH_FULLY, file) for file in files[:TOTAL]]
mat_files = [os.path.join(PATH_FULLY, file) for file in files[::-1][:TOTAL]]


def copy_files(files, destiny):
    for file in files:
        cmd = 'cp {} {}'.format(file, destiny)
        error = subprocess.call(cmd, shell=True)

        if error:
            print('Fail to copy ', file)
        else:
            print(file, ' copied successfully')

copy_files(fam_files, des_fam_dir)
copy_files(mat_files, des_mat_dir)
