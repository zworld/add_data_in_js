#get new_data
import sys,os
from fnmatch import fnmatchcase
import shutil

def copyFiles(sourceDir,targetDir):
    for parent,dirnames,filenames in os.walk(sourceDir):
        for filename in filenames:
            sourceFile=os.path.join(sourceDir,filename)
            targetFile=os.path.join(targetDir,filename)
            shutil.copy(sourceFile,targetFile)
            

def GetAllScripts(rootdir, include = ["*.js"]):
    scripts = []
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            if any(fnmatchcase(filename, i) for i in include):
                scripts.append(os.path.join(parent,filename))
    return scripts
    
rootdir = os.path.join(sys.path[0], 'C:\\Users\\xinzhi_zhong\\Desktop\\test2')
rootdir = os.path.join(sys.path[0], 'C:\\Users\\xinzhi_zhong\\Desktop\\test2')
copyFiles("C:\\Users\\xinzhi_zhong\\Desktop\\test1","C:\\Users\\xinzhi_zhong\\Desktop\\test2")
scripts = GetAllScripts(rootdir) 
print scripts
for i in scripts:
   f_add=open(i)
   new_data=f_add.read()
   print new_data
   f_data=open('C:\\Users\\xinzhi_zhong\\Desktop\\data.js','a')
   f_data.write('\n' + new_data)
   f_data.close
   os.remove(i)
 
    


