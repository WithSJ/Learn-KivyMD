from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen
class Test(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDLabel(
            text="MyLabel",
            pos_hint={"center_x":0.95, "center_y":0.5}
        ))
        
        # screen.add_widget(
        #     MDRaisedButton(
        #     text="MyLabel",
        #     pos_hint={"center_x":0.5, "center_y":0.5}
        # ))

        
        return screen


Test().run()