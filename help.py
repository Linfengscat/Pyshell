HELP='Help on my handmake Python Shell[Pyshell]:\n' \
     '\n' \
     '---------------------------------------漂亮的分割线-----------------------------------------\n' \
     '\n' \
     '提示符格式：［Pyshell]+系统名＠用户名+用户权限：Working at 工作路径+pid（主进程ID）\n' \
     '\n' \
     '---------------------------------------漂亮的分割线-----------------------------------------\n' \
     '\n' \
     'Method Usage:\n' \
     '\n' \
     '--------------前端控制（这些必须在主进程（主函数）里执行，包括后面实现sub功能所用的管道）---------------\n' \
     '\n' \
     '      "Your cmd"& : \n' \
     '          后台运行这条指令，可以继续运行其他指令\n' \
     '      chdir path: (change directory)\n' \
     '          更改当前工作路径到path(path要合法，否则会提示不合法路径并忽略此条指令)\n' \
     '\n' \
     '--------------文件，目录控制(后面重定向有文件更多操作)-----------------------------------------－-\n' \
     '\n' \
     '      listdir:  (list derectory)\n' \
     '          以列表形式输出当前目录下所有文件（类似于linuxshell下的ls,输出形式是列表）\n' \
     '      makedir path: (make directory) \n' \
     '          当前工作目录下创建目录path\n' \
     '      makedirs path: (make multilevel directory )　\n' \
     '          于makedir类似，但可以创建多级目录\n' \
     '      rmdir path: (remove path)\n' \
     '          删除path这个目录（只能是目录）\n' \
     '      rmfile file: (remove file)\n' \
     '          删除file这个文件（只能是文件）\n' \
     '      getatime path/file:(get access time)\n' \
     '          输出文件（目录）的最后存取时间\n' \
     '      getctime path/file:(get create time)\n' \
     '          输出文件（目录）的创建时间\n' \
     '      getmtime path/file:(get modify time)\n' \
     '          输出文件（目录）的最后修改时间\n' \
     '      getsize path/file:(get size)\n' \
     '          输出文件（目录）的大小\n' \
     '\n' \
     '-------------命令替换操作------------------------------------------------------------------\n' \
     '\n' \
     '      sub cmdA as cmdB:\n' \
     '          临时的命令替换，A是你自定义命令，B为你要替换的命令（原命令不会失效），仅在本次运行中有效\n' \
     '      psub cmdA as cmdB: (permanent substitude)\n' \
     '          永久性的命令替换（退出本次程序后重新打开自定义依然有效）\n' \
     '          替换原则：临时＞永久：（临时和永久替换用了相同的关键字，则执行临时替换所对应的系统命令）\n' \
     '                  命令覆盖　：对同样的关键字进行多次替换，执行是会执行最后一次替换所对应指令\n' \
     '                  不验证所对应命令的有效性，但运行是会提示你自定义命令是无效的\n' \
     '\n' \
     '-------------重定向控制--------------------------------------------------------------------\n' \
     '\n' \
     '      redir cmd to file:(redirect the result of your command to file)\n' \
     '          将cmd指令的执行结果写入文件，而不是控制台（屏幕），会替换掉原文件内容\n' \
     '      redir cmd to file -a: (-a表示以追加的方式)\n' \
     '          执行结果追加到文件后面写入，而不影响文件原有内容\n' \
     '      redir from file:\n' \
     '          读取file里内容输出到控制台（屏显）\n' \
     '      redir from file -c: (-c表示当做命令来执行)\n' \
     '          读取file内容并将其当做系统命令执行（不可执行会提示命令无效）\n' \
     '      writeto file:\n' \
     '          提供一个文本输入流(以double＼n结束输入)，输出的内容会写到指定文件中（非追加\n' \
     '      writeto file -a: (-a表示追加的方式)\n' \
     '          写入结果追加到文件后面，而不影响文件原有内容\n' \
     '      文件存在性说明：redirto,writeto系列在文件不存在是会创建文件\n' \
     '                  redirfrom系列要求文件必须存在，不存在会提示＇文件不存在＇并忽略此条指令\n' \
     '\n' \
     '-------------管道控制----------------------------------------------------------------------\n' \
     '\n' \
     '      cmdA pipeto cmdB:\n' \
     '          cmdA的输出流（执行结果）直接当做cmdB的输入\n' \
     '          说明：这边实现的其实是一个伪管道，因为没有真正的缓冲机制，而且有些cmdB类的命令可能不能实现，\n' \
     '              　因为cmdB类命令必须是能本身够读取文件执行的命令格式\n' \
     '\n' \
     '------------------------------------------------------------------------------------------\n' \
     'Copyrigth@j142 10141346 linfeng\n' \
     '------------------------------------------------------------------------------------------'



DESCRIPTION='Author : 林锋  10141346   计142\n' \
            'Email : wobuxinnihuikan@163.com\n' \
            'Last Modify Time : 2017-6-20\n' \
            'Use "gethelp" to get help and"getout" to exit\n' \
            '----------------------------------------------------------------------------------------------'
