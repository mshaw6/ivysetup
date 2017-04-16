#This module download the SBT
import wget
import tarfile
import os

def downloadSBT():
    url = 'https://dl.bintray.com/sbt/native-packages/sbt/0.13.13/sbt-0.13.13.tgz'
    try:
        print("Downloading SBT")
        wget.download(url, bar=wget.bar_thermometer)
        print "File Download Complete"
    except:
        print "Unable to download SBT"

def unzipSBT():
    print "Unzipping tar file"
    tar=tarfile.open("sbt-0.13.13.tgz","r:gz")
    tar.extractall()
    tar.close()

def cleanupSBT():
    os.remove("sbt-0.13.13.tgz")
    os.rename("sbt-launcher-packaging-0.13.13", "sbt")