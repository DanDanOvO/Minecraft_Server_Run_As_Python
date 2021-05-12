# 获取编译好的核心，并复制到server文件夹 与用户交互储存内存参数
import json
import os
import shutil
import newpassword


def autorun():
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
        except UnboundLocalError:
            print("UnboundLocalError")
        except TypeError:
            print("TypeError")
        else:
            if textmax <= 0 or textmin <= 0:
                print("内存不可以为0")
            else:
                filename = 'config.json'
                rconpass = newpassword.password()
                rconport = newpassword.port()
                print(f"您设置的最大内存为{maxmemory}")
                print(f"您设置的最小内存为{minmemory}")
                print("您的Rcon配置为")
                print(f"密码 {rconpass}")
                print(f"端口 {rconport}")
                print("请使用Rcon客户端控制服务器")
                print("例如rcon.iecraft.com")
                config = {"maxsize": f"{maxmemory}", "minsize": f"{minmemory}", "jar": f"{jar}",
                          "rconpass": f"{rconpass}",
                          "rconport": f"{rconport}"}
                jsondata = json.dumps(config)
                with open(filename, 'w') as f:
                    json.dump(jsondata, f)
                return config
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
        except UnboundLocalError:
            print("UnboundLocalError2")
        except TypeError:
            print("TypeError")
        else:
            if textmax <= 0 or textmin <= 0:
                print("内存不可以为0")
            else:
                filename = 'config.json'
                rconpass = newpassword.password()
                rconport = newpassword.port()
                print(f"您设置的最大内存为{maxmemory}")
                print(f"您设置的最小内存为{minmemory}")
                print("您的Rcon配置为")
                print(f"密码 {rconpass}")
                print(f"端口 {rconport}")
                print("请使用Rcon客户端控制服务器")
                print("例如rcon.iecraft.com")
                config = {"maxsize": f"{maxmemory}", "minsize": f"{minmemory}", "jar": f"{jar}",
                          "rconpass": f"{rconpass}",
                          "rconport": f"{rconport}"}
                jsondata = json.dumps(config)
                with open(filename, 'w') as f:
                    json.dump(jsondata, f)
                return config
