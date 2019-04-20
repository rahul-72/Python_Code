from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.factory import Factory

class My3App(App):
    def build(self):
        return Hello()


class Hello(Widget):
    def btn(self):
        return MyPopup().open()

class MyPopup(Popup):
    def hi(self):
        return MyPopup2().open()

class MyPopup2(Popup):
    pass


#Factory.register('MyPopup', cls=MyPopup)



if __name__ == "__main__":
    My3App().run()