import kivy
from kivy.app import App
from kivy.uix.widget import Widget
# to use the IDs from my.kv
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# first way
# Builder.load_file("my.kv")
# Builder.load_file("box.kv")
# Builder.load_file("inherit.kv")
# Builder.load_file("float_layout.kv")
# Builder.load_file("update_label.kv")
# Builder.load_file("round_btn.kv")
Builder.load_file("switch.kv")



# 2nd way
# Builder.load_string("""
# <MyLayout>

#     name:name
#     food:food
#     color:color

#     GridLayout:
#         cols:1
#         size:root.width, root.height

#         GridLayout:
#             cols:2

#             Label:
#                 text: "Name : "
#             TextInput:
#                 id:name
#                 multiline:False

#             Label:
#                 text: "Favorite Food : "
#             TextInput:
#                 id: food
#                 multiline:False

#             Label:
#                 text: "Favorite Color : "
#             TextInput:
#                 id:color
#                 multiline:False

#         Button:
#             text: "Submit"
#             font_size: 32
#             on_press:root.press()

# """)

class MyLayout(Widget):
    # initialize infinite keywords
    # name = ObjectProperty(None)
    # food = ObjectProperty(None)
    # color = ObjectProperty(None)

    def update_label(self):
        # create variables for the widget
        name = self.ids.name_input.text
        print(name)

        # to update label
        self.ids.name_label.text = f"Hello {name}!"
        self.ids.name_input = ""


    def press(self):
        name = self.name.text
        food = self.food.text
        color = self.color.text
        print(f"Hello {name}, your favourite food is {food},and your favorite color is {color}")
        # self.add_widget(Label(text=f"Hello {name}, your favourite food is {food},and your favorite color is {color}"))
        # to clear the input boxes
        self.name.text = ""
        self.food.text = ""
        self.color.text = ""

    def clear(self):
        self.name.text = ""
        self.food.text = ""
        self.color.text = ""

    def switch_click(self, switch_obj, switch_val):
        # print(switch_val)
        if switch_val:
            self.ids.my_label.text = "Switch is on"
        else:
            self.ids.my_label.text = "Switch is off"
        

class ThisApp(App):

    def build(self):
        # return Label(text="Hello world")
        return MyLayout()
    
if __name__ == "__main__":
    ThisApp().run()