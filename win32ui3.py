import os
import win32con
import win32ui
# win32con与win32ui等模块从 "pip install pywin32" 下载

default_name = ''
# 默认输入文件名 (一般 "保存/另存为" 为文件名加后缀, "打开" 为空字符串)

file_type = '所有文件(*.*)|*.*|图片文件(*.png;*.jpg)|*.png;*.jpg|'
# 可选的文件类型 ("|"与下一个"|" 中间的 "*."+文件后缀 才是格式判别标准, 第一个"|"之前的所有字符串 (如 "(*.*)") 均为显示内容，无实际作用))

mode = True
# "False"为 "保存/另存为", "True"为 "打开"

API_flag = win32con.OFN_OVERWRITEPROMPT | win32con.OFN_FILEMUSTEXIST
dlg = win32ui.CreateFileDialog(mode, None, default_name, API_flag, file_type)

dlg.SetOFNTitle("选择您的文件")
# "SetOFNTitle()": 设置标题

dlg.SetOFNInitialDir(os.path.abspath('desktop'))
# "SetOFNInitialDir()": 设置默认路径(需绝对路径) ("os.path.abspath()" 获取绝对路径)

dlg.DoModal()
# "DoModal()": 开始运行对话框, 阻滞程序

filename = dlg.GetPathName()
# "GetPathName()": 获取文件路径

fileExt = dlg.GetFileExt()
# "GetFileExt()": 获取文件后缀名


if os.path.exists(filename):
    pass
elif not mode:  # 当模式为 "保存/另存为" 时有可能需要新建文件, 所以文件有可能不存在
    if os.path.split(filename)[0] == '':
        print('对话框被关闭')
    else:
        pass
else:
    print('对话框被关闭或文件路径错误')
# 当对话框被关掉时会返回 输入框里的字符串.

