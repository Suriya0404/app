from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Interface(FloatLayout):
    def print_message(self):
        print('Hello from interface !!!')


class Interface1(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = Button(text="Click Me!", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn.bind(on_press=self.button_press)
        self.add_widget(btn)

    def button_press(self,obj):
        print(obj.text, obj.size)


class FirstApp(App):

    def build(self):
        layout = FloatLayout()
        label = Label(text="Hello world!!!", font_size='32sp', color=(0.5,0.5,1,1))
        text_input = TextInput()
        layout.add_widget(text_input)
        layout.add_widget(label)
        return layout
    def print_message(self):
        print('Hello from app !!!')


FirstApp().run()



