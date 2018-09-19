#Script to run graphics on ubuntu 16.04 LTS
import os
import tarfile

f = open("commands.txt","r")
str = f.read()

tf = tarfile.open("libgraph-1.0.2.tar.gz")
tf.extractall()

os.system(str)