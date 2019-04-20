from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.actionbar import ActionBar,ActionButton,ActionGroup,ActionOverflow,ActionView,ActionPrevious
from kivy.uix.boxlayout import BoxLayout
class My1App(App):
    def build(self):
        return Menu()

class Menu(BoxLayout):
    def btn2(self):
        print("I am btn 2")

if __name__ == "__main__":
    My1App().run()