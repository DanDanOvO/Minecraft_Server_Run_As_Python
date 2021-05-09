# 使用build_minecraft()编译核心，并复制编译好的核心到server文件夹 与用户交互储存内存参数
import json
import BuildNewJar
import os
import shutil


def autorun():
    BuildNewJar.build_minecraft()
    try:
        os.mkdir("server")
        src_dir_path = 'Build'  # 源文件夹
        to_dir_path = 'server'  # 存放复制文件的文件夹
        key = 'spigot'  # 源文件夹中的文件包含字符key则复制到to_dir_path文件夹中
        if not os.path.exists(to_dir_path):
            os.mkdir(to_dir_path, 1)
        if os.path.exists(src_dir_path):
            for file in os.listdir(src_dir_path):
                # is file
                if os.path.isfile(src_dir_path + '/' + file):
                    if key in file:
                        jar = file
                        shutil.copy(src_dir_path + '/' + file, to_dir_path + '/' + file)
        maxmemory = input("请输入您需要的最大内存M:")
        minmemory = input("请输入您需要的最小内存M:")
        try:
            textmax = int(maxmemory)
            textmin = int(minmemory)
        except ValueError:
            print("输入值不能为空")
        except UnboundLocalError:
            print("输入值不能为空")
        try:
            if textmax <= 0 or textmin <= 0:
                print("内存不可以为0")
            else:
                filename = 'config.json'
                config = {"maxsize": f"{maxmemory}", "minsize": f"{minmemory}", "jar": f"{jar}"}
                jsondata = json.dumps(config)
                with open(filename, 'w') as f:
                    json.dump(jsondata, f)
                    return config
        except UnboundLocalError:
            pass
        except TypeError:
            pass
    except FileExistsError:
        src_dir_path = 'Build'  # 源文件夹
        to_dir_path = 'server'  # 存放复制文件的文件夹
        key = 'spigot'  # 源文件夹中的文件包含字符key则复制到to_dir_path文件夹中
        if not os.path.exists(to_dir_path):
            os.mkdir(to_dir_path, 1)
        if os.path.exists(src_dir_path):
            for file in os.listdir(src_dir_path):
                # is file
                if os.path.isfile(src_dir_path + '/' + file):
                    if key in file:
                        jar = file
                        shutil.copy(src_dir_path + '/' + file, to_dir_path + '/' + file)
        maxmemory = input("请输入您需要的最大内存M:")
        minmemory = input("请输入您需要的最小内存M:")
        try:
            textmax = int(maxmemory)
            textmin = int(minmemory)
        except ValueError:
            print("输入值不能为空")
        except UnboundLocalError:
            print("输入值不能为空")
        try:
            if textmax <= 0 or textmin <= 0:
                print("内存不可以为0")
            else:
                filename = 'config.json'
                config = {"maxsize": f"{maxmemory}", "minsize": f"{minmemory}", "jar": f"{jar}"}
                jsondata = json.dumps(config)
                with open(filename, 'w') as f:
                    json.dump(jsondata, f)
                    return config
        except UnboundLocalError:
            pass
        except TypeError:
            pass
