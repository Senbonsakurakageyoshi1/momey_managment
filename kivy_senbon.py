
import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle,Color
from kivy.config import Config
from kivy.uix.widget import Widget

class TutorialApp(App):

    def build(self):
        b = BoxLayout(orientation='vertical')


        t = TextInput(font_size=10,
                      size_hint_y=None,
                      height=100)

        f = FloatLayout()


        s = Scatter()

        l = Label(text="Hello !",
                  font_size=50)

        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(t)
        b.add_widget(f)

        # Binding it with the label
        t.bind(text=l.setter('text'))

        return b

class CanvasWidget(Widget):

    def __init__(self,**kwargs):

        super(CanvasWidget,self).__init__(**kwargs)

        with self.canvas:
            Color(.234,.456,.678,.8)

            self.rect =  Rectangle(source= '/home/paindr/PycharmProjects/pythonProject1/k.png', pos = self.center,size = (self.width/2.,self.height/2.))
            self.bind(pos = self.update_rect,size=self.update_rect)

    def update_rect(self,*args):
        self.rect.pos = self.pos
        self.rect.size = self.size
class CanvasApp(App):
    def build(self):
        return CanvasWidget()






CanvasApp().run()
