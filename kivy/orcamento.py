from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import mysql.connector

class Contener(BoxLayout):    
    def buscar(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='si411225',
            database= 'world'
        )

        cursor = conn.cursor()
        cursor.execute('Select * from categories')
        result =  cursor.fetchall()
        for  item in result:
            self.ids.table.add_widget(Label(text=item[1],font_size=10))


class Orcamento(App):
    def build(self):
        return Contener()



Orcamento().run()
