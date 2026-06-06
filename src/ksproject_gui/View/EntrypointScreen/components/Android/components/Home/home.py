from carbonkivy.uix.tab import CTab
from carbonkivy.uix.boxlayout import CBoxLayout

from kivy.properties import ObjectProperty
from ksproject_gui.libs.datamodel import KivySchoolData


class Home(CTab):
    data = ObjectProperty() # type: ObjectProperty[KivySchoolData.Android]
    def __init__(self, *args, **kwargs):
        super(Home, self).__init__(*args, **kwargs)
        
class RightLayout(CBoxLayout):
    data = ObjectProperty() # type: ObjectProperty[KivySchoolData.Android]
    def __init__(self, *args, **kwargs):
        super(RightLayout, self).__init__(*args, **kwargs)