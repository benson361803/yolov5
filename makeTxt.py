import os
import random

def checkdir_exist(path: str):
    if os.path.isdir(path):
        print(path, "Exist")
    else:
        print("mkdir", path)
        os.mkdir(path, mode=0o777)
import argparse
import shutil
root_path = os.getcwd()+'/data'
xmlfilepath = os.path.join(root_path, 'Annotations')
txtsavepath = os.path.join(root_path, 'ImageSets')
labelpath = os.path.join(root_path, 'labels')
imagepath = os.path.join(root_path, 'images')




all_path_list = [xmlfilepath, txtsavepath, labelpath,imagepath]
for path in all_path_list:
    checkdir_exist(path)

train_set = ['train', 'test', 'val']

for set in train_set:
    fp = open(os.path.join(txtsavepath, set+'.txt'), 'w')
    fp.close()






total_xml = os.listdir(xmlfilepath)
trainval_percent = 0.9
train_percent = 0.9
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftest = open(root_path+'/ImageSets/test.txt', 'w')
ftrain = open(root_path+'/ImageSets/train.txt', 'w')
fval = open(root_path+'/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    pngname = total_xml[i][:-4]+'.jpg'
    if i in trainval:
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)

    else:
        ftest.write(name)

ftrain.close()
fval.close()
ftest.close()













# parser = argparse.ArgumentParser()
# parser.add_argument('--a', type=str, default=xmlfilepath, help='Annotation_path')
# parser.add_argument('--b', type=str, default=txtsavepath, help='ImageSets')
#
# opt = parser.parse_args()








