from kivy.app import App
from kivy.uix.filechooser import FileChooser,FileChooserListView
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import os
class My5App(App):
    def build(self):
        return Hello()


class Hello(BoxLayout):
    def btn(self):
        return MyPopup().open()

class MyPopup(Popup):
    def open1(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print(f.read())

if __name__ == "__main__":
    My5App().run()
