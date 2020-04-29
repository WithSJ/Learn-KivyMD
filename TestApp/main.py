from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')
# fix size of Kivy App Window 

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class MyApp(MDApp):
    dialog = None
    def build(self):
        return Builder.load_file("LoginScreen.kv")
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                size_hint= (0.8,0.5),
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="DISCARD", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()

MyApp().run()