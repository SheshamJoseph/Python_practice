import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

# set window size
Window.size = (450, 600)


Builder.load_file("calc.kv")

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def number_pressed(self, number):
        # assign the value in the input field to a variable
        prior = self.ids.calc_input.text
        # if value is a zero
        if prior == "0":
            self.ids.calc_input.text = ""
            prior = self.ids.calc_input.text
        self.ids.calc_input.text = "".join([prior, f"{number}"])
    
    def add(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}+"

    def subtract(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}-"

    def divide(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}/"

    def multiply(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}*"
        

class CalculatorApp(App):
    def build(self):
        return MyLayout()
    

if __name__ == "__main__":
    CalculatorApp().run()