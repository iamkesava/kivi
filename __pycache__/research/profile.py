from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker

s1='''
MDFloatLayout:
    id:bg
    md_bg_color:1,1,1,1
    MDFloatLayout:
        size_hint_x:1
        size_hint_y:.33
        pos_hint:{"center_x":.5,"center_y":.85}
        canvas:
            Color:
                rgb:(1,1,1,1)

            Rectangle:
                size:self.size
                pos:self.pos
                source:"pictures/moon.jpeg"

    MDFloatLayout:
        size_hint_x:.265
        size_hint_y:.265
        pos_hint:{"center_x":.5,"center_y":.7}
        canvas:
            Color:
                rgb:(1,1,1,1)

            Ellipse:
                size:self.size
                pos:self.pos
                source:"pictures/Deadpool.jpg"

    MDSwitch:
        id:switch
        pos_hint:{"center_x":.1,"center_y":.1}
        on_active:app.check(*args)

    MDLabel:
        id:name
        text:"G.Kesavarajan"
        pos_hint:{"center_y":.5}
        halign:"center"
        theme_text_color:"Custom"
        #text_color:0,0,1,1
        font_style:"H6"

    MDLabel:
        id:name1
        text:"@youtube"
        pos_hint:{"center_y":.44}
        halign:"center"
        theme_text_color:"Custom"
        #text_color:0,0,1,1
        font_style:"H6"

    MDIconButton:
        id:fb
        icon:"facebook"
        pos_hint:{"center_x":.3,"center_y":.3}
        user_font_size:"60sp"
        theme_text_color:"Custom"
        text_color:66/255,103/255,178/255,1

    MDLabel:
        id:count1
        text:"940k"
        pos_hint:{"center_x":.770,"center_y":.21}
        font_style:"H5"
        bold:True

    MDIconButton:
        id:you
        icon:"youtube"
        user_font_size:"60sp"
        pos_hint:{"center_x":.5,"center_y":.3}
        theme_text_color:"Custom"
        text_color:1,0,0,1
        font_style:"H5"
        bold:True

    MDLabel:
        id:count2
        text:"200k"
        pos_hint:{"center_x":.970,"center_y":.21}
        font_style:"H5"
        bold:True

    MDIconButton:
        id:twitter
        icon:"twitter"
        user_font_size:"60sp"
        pos_hint:{"center_x":.7,"center_y":.3}
        theme_text_color:"Custom"
        text_color:29/255,163/255,242/255,1

    MDLabel:
        id:count3
        text:"2.5M"
        pos_hint:{"center_x":1.154,"center_y":.21}
        font_style:"H5"
        bold:True
'''

class appli(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Gray"
        return Builder.load_string(s1)

    def check(self,checkbox,value):
        if value:
            self.root.md_bg_color=[73/255,72/255,73/255,1]
            self.root.ids.switch.thumb_color_down=[1,1,1,1]
            self.root.ids.name.text_color=[168/255,168/255,168/255,1]
            self.root.ids.name1.text_color=[1,1,1,1]
            
        else:
            self.root.md_bg_color=[1,1,1,1]
            self.root.ids.switch.thumb_color_down=[73/255,72/255,73/255,1]
            self.root.ids.name.text_color=[0,0,0,1]
            self.root.ids.name1.text_color=[0,0,0,1]

appli().run()

