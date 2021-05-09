import requests
import os
import subprocess


def download_buildtools():
    """从spigot获取最新的BuildTools"""
    download_addres = 'https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar'
    f = requests.get(download_addres)
    try:
        os.mkdir("Build")
        os.chdir("Build")
        with open("BuildTools.jar", "wb") as code:
            code.write(f.content)
    except FileExistsError:
        os.chdir("Build")
        with open("BuildTools.jar", "wb") as code:
            code.write(f.content)


def build_jar():
    """编译核心"""
    subprocess.run('java  -Xmx1024M -jar BuildTools.jar')


def build_minecraft():
    """下载并编译"""
    download_buildtools()
    build_jar()
