from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
# import matplotlib.pyplot as plt
# import csv
# import duplic
from threading import Thread
import subprocess
import sys
import os


def main():

    class LoadDialog(FloatLayout):
        load = ObjectProperty(None)
        cancel = ObjectProperty(None)



    class Root(FloatLayout):

        def dismiss_popup(self):
            self._popup.dismiss()

        def show_load(self):
            content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
            self._popup = Popup(title="Select Folder", content=content,
                                size_hint=(0.9, 0.9))
            self._popup.open()

        def load(self, path, filename):
            global duplicate_find
            self.file_name = str(os.path.join(path, filename[0]))
            print(self.file_name)
            log_file = open("Logs.log", 'w')
            log_file.write(self.file_name)
            duplicate_find = subprocess.Popen('python duplic.py', shell=True)
            self.dismiss_popup()
            # self.duplicate_find = Thread(target=duplic.bigger(self.file_name))
            # self.duplicate_find.daemon = True
            # self.duplicate_find.start()

    class FChooserApp(App):
        pass


    Factory.register('Root', cls=Root)
    Factory.register('LoadDialog', cls=LoadDialog)
    FChooserApp().run()


if __name__ == '__main__':
    main()
    