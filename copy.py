import os
import os.path
import shutil

def copyFiles(sourceDir,targetDir):
    for parent,dirnames,filenames in os.walk(sourceDir):
        for filename in filenames:
            sourceFile=os.path.join(sourceDir,filename)
            targetFile=os.path.join(targetDir,filename)
            shutil.copy(sourceFile,targetFile)
            