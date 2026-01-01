from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Hello Infinix Hot 9")
        button = Button(text="اضغط هنا")

        button.bind(on_press=lambda x: setattr(label, 'text', 'اشتغل التطبيق ✔️'))

        layout.add_widget(label)
        layout.add_widget(button)
        return layout

if __name__ == "__main__":
    MyApp().run()
