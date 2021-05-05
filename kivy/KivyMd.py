from kivy.lang import Builder
from kivymd.app import MDApp


class Example(MDApp):
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }

    def build(self):
        with open('kivyMd.kv','r') as file :
            kv= file.read()
            return Builder.load_string(kv)


Example().run()