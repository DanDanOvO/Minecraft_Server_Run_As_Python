# **糊涂工具箱**
### 1.项目说明
##### 	本程序可以自动编译最新的spigot核心，轻松的创建服务器，即使您没有开过Minecraft服务器，又或者您没有Linux基础，苦于没有一个简单的方法来维护服务器
#####   v0.5之后的版本统一使用Rcon进行服务器管理，支持任意Rcon客户端
### 2.主要功能
- 开启服务器
- 自动编译spigot核心
- 一键创建服务器
- 强制结束服务器进程
- Rcon控制台(下个版本更新)
- Web Rcon控制台(预计更新)
- 实时后台监控(下个版本更新)
### 2.安装运行
#### 必须的：
- Java11
- Git
#### 可选的：
- ~~screen~~(已经不需要)
- wget
- htop
#####	(1)运行前提条件
- Windows需要自行安装并配置好Git环境变量

#####	(2)项目安装步骤
##### Debian系：
- 更新软件源列表
- `apt update`
- 获取并安装该程序 
- `apt install -y default-jdk git htop wget & wget https://hututu.teriri.cc/hutu & chmod 777 hutu & ln -s -f /root/hutu /usr/bin/ht`
##### Redhat系：
- 更新软件源列表
- `yum update`
- 获取并安装改成该程序 
- `yum install -y default-jdk git htop wget & wget https://hututu.teriri.cc/hutu & chmod 777 hutu & ln -s -f /root/hutu /usr/bin/ht`
##### Windows：
- 预计下个版本更新
### 3.操作说明
##### Linux：
- 直接输入`ht`运行
##### Windows：
- 可以直接双击运行
- 但更推荐使用cmd运行
