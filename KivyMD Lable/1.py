from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):
        return MDLabel(text="Hello With SJ",pos_hint={"center_x": 0.5, "center_y": 0.5})

if __name__ == "__main__":
    MyApp().run()