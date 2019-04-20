from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.splitter import Splitter


class My7App(App):
    def build(self):
        return Hello()


class Hello(BoxLayout):
    pass


if __name__=="__main":
    My7App().run()