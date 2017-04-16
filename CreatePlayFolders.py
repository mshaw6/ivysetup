#This module creates directory Structure
import os
base_dir="/data/jenkins/sbt_installs/"
def directoryStatus(dir_name):
    try:
        os.path.dirname(base_dir+dir_name)
        os.listdir(base_dir+dir_name)
        print "Directory Already Exists " + dir_name
    except:
        print "Creating New Directory :" + dir_name
        os.mkdir(base_dir+dir_name)
def createPlayDirectory(dir_name,app_dir):
    try:
        dir_cwd = os.getcwd()
        print "Present Working Directory :" + dir_cwd
        os.chdir(base_dir+dir_name)
        print "Creating Application Directory :" + app_dir
        os.mkdir(app_dir)
        os.chdir(app_dir)
    except:
        print "Some Error Occured"
