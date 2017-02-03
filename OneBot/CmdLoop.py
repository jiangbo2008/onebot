#!/usr/bin/python3
# coding=UTF-8

from cmd import Cmd
import sys

class CmdLoop(Cmd): 
    """description of class"""
    def __init__(self):     #初始基础类方法
        Cmd.__init__(self)

    def help_hello(self):
        print("输入hello参数，将执行do_hello方法，输出参数值")

    def do_hello(self,line):
        print("do_hello:",line)

    def help_exit(self):    #以help_*开头的为帮助
        print("输入exit退出程序")

    def do_exit(self,line): #以do_*开头为命令
        print("Exit:",line)
        sys.exit()

    def do_shell(self,line):
        print("do_shell:", line)

        
if __name__ == "__main__":
    cmd = CmdLoop()
    cmd.cmdloop()
