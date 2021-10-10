from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "John Cena", "Elon Musk"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            # temp_label.bind(on_release=self.press_entry)
            # add the button to the "entries_box" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
