from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem,IconLeftWidget

KV = '''
ScrollView:

    MDList:
        id: container
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(
                TwoLineListItem(text=f"Friend {i}",secondary_text="Last message text from this friend"),
            )

Test().run()
