# app.py - My DearPyGUI windowed app
import dearpygui.dearpygui as dpg

# Generate unique ids for all widgets we want to change in runtime
dpg.create_context()
dpg.create_viewport(title='Circle Calculator', width=600, height=300)

radius_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()

def callback():
    output = "Radius Value: " + str(dpg.get_value(radius_id))
    dpg.set_value(output_id, output)

with dpg.window(label="Circle Calculator"):
    dpg.add_text("Welcome to the Circle Calculator")
    dpg.add_input_int(label="Radius")
    dpg.add_button(label="Calculate", callback=callback)
    dpg.add_button(label="Clear")
    dpg.add_text("", tag=output_id)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()