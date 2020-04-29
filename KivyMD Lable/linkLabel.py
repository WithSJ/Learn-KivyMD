from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')
# fix size of Kivy App Window 

from kivymd.app import MDApp
from kivy.lang import Builder

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("l.kv")

MyApp().run()