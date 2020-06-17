from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
Screen:

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "MDLabel"

        MDLabel:
            text: "MDLabel"
            halign:"center"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()