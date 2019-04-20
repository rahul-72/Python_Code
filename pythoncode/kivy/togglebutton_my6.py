from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout


class My6App(App):
    def build(self):
        return Hello()


class Hello(BoxLayout):
    def btn(self):
        if self.ids['male1'].state=='down':   #When any button is pressed then its state is 'down'....
            print("Hello male toggle button.")

        elif self.ids['female1'].state=='down':
            print("female")

        else:
            print("choose atleast one button")


if __name__ == "__main__":
    My6App().run()
