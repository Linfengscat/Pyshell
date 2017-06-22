import os
import time
import sys
import re
import shlex
from complied_re import *
import help

#========================================漂亮的分割线嘿嘿嘿====================================================
class RedirectStdout:  #  cStringIO
    def __init__(self):
        self.content = ''
        self.savedStdout = sys.stdout
        self.memObj, self.fileObj, self.nulObj = None, None, None

    def write(self, outStr):# 外部的print语句将执行本write()方法，并由当前sys.stdout输出 ????不存在的
        self.content += outStr

    def toCons(self):  # 标准输出重定向至控制台
        sys.stdout = self.savedStdout
    # def toMemo(self):  # 标准输出重定向至内存
    #     self.memObj = cStringIO.StringIO()
    #     sys.stdout = self.memObj

    def toFile(self, flag='a+',file='out.txt'):  # 标准输出重定向至文件
        self.fileObj = open(file, flag, 1)  # 改为行缓冲
        sys.stdout = self.fileObj

    def toMute(self):  # 抑制输出
        self.nulObj = open(os.devnull, 'w')
        sys.stdout = self.nulObj

    def restore(self):
        self.content = ''
        if self.memObj:
            self.memObj.close()
        if self.fileObj:
            self.fileObj.close()
        if self.nulObj:
            self.nulObj.close()
        sys.stdout = self.savedStdout
#===============================================漂亮的分割线嘿嘿嘿===============================================


def split_cmd(string):
    return shlex.split(string)

def gethelp(cmd):
    if isgethelp.search(cmd):
        print(help.HELP)
        return 1
    else:
        return 0

def chdir(cmd):
    if ischdir.search(cmd):
        try:
            os.chdir(ischdir.search(cmd).group(1))
        except:
            print('更改目录失败,找不到目录' + ischdir.search(cmd).group(1))
        finally:
            return 1
    else:
        return 0

def listdir(cmd):
    if islistdir.search(cmd):
        print('当前目录文件列表:'+repr(os.listdir()))
        return 1
    else:
        return 0

def makedir(cmd):
    if ismakedir.search(cmd):
        try:
            os.mkdir(ismakedir.search(cmd).group(1))
        except:
            print('创建目录失败')
        finally:
            return 1
    else:
        return 0

def makedirs(cmd):
    if ismakedirs.search(cmd):
        try:
            os.makedirs(ismakedirs.search(cmd).group(1))
        except:
            print('创建目录失败')
        finally:
            return 1
    else:
        return 0

def rmdir(cmd):
    if isrmdir.search(cmd):
        try:
            os.rmdir(isrmdir.search(cmd).group(1))
        except:
            print('目录都不存在，你还删除个啥子！')
        finally:
            return 1
    else:
        return 0

def rmfile(cmd):
    if isrmfile.search(cmd):
        try:
            os.remove(isrmfile.search(cmd).group(1))
        except:
            print('文件都不存在，你还删除个啥子！')
        finally:
            return 1
    else:
        return 0

def getatime(cmd):
    if isgetatime.search(cmd):
        try:
            s=os.path.getatime(isgetatime.search(cmd).group(1))
            timeArray = time.localtime(s)
            stdtime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            print(stdtime)
        except:
            print('读取存取时间失败（文件不存在）')
        finally:
            return 1
    else:
        return 0

def getmtime(cmd):
    if isgetmtime.search(cmd):
        try:
            s=os.path.getmtime(isgetmtime.search(cmd).group(1))
            timeArray = time.localtime(s)
            stdtime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            print(stdtime)
        except:
            print('读取修改时间失败（文件不存在）')
        finally:
            return 1
    else:
        return 0

def getctime(cmd):
    if isgetctime.search(cmd):
        try:
            s=os.path.getctime(isgetctime.search(cmd).group(1))
            timeArray = time.localtime(s)
            stdtime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            print(stdtime)
        except:
            print('读取创建时间失败（文件不存在）')
        finally:
            return 1
    else:
        return 0

def getsize(cmd):
    if isgetsize.search(cmd):
        try:
            s=os.path.getsize(isgetsize.search(cmd).group(1))
            print(s)
            # timeArray = time.localtime(s)
            # stdtime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            # print(stdtime)
        except:
            print('读取文件大小失败（文件不存在）')
        finally:
            return 1
    else:
        return 0

def psub(cmd):
    if ispsub.search(cmd):
        key,value=ispsub.search(cmd).group(1),ispsub.search(cmd).group(2)
        with open('/home/llinfeng/Documents/cmdlist.txt','a+') as f:
            f.write(key+'--'+value+'\n')
        print('永久替换成功')
        return 1
    else:
        return 0

def sub(cmd):
    if issub.search(cmd):
        KWhash={}
        KWhash[issub.search(cmd).group(1)] = issub.search(cmd).group(2)
        return KWhash
    else:
        return 0

def searchsub(cmd,KEYWORDhash):
    if cmd in KEYWORDhash.keys():
        splitcm=shlex.split(KEYWORDhash[cmd])
        try:
            os.execvp(splitcm[0],splitcm)
        except:
            print('Wrong define of your command')
        finally:
            return 1
    else:
        return 0

def CreatePermkeyList():
    PERMKEYHASH={}
    with open('/home/llinfeng/Documents/cmdlist.txt', 'r+') as f:
        for i in f.readlines():
            PERMKEYHASH[fdcmd.search(i).group(1)] = fdcmd.search(i).group(2)
    return PERMKEYHASH

def searchpsub(cmd,PERMKEYHASH):
    if cmd in PERMKEYHASH.keys():
        splitcm=shlex.split(PERMKEYHASH[cmd])
        try:
            os.execvp(splitcm[0],splitcm)
        except:
            print('Wrong define of your Permanent command')
        finally:
            return 1
    else:
        return 0

def redirto_a(cmd):
    if isredirto_a.search(cmd):
        try:
            std=RedirectStdout()
            sys.stdout=std
            std.toFile('a+',isredirto_a.search(cmd).group(2))
            s=os.popen(isredirto_a.search(cmd).group(1))
            print(s.read())
            std.restore()
        except:
            print('写入文件失败')
        finally:
            return 1
    else:
        return 0

def writeto_a(cmd):
    if iswriteto_a.search(cmd):
        try:
            print('Add your message to ' + iswriteto_a.search(cmd).group(1))
            std=RedirectStdout()
            sys.stdout=std
            std.toFile('a+',iswriteto_a.search(cmd).group(1))
            enter=''
            while True:
                l=input()
                if l==enter:
                    break
                if l=='\n':
                    enter=l
                print(l)
            std.restore()
            print('End Writing')
        except:
            print('写入失败')
        finally:
            return 1
    else:
        return 0

def writeto(cmd):
    if iswriteto.search(cmd):
        try:
            print('Put your message to ' + iswriteto.search(cmd).group(1))
            std=RedirectStdout()
            sys.stdout=std
            std.toFile('w+',iswriteto.search(cmd).group(1))
            enter=''
            while True:
                l=input()
                if l==enter:
                    break
                if l=='\n':
                    enter=l
                print(l)
            std.restore()
            print('End Writing')
        except:
            print('写入失败，文件不存在滴')
        finally:
            return 1
    else:
        return 0


def redirto(cmd):
    if isredirto.search(cmd):
        try:
            std=RedirectStdout()
            sys.stdout=std
            std.toFile('w+',isredirto.search(cmd).group(2))
            s=os.popen(isredirto.search(cmd).group(1))
            print(s.read())
            std.restore()
        except:
            print('写入文件失败')
        finally:
            return 1
    else:
        return 0

def redirfrom(cmd):
    if isredirfrom.search(cmd):
        if os.path.isfile(isredirfrom.search(cmd).group(1)):
            try:
                with open(isredirfrom.search(cmd).group(1),'r+') as f:
                    print(f.read())
            except:
                print('打开文件失败')
            finally:
                return 1
        else:
            print('文件是不存在滴')
            return 1
    else:
        return 0

def redirfrom_c(cmd):
    if isredirfrom_c.search(cmd):
        if os.path.isfile(isredirfrom_c.search(cmd).group(1)):
            with open(isredirfrom_c.search(cmd).group(1), 'r+') as f:
                s=f.read()
                try:
                    os.execvp(split_cmd(s[:-1])[0],split_cmd(s[:-1]))
                except:
                    print('文件内命令是无效滴')
        else:
            print('文件是不存在滴')
        return 1
    else:
        return 0


def pipe(cmd):
    if ispipe.search(cmd):
        s=os.popen(ispipe.search(cmd).group(1)).read()
        with open('/home/llinfeng/Documents/pipe.txt','w+') as f:
            f.write(s)
        c=ispipe.search(cmd).group(2)+' /home/llinfeng/Documents/pipe.txt'
        os.system(c)
        return 1
    else:
        return 0
