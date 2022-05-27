import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

def _config(sender, keyword, user_data):

    widget_type = dpg.get_item_type(sender)
    items = user_data

    if widget_type == "mvAppItemType::mvRadioButton":
        value = True

    else:
        keyword = dpg.get_item_label(sender)
        value = dpg.get_value(sender)

    if isinstance(user_data, list):
        for item in items:
            dpg.configure_item(item, **{keyword: value})
    else:
        dpg.configure_item(items, **{keyword: value})


dpg.create_context()

dpg.create_viewport(title='Custom Title', width=500, height=500)


with dpg.window(label="Example Window", width=500, height=500):
        
                items = ("A","B","C","D","E","F","G","H","I","J","K","L","M" "O","P","Q","R","S","T","U","V","W","X","Y","Z")
                listbox_1 = dpg.add_listbox(items, label="listbox 1 (full)")
                listbox_2 = dpg.add_listbox(items, label="listbox 2", width=200)
                dpg.add_input_int(label="num_items",callback=_config, user_data=[listbox_1, listbox_2], before = listbox_1)
                dpg.add_slider_int(label="width", default_value=200, callback=_config, user_data=listbox_2, before = listbox_1, max_value=500)
        


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()