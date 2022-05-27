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

dpg.create_viewport(title='Custom Title', width=500, height=200)


with dpg.window(label="Example Window", width=500, height=200):
        

            # with dpg.tree_node(label="Selectables"):
                
                with dpg.tree_node(label="Basic",default_open = True):
                    dpg.add_selectable(label="1. I am selectable")
                    dpg.add_text("2. I am not selectable")

                with dpg.tree_node(label="Selection State: Single",default_open = True):

                    def _selection(sender, app_data, user_data):
                        for item in user_data:
                            if item != sender:
                               dpg.set_value(item, False)
                    items = (
                        dpg.add_selectable(label="1. I am selectable"),
                        dpg.add_selectable(label="2. I am selectable"),
                        dpg.add_selectable(label="3. I am selectable"),
                        dpg.add_selectable(label="4. I am selectable"),
                        dpg.add_selectable(label="5. I am selectable"),
                        )

                    for item in items:
                        dpg.configure_item(item, callback=_selection, user_data=items)

        


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()