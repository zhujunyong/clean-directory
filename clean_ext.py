#!/usr/bin/python3
# -*- coding:utf8 -*-

import sys
import os

#遍历指定路径去寻找符合targets条件的文件 
def loopPath(path, targets):
    files = os.listdir(path)
    for f in files:
        fullFileName = path + f
        if os.path.splitext(f)[1] in targets:
            print("del:"+fullFileName)
            remove(fullFileName)
            continue
        if os.path.isdir(fullFileName):
            loopPath(fullFileName+'/', targets)             
            
#删除文件或文件夹
def remove(myfile):
    if os.path.isdir(myfile):
        return
    else:
        os.remove(myfile)

#程序入口,删除指定扩展名的文件
if __name__ == '__main__':
    #检查参数
    if len(sys.argv) < 3:
        print("usage: python3 cleaner.py path ext1 ext2 ...")
        print("path: the file path that you want to clean")
        print("ext1: the file extension name that you want to clean, eg. .class, .jar")
        print("ext2: same as ext1")
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


