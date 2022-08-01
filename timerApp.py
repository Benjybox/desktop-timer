import kivy
from kivy.app import App
from kivy.app import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout

def on_button_click(self):
    print ("Timer Started")


class MainWidget(Widget):
    pass

class TimerApp (App):
    pass

TimerApp().run()