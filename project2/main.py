from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Interface(FloatLayout):
    def display_information(self):
        data = self.ids.text_input.text
        self.ids.label.text = data


class Project2App(App):
    pass


if __name__ == '__main__':
    Project2App().run()