import sys
import BuildNewJar
import RunServer
import AutoRUN
import runshell


def cli(u_input=0):
    raw_tip = "========================================"
    if not u_input:
        print("===============功能列表==================")
        print("(1) 启动服务器           (2) 自动编译最新的spigot核心")
        print("(3) 修改启动参数         (4) 一键创建服务器")
        #print("(5) 返回控制台           (6) 强制关闭服务器")
        print("(0) 取消")
        print("===============使用方法==================")
        print("如果您首次运行且没有服务端,请先使用(2)编译核心,然后使用(4)创建服务器")
        print("如果您拥有服务端,请把服务端文件夹重命名为server并放到程序运行目录,并使用(1)启动服务器")
        print(raw_tip)
        try:
            u_input = input("请输入命令编号：")
            if sys.version_info[0] == 3: u_input = int(u_input)
        except:
            u_input = 0

    nums = [1, 2, 3, 4, ]#5, 6]
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
        print("编译完成,请使用(4)创建服务器")
        cli()
    elif u_input == 3:
        RunServer.get_new_config()
        print("修改完成")
        cli()
    elif u_input == 4:
        AutoRUN.autorun()
        RunServer.start_server()
    #elif u_input == 5:
    #    runshell.run_shell("screen -r mcserver")
    #elif u_input == 6:
    #    runshell.run_shell("screen -S mcserver -X quit")



cli()
