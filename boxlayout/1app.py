from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')

from kivymd.app import MDApp
from kivy.lang import Builder

kv="""
MDBoxLayout:
    size_hint: 0.7,0.4
    pos_hint: {"center_x":0.5,"center_y":0.5}
    # adaptive_size: False
    md_bg_color: app.theme_cls.primary_light
    
    MDBoxLayout:
        size_hint: 0.7,0.4 
        pos_hint: {"center_x":0.5,"center_y":0.5}
        md_bg_color: app.theme_cls.primary_dark
        
        # MDLabel:
        #     text: "KivyMD"            
        #     font_style: "H3"

    Box:
        MDTextField:
            hint_text: "Username or Email"
            # pos_hint: {"center_y":0.5}
            
    # MDTextField:
    #     hint_text: "Password"
    #     pos_hint: {"center_x":0.5, "center_y": 0.7}
    #     password: True
    # MDRaisedButton:
    #     text: "Login"
    #     pos_hint: {"center_x":0.5, "center_y":0.45}
    #     size_hint: 0.4,0.04
        

"""

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    MyApp().run()