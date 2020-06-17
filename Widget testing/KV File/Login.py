kv="""
MDTextField:
    hint_text: "required = True"
    required: True
    helper_text_mode: "on_error"
    helper_text: "Enter text"
"""
from kivy.lang import Builder
from kivymd.app import MDApp

class Test(MDApp):
    def build(self):
        return Builder.load_string(kv)


Test().run()