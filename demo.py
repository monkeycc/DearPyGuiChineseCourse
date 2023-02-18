import dearpygui.dearpygui as dpg
import os

# 获取当前目录 调用ttf
directory_path = os.path.dirname(os.path.abspath(__file__))


#  创建上下文   *必须
dpg.create_context()

#  创建窗口     *必须
dpg.create_viewport(title='This title', width=200, height=200)

#  安装程序     *必须
dpg.setup_dearpygui()


# 设置字体，必须加上，中文才会显示正常
with dpg.font_registry():
    with dpg.font( directory_path + "/MiSans-Medium.ttf", 20) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
dpg.bind_font(default_font) 

# 设置 单独窗口
with dpg.window(label="我是窗口", width=180, height=25,pos=(25,50)):
    dpg.add_text("Hello world 你好 世界")

# 显示窗口     *必须
dpg.show_viewport()

# 开始     *必须
dpg.start_dearpygui()

#  结束上下文   *必须
dpg.destroy_context()