# 与用户交互并保存参数到config.json
import json
import os
import runshell
import newpassword


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
            rconpass = newpassword.password()
            rconport = newpassword.port()
            print(f"您设置的最大内存为{maxmemory}")
            print(f"您设置的最小内存为{minmemory}")
            print("您的Rcon配置为")
            print(f"密码 {rconpass}")
            print(f"端口 {rconport}")
            print("请妥善保管该数据，不要泄露您的密码与端口")
            config = {"maxsize": f"{maxmemory}", "minsize": f"{minmemory}", "jar": f"{jar}", "rconpass": f"{rconpass}",
                      "rconport": f"{rconport}"}
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
        runshell.run_shell(f"nohup java -Xmx{xmx}M -Xms{xms}M -jar {jar} nogui >/dev/null 2>&1 &")
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
        runshell.run_shell(f"nohup java -Xmx{xmx}M -Xms{xms}M -jar {jar} nogui >/dev/null 2>&1 &")


def regandlogin():
    """获取config.json返回值，如存在则运行，如不存在则创建配置并运行"""
    config = get_stored_config()
    if config:
        config = get_stored_config()
        dict_config = eval(config)
        rconpass = dict_config["rconpass"]
        rconport = dict_config["rconport"]
        print("您的Rcon配置为")
        print(f"密码 {rconpass}")
        print(f"端口 {rconport}")
        print("请使用Rcon客户端控制服务器")
        print("例如rcon.iecraft.com")
        start_server()
    else:
        get_new_config()
        rcon()
        start_server()


def rcon():
    """创建server.properties与eula，并使用config.json配置rcon"""
    config = get_stored_config()
    dict_config = eval(config)
    rconpass = dict_config["rconpass"]
    rconport = dict_config["rconport"]
    sp = "server/server.properties"
    with open(sp, 'w') as f:
        f.write("max-players=20\n")
        f.write("network-compression-threshold=256\n")
        f.write("resource-pack-sha1=\n")
        f.write("max-world-size=29999984\n")
        f.write("function-permission-level=2\n")
        f.write(f"rcon.port={rconport}\n")
        f.write("server-port=25565\n")
        f.write("debug=false\n")
        f.write("server-ip=\n")
        f.write("spawn-npcs=true\n")
        f.write("allow-flight=false\n")
        f.write("level-name=world\n")
        f.write("view-distance=10\n")
        f.write("resource-pack=\n")
        f.write("spawn-animals=true\n")
        f.write("white-list=false\n")
        f.write(f"rcon.password={rconpass}\n")
        f.write("generate-structures=true\n")
        f.write("max-build-height=256\n")
        f.write("online-mode=false\n")
        f.write("level-seed=\n")
        f.write("use-native-transport=true\n")
        f.write("prevent-proxy-connections=false\n")
        f.write("enable-jmx-monitoring=false\n")
        f.write("enable-rcon=true\n")
        f.write("rate-limit=0\n")
        f.write("motd=runonhutu\n")
    eula = "server/eula.txt"
    with open(eula, 'w') as e:
        e.write("eula=true")
