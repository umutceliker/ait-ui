#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------
from ait_ui import app
from ait_ui.elements import Element, Elm, Text, Image, ImageViewer, Canvas, Row, Button, Slider, Radio, Label

class MyApp():
    def __init__(self):
        self.main = Element()
        with self.main:
            with Row(id="toolbar") as toolbar:
                toolbar.style("border", "1px solid black").style("width", "100%").style("height", "50px")
                Label(usefor= "pan-mode", value="Pan Mode:")
                Radio(id="pan-mode", name = "mouse-mode").on("change", self.on_mouse_mode)
                Label(usefor= "draw-mode", value="Draw Mode:")
                Radio(id="draw-mode", value = "Draw", name = "mouse-mode").on("change", self.on_mouse_mode)
                Label(usefor= "brush-size", value="Brush Size:")
                Slider(id="brush-size", min=1, max=100, value=10).on("change", lambda id, value: Elm("view1").brush_size(value))
            view1 = ImageViewer(id="view1", value='https://www.w3schools.com/w3css/img_lights.jpg').style("border", "1px solid black")
            view1.style("width", "100%").style("height", "800px")

    def on_mouse_mode(self, id, value):
        print(f"Mouse mode {id} changed to: " + str(value))
        Elm("view1").mouse_mode(id)

    def render(self):
        return self.main.render()

if __name__ == '__main__':
    app.run(ui = MyApp, debug=True)