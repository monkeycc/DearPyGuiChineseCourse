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

dpg.create_viewport(title='Custom Title', width=400, height=400)


with dpg.window(label="Example Window", width=400, height=400):
        

            # with dpg.tree_node(label="Absolute Position Placement"):
                dpg.add_button(label="Set Button 2 Pos", callback=lambda: dpg.set_item_pos(B2, (200, 250)))
                dpg.add_button(label="Reset Button 2 Pos", callback=lambda: dpg.reset_pos(B2))
                dpg.add_button(label="Button 1", pos=[0,200], width=75, height=75)
                B2 = dpg.add_button(label="Button 2", width=75, height=75)
                dpg.add_button(label="Button 3")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()