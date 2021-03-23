from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BoxLyt(App):
    def build(self):
        btn1 = Button(text='Botao 01')
        btn2 = Button(text='Botao 02')
        btn3 = Button(text='Botao 03')

        box = BoxLayout(orientation='horizontal')
        box.add_widget(btn1)
        box.add_widget(btn2)
        box.add_widget(btn3,0)

        return box


BoxLyt().run()
