#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
remove useless folders or files.

"""

__author__ = 'Zhu JunYong'

import sys
import os
import shutil

#遍历指定路径去寻找符合targets条件的文件或文件夹 
def loopPath(path, targets):
    files = os.listdir(path)
    #删除空目录
    if len(files) == 0:
        print("del empty dir:"+path)
        os.rmdir(path)
        return
    #遍历目录
    for f in files:
        fullFileName = path + f
        if f in targets:
            print("del:"+fullFileName)
            remove(fullFileName)
            continue
        if os.path.isdir(fullFileName):
            loopPath(fullFileName+'/', targets)             
            
#删除文件或文件夹
def remove(myfile):
    if os.path.isdir(myfile):
        shutil.rmtree(myfile)
    else:
        os.remove(myfile)

#程序入口,删除指定文件名的文件或目录
if __name__ == '__main__':
    #检查参数
    if len(sys.argv) < 3:
        print("usage: python3 cleaner.py path filename1 filename2 ...")
        print("path: the file path that you want to clean")
        print("filename1: the filename that you want to clean, eg. .svn, .setting, desktop.ini, .classpath, .project")
        print("filename2: same as filename1")
        sys.exit(0) 
    #给路径和检查列表赋值
    path = sys.argv[1]
    targets = sys.argv[2:]
    #检查路径是否合法
    if not path.endswith('/'):
        path = path + '/'
    if not os.path.isdir(path):
        print("the directory:"+path+" is not a path or does not exist")
        sys.exit(0)
    
    loopPath(path, targets)     


