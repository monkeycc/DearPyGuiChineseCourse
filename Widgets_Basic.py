import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

def _hsv_to_rgb(h, s, v):
    if s == 0.0: return (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = v*(1.-s), v*(1.-s*f), v*(1.-s*(1.-f)); i%=6
    if i == 0: return (255*v, 255*t, 255*p)
    if i == 1: return (255*q, 255*v, 255*p)
    if i == 2: return (255*p, 255*v, 255*t)
    if i == 3: return (255*p, 255*q, 255*v)
    if i == 4: return (255*t, 255*p, 255*v)
    if i == 5: return (255*v, 255*p, 255*q)

def helloprint():
    print("Hello")



dpg.create_context()

dpg.create_viewport(title='Custom Title', width=1000, height=1000)

with dpg.window(label="Example Window", width=1000, height=1000):

    with dpg.tree_node(label="Basic",default_open=True):

        with dpg.group(horizontal=True):
            dpg.add_button(label="Button", callback=helloprint)
            dpg.add_button(label="Button", callback=helloprint, small=True)
            dpg.add_button(label="Button", callback=helloprint, arrow=True) # default direction is mvDir_Up
            dpg.add_button(label="Button", callback=helloprint, arrow=True, direction=dpg.mvDir_Left)
            dpg.add_button(label="Button", callback=helloprint, arrow=True, direction=dpg.mvDir_Right)
            dpg.add_button(label="Button", callback=helloprint, arrow=True, direction=dpg.mvDir_Down)

        dpg.add_checkbox(label="checkbox", callback=helloprint)
        dpg.add_radio_button(("radio a", "radio b", "radio c"), callback=helloprint, horizontal=True)
        dpg.add_selectable(label="selectable", callback=helloprint)

        with dpg.group(horizontal=True):

            for i in range(7):

                with dpg.theme(tag="__demo_theme"+str(i)):
                    with dpg.theme_component(dpg.mvButton):
                        dpg.add_theme_color(dpg.mvThemeCol_Button, _hsv_to_rgb(i/7.0, 0.6, 0.6))
                        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, _hsv_to_rgb(i/7.0, 0.8, 0.8))
                        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, _hsv_to_rgb(i/7.0, 0.7, 0.7))
                        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, i*5)
                        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, i*3, i*3)

                dpg.add_button(label="Click", callback=helloprint)
                dpg.bind_item_theme(dpg.last_item(), "__demo_theme"+str(i))

        with dpg.group(horizontal=True):

            dpg.add_text("Press a button: ")
            widget = dpg.add_text("0")
            dpg.add_button(arrow=True, direction=dpg.mvDir_Left, user_data=widget, callback=lambda s, a, u: dpg.set_value(u, int(dpg.get_value(u))-1))
            dpg.add_button(arrow=True, direction=dpg.mvDir_Right, user_data=widget, callback=lambda s, a, u: dpg.set_value(u, int(dpg.get_value(u))+1))

        dpg.add_text("hover me")
        with dpg.tooltip(dpg.last_item()):
            dpg.add_text("I'm a simple tooltip!")

        dpg.add_separator()

        dpg.add_text("Value", label="Label", show_label=True)
        dpg.add_combo(("AAAA", "BBBB", "CCCC", "DDDD", "EEEE", "FFFF", "GGGG", "HHHH", "IIII", "JJJJ", "KKKK"), label="combo", default_value="AAAA", callback=helloprint)
        dpg.add_input_text(label="input text", default_value="Hello, world!", callback=helloprint)
      
        dpg.add_input_text(label="input text (w/ hint)", hint="enter text here", callback=helloprint)
        dpg.add_input_int(label="input int", callback=helloprint)
        dpg.add_input_float(label="input float", callback=helloprint, format="%.06f")
        dpg.add_input_float(label="input float scientific", format="%e", callback=helloprint)
        dpg.add_input_floatx(label="input floatx", callback=helloprint, default_value=[1,2,3,4])
        dpg.add_input_double(label="input double", callback=helloprint, format="%.14f")
        dpg.add_input_doublex(label="input doublex", callback=helloprint, default_value=[1,2,3,4], format="%.14f")
        dpg.add_drag_int(label="drag int", callback=helloprint)
        
        dpg.add_drag_int(label="drag int 0..100", format="%d%%", callback=helloprint)
        dpg.add_drag_float(label="drag float", callback=helloprint)
        dpg.add_drag_float(label="drag small float", default_value=0.0067, format="%.06f ns", callback=helloprint)
        dpg.add_slider_int(label="slider int", max_value=3, callback=helloprint)
        dpg.add_slider_float(label="slider float", max_value=1.0, format="ratio = %.3f", callback=helloprint)
        dpg.add_slider_double(label="slider double", max_value=1.0, format="ratio = %.14f", callback=helloprint)
        dpg.add_slider_int(label="slider angle", min_value=-360, max_value=360, format="%d deg", callback=helloprint)
       
        dpg.add_color_edit((102, 179, 0, 128), label="color edit 4", callback=helloprint)
        dpg.add_color_edit(default_value=(.5, 1, .25, .1), label="color edit 4", callback=helloprint)
        dpg.add_listbox(("Apple", "Banana", "Cherry", "Kiwi", "Mango", "Orange", "Pineapple", "Strawberry", "Watermelon"), label="listbox", num_items=4, callback=helloprint)
        dpg.add_color_button()

dpg.setup_dearpygui()

dpg.show_viewport()


dpg.start_dearpygui()



dpg.destroy_context()