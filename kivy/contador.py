from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass

class Contador(App):
    def build(self):
        return Incrementador()

Contador().run()
