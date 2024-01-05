import os
import zipfile
import shutil
from config import *
import sys

def doDecompile(javaPath, jarPath):
    print(os.popen(
        f"{javaPath} -cp java-decompiler.jar org.jetbrains.java.decompiler.main.decompiler.ConsoleDecompiler -dgs=true ./src/{jarPath} ./target/").read())
    print("反编译完成")

def doUnzip(jarName):
    zipfile.ZipFile(f"./target/{jarName}").extractall(f"./target/{jarName[:-4]}")
    print("jar包解压完成")

def makeIdeaProject(jarName):
    try:
        shutil.copytree(f"./target/{jarName[0:-4]}/BOOT-INF/classes", f"./project/{jarName[:-4]}/src/main/java")
        shutil.copytree(f"./target/{jarName[0:-4]}/BOOT-INF/lib", f"./project/{jarName[:-4]}/lib")
        if(copyConfig):
            shutil.copytree(f"./IdeaTemplate/jar/.idea", f"./project/{jarName[:-4]}/.idea")
            shutil.move(f"./project/{jarName[:-4]}/.idea/artifacts/NEWAWDJAR.xml", f"./project/{jarName[:-4]}/.idea/artifacts/{jarName[:-4]}.xml")
            with open(f"./project/{jarName[:-4]}/.idea/artifacts/{jarName[:-4]}.xml", "r") as f:
                content=f.read()
                content=content.replace("NEWAWDJAR", jarName[:-4])
            with open(f"./project/{jarName[:-4]}/.idea/artifacts/{jarName[:-4]}.xml", "w") as f:
                f.write(content)
    except:
        shutil.copytree(f"./target/{jarName[0:-4]}/WEB-INF/classes", f"./project/{jarName[:-4]}/src/main/java")
        shutil.copytree(f"./target/{jarName[0:-4]}/WEB-INF/lib", f"./project/{jarName[:-4]}/lib")
        if(copyConfig):
            shutil.copytree(f"./IdeaTemplate/war/.idea", f"./project/{jarName[:-4]}/.idea")
            shutil.move(f"./project/{jarName[:-4]}/.idea/artifacts/NEWAWDWAR.xml", f"./project/{jarName[:-4]}/.idea/artifacts/{jarName[:-4]}.xml")
            with open(f"./project/{jarName[:-4]}/.idea/artifacts/{jarName[:-4]}.xml", "r") as f:
                content=f.read()
                content=content.replace("NEWAWDWAR", jarName[:-4])
                content=content.replace("app_副本", jarName[:-4])
            with open(f"./project/{jarName[:-4]}/.idea/artifacts/{jarName[:-4]}.xml", "w") as f:
                f.write(content)
    shutil.copytree(f"./target/{jarName[0:-4]}/META-INF", f"./project/{jarName[:-4]}/META-INF")

    print("idea项目创建完成")

def cleanDir(directory:str):
    try:
        # 获取目录中的所有文件
        file_list = os.listdir(directory)
        for file_name in file_list:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):  # 只删除文件，而不是目录
                print(f"删除文件: {file_path}")
                os.remove(file_path)  # 删除文件
        print("目录下的所有文件已删除")
    except OSError as e:
        print(f"删除文件时出错：{e}")


def parseCommand():
    pass

if __name__=="__main__":
    # clean target and project
    cleanDir('./target')
    cleanDir('./project')

    doDecompile(javaPath, jarPath)
    doUnzip(os.path.basename(jarPath))
    makeIdeaProject(os.path.basename(jarPath))
