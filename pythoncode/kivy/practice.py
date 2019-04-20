from kivy.app import App
from kivy.graphics import Canvas
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color
class MyApp(App):
    def build(self):
        return Hello()

class Hello(BoxLayout):
    pass


if __name__ == "__main__":
    MyApp().run()

