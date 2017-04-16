import CreatePlayFolders
import SbtInstall
import os
import SetIVYPath
dir_name=raw_input("Enter the directory to be created : ")
base_dir="/data/jenkins/sbt_installs/"
app_name = []
def readPlayApps():
    playapps = open('PlayApps','r')
    for appname in playapps:
        app_name.append(appname.rstrip())
    playapps.close()

def initializeApp():
    readPlayApps()
    for app_dir in app_name:
        CreatePlayFolders.directoryStatus(dir_name)
        CreatePlayFolders.createPlayDirectory(dir_name,app_dir)
        SbtInstall.downloadSBT()
        SbtInstall.unzipSBT()
        SbtInstall.cleanupSBT()
        SetIVYPath.setPath()
        os.chdir(base_dir+dir_name)
initializeApp()
