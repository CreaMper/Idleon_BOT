from ctypes import windll, Structure, c_long, byref
from ctypes.wintypes import POINT


class Mouse:

    def queryMousePosition(self):
        point = POINT()
        windll.user32.GetCursorPos(byref(point))
        return point.x, point.y