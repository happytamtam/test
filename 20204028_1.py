import os
import glob
import shutil

path = os.getcwd()

print(path) #課題1

new_dir_path = path + '/new-dir'
new_dir_path2 = path + '/new-dir2'

file_kakunin = os.path.exists(new_dir_path)

if file_kakunin == False: #課題2
    os.makedirs(new_dir_path)
    os.makedirs(new_dir_path2)
else:
    pass

files = os.listdir(new_dir_path)
new_dir = path + '/new-dir/'


for x in files: #課題3 & 課題4
    file_size =os.path.getsize(new_dir+ x)
    print(x,str(file_size))
    os.rename(new_dir + x,new_dir + x + "2")

print(os.listdir(new_dir_path))

txt = glob.glob(new_dir + "*.txt*") #課題5 画像の場合は「.jpg」

print(txt)

new_dir2 = path + '/new-dir2/'
new_path = shutil.move(txt[0], new_dir2) #課題6

print(os.listdir(new_dir2))






