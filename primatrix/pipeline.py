# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import shutil
import os
import subprocess as sp
import logging
 

train = pd.DataFrame(pd.read_csv('train_labels.csv', sep=','))
train_col = list(train)
train_subset= ''
dir_base = "/home/rodrigo/datascience/projects/pri-matrixFac/tensorflow/tf_files/primatrix"

if os.path.exists(dir_base):
    shutil.rmtree(dir_base)
    os.makedirs(dir_base)

"""
Data Pipeline from pre classified video files - training data
"""
logging.info("Start - Preparing data for training")


#Loop the mapping file
for fold in  train_col:
    if fold not in ['filename','blank']:
        train_subset = str(pd.DataFrame(train[train[fold] > 0]['filename'])).values.tolist())
        #train_subset = train_subset.replace("'","")
        #train_subset = train_subset.replace("[","")
        #train_subset = train_subset.replace("]","")
        print(fold)
        #print(train_subset)
        directory = "/home/rodrigo/datascience/projects/pri-matrixFac/tensorflow/tf_files/primatrix/" + fold
        if not os.path.exists(directory):
            os.makedirs(directory)
    #Loop the files inside directory and move to corresponding folders
    for filename in os.listdir("/home/rodrigo/datascience/projects/pri-matrixFac/micro"):#train_subset:        
        if  str(filename) in str(train_subset):
            string = str("/home/rodrigo/datascience/projects/pri-matrixFac/micro/" + str(filename))
            string = string.replace("'","")
            string = string.replace("[","")
            string = string.replace("]","")
            #print(string)
            #shutil.copy(string, directory)
            filebase = directory + "/" + filename
            filebase = filebase.replace(".mp4","_%05d.png")
            #print(string)
            #print(filebase)
            cmd = 'ffmpeg -i ' + string + ' -r 0.25 ' +  filebase+ ''
            #print(cmd)
            sp.call(cmd,shell=True)
            print(filename)
            


logging.info("End - Preparing data for training")  
