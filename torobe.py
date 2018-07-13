from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class Torobe(FloatLayout):
    pass

class TorobeApp(App):
    def build(self):
        return Torobe()

if __name__ == '__main__':
    TorobeApp().run()
