import subprocess
import sys

def run_shell(shell):
    """运行命令实时输出"""
    cmd = subprocess.Popen(shell, stdin=subprocess.PIPE, stderr=sys.stderr, close_fds=True, stdout = sys.stdout, universal_newlines=True, shell=True, bufsize=1)
    cmd.communicate()
    return cmd.returncode