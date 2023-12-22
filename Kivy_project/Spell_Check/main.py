import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.spelling import Spelling

Builder.load_file("spell_check.kv")

class MyLayout(Widget):
    def press(self):
        spelling = Spelling()
        spelling.select_language('en-US')
        # to see the list of languages
        # spelling.list_languages()
        word = self.ids.word_input.text
        suggestions = spelling.suggest(word)
        words = ""
        for suggetion in suggestions:
            words = f"{words} {suggetion}"
        
        self.ids.word_label.text = f"{words}"

class MyApp(App):

    def build(self):
        return MyLayout()
    
if __name__ == "__main__":
    MyApp().run()