import sys
import BuildNewJar
import RunServer
import AutoRUN


def cli(u_input=0):
    raw_tip = "==============================================="
    if not u_input:
        print("===============功能列表==================")
        print("(1) 启动服务器           (2) 自动编译最新的spigot核心")
        print("(3) 修改启动参数         (4) 一键创建服务器")
        print("(0) 取消")
        print(raw_tip)
        try:
            u_input = input("请输入命令编号：")
            if sys.version_info[0] == 3: u_input = int(u_input)
        except:
            u_input = 0

    nums = [1, 2, 3, 4]
    if not u_input in nums:
        print(raw_tip)
        print("已取消!")
        exit()

    print(raw_tip)
    print("正在执行(%s)..." % u_input)
    print(raw_tip)

    if u_input == 1:
        RunServer.regandlogin()
    elif u_input == 2:
        BuildNewJar.build_minecraft()
        print("编译完成,请在程序运行目录中的Build文件夹中找到核心文件")
    elif u_input == 3:
        RunServer.get_new_config()
        print("修改完成")
        cli()
    elif u_input == 4:
        AutoRUN.autorun()
        RunServer.start_server()


cli()
