from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')
# fix size of Kivy App Window 
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
class MyApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(Builder.load_file("Email_Field.kv")) 

        screen.add_widget(
            MDRaisedButton(
                text = "Login",
                pos_hint={"center_x":0.5, "center_y":0.5},  
                size_hint=(.3,.045)))        

        return screen

MyApp().run()