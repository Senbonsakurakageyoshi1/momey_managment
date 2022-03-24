
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
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp

dropdown = DropDown()
for index in range(10):

    btn = Button(text='Value %d' %index, size_hint_y=None,height=40)
    btn.bind(on_release = lambda btn:dropdown.select(btn.text))

    dropdown.add_widget(btn)

mainbutton = Button(text='Hello',size_hint = (None,None), pos=(350,300))
mainbutton.bind(on_release = dropdown.open)

dropdown.bind(on_select = lambda instance,x:setattr(mainbutton,'text',x))

class check_box(GridLayout):



    def __init__(self,**kwargs):

        super(check_box,self).__init__(**kwargs)


        self.cols = 2

        self.add_widget(Label(text='Male'))
        self.active =  CheckBox(active=True)
        self.add_widget(self.active)

        self.lbl_active = Label(text='Checkbox is on')
        self.add_widget(self.lbl_active)

        #attach a callback
        self.active.bind(active=self.on_checkbox_Active)

        #callback for the checkbox

    def on_checkbox_Active(self,checkboxInstance,isActive):
        if isActive:
            self.lbl_active.text = 'checkbox is ON'
            print("Checbox checked")

        else:
            self.lbl_active.text="checkbox is off"
            print("checkbox unchecked")



        self.add_widget(Label(text='Female'))
        self.active = CheckBox(active=True)
        self.add_widget(self.active)

        self.add_widget(Label(text='Other'))
        self.active = CheckBox(active=True)
        self.add_widget(self.active)
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
        return check_box()



runTouchApp(mainbutton)


CanvasApp().run()
