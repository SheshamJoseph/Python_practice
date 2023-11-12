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
    
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}{sign}"
        
    def equals(self):
        prior = self.ids.calc_input.text
        """if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            for number in num_list:
                answer += float(number)
            
            self.ids.calc_input.text = str(answer)"""
        try:
            answer = eval(prior)
        except:
            self.ids.calc_input.text = "Math Error"
        else:
            self.ids.calc_input.text = f"{answer}"

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
             self.ids.calc_input.text = f"{prior}."
        elif "." in prior:
            pass
        else:
            self.ids.calc_input.text = f"{prior}."

    def delete(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior[:-1]}"
    
    def sign_inverse(self):
        prior = self.ids.calc_input.text
        if prior[0] == "-":
            self.ids.calc_input.text = f"{prior.replace('-', '')}"
        else:
            self.ids.calc_input.text = f"-{prior}"
class CalculatorApp(App):
    def build(self):
        return MyLayout()
    

if __name__ == "__main__":
    CalculatorApp().run()