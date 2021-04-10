from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class WindowManager(ScreenManager):
    pass

class Tasks(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self)

class TaskList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self)
    # for i in range(10):
    #    self.ids.box.add_widget(Label(text='T:', font_size=30))


class MyTasks(App):
    def build(self):
       return Builder.load_file('mytasks.kv')


MyTasks().run()
