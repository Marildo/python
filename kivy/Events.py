from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class EventTest(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='Botao 01', font_size=33, on_release=self.incrementar)
        button.bind(on_press=self.on_press)
        self.lbl = Label(text='0000')
        box.add_widget(button)
        box.add_widget(self.lbl)
        return box

    def incrementar(self, event):
        value = int(self.lbl.text)
        print(value)
        self.lbl.text = str(value+1)

    def on_press(self, event):
        value = int(self.lbl.text) /10
        self.lbl.color =0.3, 0.3, value






EventTest().run()
