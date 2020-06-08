from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen = Screen()
        screen.add_widget(
            MDFlatButton(
                text="HEllo",
                pos_hint={"center_x":0.5,"center_y":0.5},
                # increment_width= "164dp"
                # text_color= [1, 0, 0, 0]
            )
        )
        return screen

MyApp().run()
        