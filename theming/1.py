from kivymd.app import MDApp


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"

    def on_start(self):
        self.fps_monitor_start()
        

if __name__ == "__main__":
    MyApp().run()