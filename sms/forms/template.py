import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

form_root = os.path.dirname(__file__)
kv_path = os.path.join(form_root, 'kv_container', 'template.kv')
Builder.load_file(kv_path)


class FormTemplate(Screen):
    form_root = form_root


if __name__ == '__main__':
    from kivy.app import runTouchApp
    from kivy.core.window import Window

    Window.maximize()
    runTouchApp(FormTemplate())
