from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class MyMainApp(App):
    def build(self):
        return Builder.load_file("screen_manager.kv")


if __name__ == "__main__":
    MyMainApp().run()