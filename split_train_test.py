import os
from random import shuffle
from os import listdir, getcwd
from os.path import join

if __name__ == '__main__':
    dest = "list/train.txt"
    dest2 = "list/val.txt"

    base = "dataset"

    file_list = [item for item in os.listdir(base) if ".jpg" in item] 
    shuffle(file_list) 
    train_test_ratio = 0.85
    a = int(len(file_list) * train_test_ratio)  

    train_file = open(dest, 'a')
    val_file = open(dest2, 'a')

    print("train set:", len(file_list[:a]))
    print("val set:", len(file_list[a:]))

    for file_obj in file_list[a:]: 
        file_path = os.path.join(base, file_obj)
        val_file.write(file_path + '\n')
        
    for file_obj in file_list[:a]: 
        file_path = os.path.join(base, file_obj)
        train_file.write(file_path + '\n') 

    train_file.close()
    val_file.close()