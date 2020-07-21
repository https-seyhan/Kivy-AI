import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import *
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from random import random
from kivy.properties import ListProperty

import  os
os.chdir('/home/saul/pythontraining/NLP')



kv = '''
<ColoredLabel>:
    size: (100,100)
    pos: (10,10) # no effect
    background_color:
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size
    '''

Builder.load_string(kv)

class ColoredLabel(Label):
    background_color = ListProperty((0,0,0,1))

class MyApp(App):
    def build(self):
        f = AnchorLayout()
        g = GridLayout(cols=2, rows=2)
        layout = BoxLayout(size_hint=(1, None), height=50)
#        v = Video(source='driver.mp4', state='play', options={'eos':'loop'})
        l1 = Label(text="jenkins", font_size=32)
        l2 = Label(text="git", font_size=32)
#        f.add_widget(v)
        self.__getFile()
        label = ColoredLabel(text=self.__getFile(), size_hint=(None, None), background_color=(random(), random(), random(), 1))
        g.add_widget(label)

        f.add_widget(g)

        return f
    def __getFile(self):
        print("Get File")
        #return "Get File"
        with open("journal.txt", 'r') as file:
            journal = file.read()
        return journal

if __name__ == "__main__":
    MyApp().run()