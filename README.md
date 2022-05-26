<h4 align="center">DearPyGui 中文教程</h4>

<h1></h1>

<BR>![Themes](https://raw.githubusercontent.com/hoffstadt/DearPyGui/assets/linuxthemes.PNG) 
  
## 特征  
-**现代外观**-完整的主题和风格控制

-**出色的性能**-基于GPU的渲染和高效的C/C++代码

-**稳定运行**-异步功能支持

-**快速图形**-以60 fps的速度显示超过100万个数据点，可进行缩放和平移

-**节点编辑器**-直观的用户交互

-**内置演示**-快速了解所有功能

-**开发人员工具**-主题和资源检查、运行时指标、调试器

-**跨平台**-Windows、Linux、MacOS

-**MIT license**

<h1></h1>
  
  ## 安装

最低要求 Python 3.7 64bit.
 ```
 pip install dearpygui
 or
 pip3 install dearpygui
 ```
  
  
  ## 简单的示例
 
这里创建一个简单的示例
  
<img width="177" alt="1" src="https://user-images.githubusercontent.com/6490927/168543045-9bb21a56-e6ff-427a-972d-d864a7de1eb8.png">

  
```Python
import dearpygui.dearpygui as dpg

#  创建上下文   *必须
dpg.create_context()

#  创建窗口     *必须
dpg.create_viewport(title='This title', width=200, height=200)

#  安装程序     *必须
dpg.setup_dearpygui()


# 设置字体，必须加上，中文才会显示正常
with dpg.font_registry():
    with dpg.font("./MiSans-Medium.ttf", 20) as default_font:
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
```
<br/>
 
  ## QQ 交流群
 
水平有限，时间有限，共同交流，共同踩坑
  
QQ 交流群
582410579

<img width="165" alt="微信截图_20220516154643" src="https://user-images.githubusercontent.com/6490927/168543996-90591289-d93b-4f0f-8986-f6e8190b6de1.png">
  
  
  ## Widgets_Basic.py
  
<img width="660" alt="微信截图_20220526220704" src="https://user-images.githubusercontent.com/6490927/170504266-b06566a6-458b-4421-99a3-963ff1bf958c.png">

