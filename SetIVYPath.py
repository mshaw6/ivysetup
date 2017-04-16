#This moulde replaces the IVY path in sbtopts
import fnmatch
import os
IVY_PATH="-ivy"
SBT_PATH= "/sbt/conf"
def setPath():
    APP_PATH=os.getcwd()
    os.chdir(APP_PATH+SBT_PATH)
    sbt_file=open('sbtopts','a')
    sbt_file.write(IVY_PATH+" "+APP_PATH+"/.ivy2")
    sbt_file.close()