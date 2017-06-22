import sys
import os
import shlex
import re
import time
from complied_re import *
from init_command import *
from subprocess import *
import help

SHELL_STATUS_RUN = 1
SHELL_STATUS_STOP = 0
LOOP_EXIT = 0
KEYWORDhash={}

def shell_loop():
    os.chdir('/home/llinfeng')
    print(help.DESCRIPTION)
    #os.chdir("/home/llinfeng")
    status = SHELL_STATUS_RUN
    loopsta = LOOP_EXIT
    while status == SHELL_STATUS_RUN:
        #建立管道以实现sub功能
        rd,wt = os.pipe()
        u = os.popen('whoami').read()
        s = os.popen('uname').read()
        if u[:-1]=='llinfeng':
            r='#'
        else:
            r='$'
        sys.stdout.write('[Pyshell]'+s[:-1]+'@'+u[:-1]+r+':Working at '+os.getcwd()+' now pid:' +repr(os.getpid())+'>>>')
        sys.stdout.flush()
        cmd = sys.stdin.readline()
        if not cmd=='\n':
            if cmd[:-1] == 'getout':
                print('Thanks For Using~~~~')
                sys.exit(0)
                break
            elif isback.search(cmd):
                cmd=cmd[:-2]
                if chdir(cmd)==0:
                    status=bkrun(cmd,rd,wt)
            else:
                cmd=cmd[:-1]
                if chdir(cmd)==0:
                    status=ftrun(cmd,rd,wt)
        else:
            pass
        #管道读取
        os.close(wt)
        rd = os.fdopen(rd)
        dic=rd.read() #管道文件只能读取一次　取出来就没了　所以必须用dic来保存
        rd.close()
        if dic:
            KEYWORDhash[fdcmd.search(dic).group(1)]=fdcmd.search(dic).group(2)

def bkrun(cmd,rd,wt):
    try:
        splitcmd = split_cmd(cmd)
    except:
        print('Invalid command')
        return 1
    pid = os.fork()
    if pid == -1:
        print('创建子进程失败')
    if pid == 0:
        os.close(rd)
        print('\nchild process'+repr(os.getpid())+' is working backgroud...')
        #time.sleep(1)
        if execute(cmd,splitcmd,rd,wt)==1:
            print('invalid command in childproceess '+repr(os.getpid()))
        os._exit(0)
    elif pid > 0:
        return SHELL_STATUS_RUN

def ftrun(cmd,rd,wt):
    try:
        splitcmd = split_cmd(cmd)
    except:
        print('Invalid Command')
        return 1
    pid=os.fork()
    if pid==0:
        os.close(rd)
        print('childprocess'+repr(os.getpid())+' :Command executing...')
        #time.sleep(1)
        if execute(cmd,splitcmd,rd,wt)==1:
            print('Invalid Command')
        #print(os.getpid())
        os._exit(0)

    elif pid>0:
        while True:
            wpid,status=os.waitpid(pid,0)
            if os.WIFEXITED(status) or os.WIFSIGNALED(status): #os.WIFSIGNALED(status)  如果进程由于信号而退出，则返回True，否则返回False。
                                                               #os.WIFEXITED(status)  如果进程是以exit()方式退出的，则返回True，否则返回False。
                break
    return SHELL_STATUS_RUN

def execute(cmd,splitcmd,rd,wt):
    if proexecute(cmd,splitcmd,rd,wt)==1:
        return 0
    else:
        try:
            #os.system(cmd)
            os.execvp(splitcmd[0], splitcmd)
            return 0
        except:
            return 1

def proexecute(cmd,splitcmd,rd,wt):
    PERMKEYHASH=CreatePermkeyList()
    if gethelp(cmd)==1:
        return 1
    if listdir(cmd)==1:
        return 1
    if makedir(cmd)==1:
        return 1
    if makedirs(cmd)==1:
        return 1
    if rmdir(cmd):
        return 1
    if rmfile(cmd):
        return 1
    if getatime(cmd)==1:
        return 1
    if getctime(cmd)==1:
        return 1
    if getmtime(cmd)==1:
        return 1
    if getsize(cmd)==1:
        return 1
    if searchsub(cmd,KEYWORDhash)==1:
        return 1
    if searchpsub(cmd,PERMKEYHASH):
        return 1
    if psub(cmd)==1:
        return 1
    if sub(cmd)!=0:   #一定要通过管道实现　否则是传不了值滴
        try:
            wt = os.fdopen(wt,'w')
            dic=sub(cmd)
            for i in dic:
                string=i+'--'+dic[i]
            wt.write(string)
            print('命令替换成功')
        except:
            print('管道写入失败')
        return 1
    if redirto_a(cmd)==1:
        return 1
    if redirto(cmd)==1:
        return 1
    if redirfrom_c(cmd)==1:
        return 1
    if redirfrom(cmd)==1:
        return 1
    if writeto_a(cmd)==1:
        return 1
    if writeto(cmd)==1:
        return 1
    if pipe(cmd)==1:
        return 1
    else:
        return 0

def main():
  shell_loop()

if __name__ == "__main__":
    main()
