# 与用户交互并保存参数到config.json
import json
import subprocess
import os


def get_stored_config():
    """读取config.json并返回config[字符串]"""
    filename = 'config.json'
    try:
        with open(filename) as f:
            config = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return config


def get_new_config():
    """记录储存用户配置到config.json"""
    global textmin, textmax
    maxmemory = input("请输入您需要的最大内存M:")
    minmemory = input("请输入您需要的最小内存M:")
    jar = input("请输入您的核心名:")
    try:
        textmax = int(maxmemory)
        textmin = int(minmemory)
    except ValueError:
        print("输入值不能为空")
    except UnboundLocalError:
        print("输入值不能为空")

    try:
        if textmax <= 0 or textmin <= 0 or not jar.endswith('.jar'):
            print("内存不可以为0,内存最小值不能大于内存最大值,且核心名必须为.jar")
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


def start_server():
    """启动服务器进程"""
    try:
        config = get_stored_config()
        dict_config = eval(config)
        max_size = dict_config["maxsize"]
        min_size = dict_config["minsize"]
        jar = dict_config["jar"]
        xmx = int(max_size)
        xms = int(min_size)
        os.mkdir("server")
        os.chdir("server")
        subprocess.run(f'java -Xmx{xmx}M -Xms{xms}M -jar {jar}')
    except TypeError:
        pass
    except FileExistsError:
        config = get_stored_config()
        dict_config = eval(config)
        max_size = dict_config["maxsize"]
        min_size = dict_config["minsize"]
        jar = dict_config["jar"]
        xmx = int(max_size)
        xms = int(min_size)
        os.chdir("server")
        subprocess.run(f'java -Xmx{xmx}M -Xms{xms}M -jar {jar}')
def regandlogin():
    """获取config.json返回值，如存在则运行，如不存在则创建配置并运行"""
    config = get_stored_config()
    if config:
        start_server()
    else:
        get_new_config()
        start_server()
