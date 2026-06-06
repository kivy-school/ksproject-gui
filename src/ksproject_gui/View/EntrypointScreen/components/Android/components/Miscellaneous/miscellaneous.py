from datetime import datetime
from zoneinfo import ZoneInfo

from carbonkivy.uix.tab import CTab
from carbonkivy.uix.boxlayout import CBoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock

from View.components.PreviewPane import PreviewPane
from ksproject_gui.libs.datamodel import KivySchoolData


class AndroidPane(PreviewPane):
    time = StringProperty()
    data = ObjectProperty() # type: ObjectProperty[KivySchoolData.Android]

    def __init__(self, *args, **kwargs):
        super(AndroidPane, self).__init__(*args, **kwargs)
        Clock.schedule_interval(self.update_time, 1.0)

    def update_time(self, *args) -> None:
        self.time = datetime.now(ZoneInfo("UTC")).strftime("%H:%M")


class Miscellaneous(CTab):
    data = ObjectProperty() # type: ObjectProperty[KivySchoolData.Android]

    def __init__(self, *args, **kwargs):
        super(Miscellaneous, self).__init__(*args, **kwargs)

class MiscellaneousLayout(CBoxLayout):
    data = ObjectProperty() # type: ObjectProperty[KivySchoolData.Android]
    def __init__(self, *args, **kwargs):
        super(MiscellaneousLayout, self).__init__(*args, **kwargs)