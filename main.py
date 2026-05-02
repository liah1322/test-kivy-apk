from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(
            text='Hello World\n\nPython在Android上运行成功！',
            halign='center',
            valign='middle'
        )

if __name__ == '__main__':
    TestApp().run()
