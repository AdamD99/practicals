from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION = 1.609344


class ConvertMilesKmApp(App):
    output_km = StringProperty()

    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, miles):
        try:
            kilometers = round(int(miles) * CONVERSION, 3)
            self.output_km = str(kilometers)
        except ValueError:
            self.output_km = '0.0'

    def handle_increment(self, value):
        try:
            miles = int(self.root.ids.input_miles.text) + value
            self.root.ids.input_miles.text = str(miles)
        except ValueError:
            self.root.ids.input_miles.text = str(value)


ConvertMilesKmApp().run()
