from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
# self.theme_cls.primary_palette = "Purple" no work on icon button
class MyApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDIconButton(
                icon= "android", #use can use png path here
                pos_hint={"center_x":0.5,"center_y":0.5},
                user_font_size= "128sp", #by default 48sp
            )
        )
        return screen
MyApp().run()