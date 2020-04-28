from kivy.lang import Builder
from kivymd.app import MDApp

class Test(MDApp):
    def build(self):
        return Builder.load_file("toolbar.kv")


Test().run()