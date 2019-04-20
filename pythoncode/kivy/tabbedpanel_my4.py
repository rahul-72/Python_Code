from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout


class My4App(App):
    def build(self):
        return Hello()


class Hello(BoxLayout):
    pass


if __name__ == "__main__":
    My4App().run()