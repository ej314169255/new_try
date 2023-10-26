""" parameter setting of Luc let`s go said a Gibbon when step to new planet. 
Lets raise who can introduse wery haigh intelegent think. 
We has three examples and so one. 
It is programer, scool, driver"""

from PyQt5.QtGui import *
import aggdraw
import sys, traceback
from PIL import Image, ImageDraw
class WorkerSignals(QObject):
    """Defines the signals"""
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    progress = pyqtSignal(int)
self._data_lines = dict()
citem, vitem = self.get_or_create_data_row(currency)
vitem.setText("%.4f" % data["close"])
img = Image.new("RGB", (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img)
draw.ellipse((0, 0, 150, 150), fill="red", outline="red")
pen = aggdraw.Pen("red", 0.5)
brush = aggdraw.Brush("red")
draw2 = aggdraw.Draw(img)
draw2.ellipse((150, 150, 300, 300), pen, brush)
draw2.flush()
img.show()

try:
    x = 1 / 0
except ZeroDivisionError:
    Type, Value, Trace = sys.exc_info()
    print ("Type: ", Type)
    print ("Value:", Value)
    print ("Trace:", Trace)
    print ("\n", "print_exception()".center(40, "-"))
    traceback.print_exception(Type, Value, Trace, limit=5,file=sys.stdout)
    print ("\n", "print_tb()".center(40, "-"))
    traceback.print_tb(Trace, limit=1, file=sys.stdout)
