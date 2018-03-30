from PyQt5.QtCore import pyqtSignal, pyqtProperty, QPointF
from PyQt5.QtQuick import QQuickItem


class WidgetController(QQuickItem):

    nameChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        super(WidgetController, self).__init__(parent)

        self._name = ''
        self._proxy = None

        self.nameChanged.connect(self._update_widget) # NOTE: for some reason throws some errors

    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == self._name:
            return
        self._name = value
        self.nameChanged.emit(value)

    def _update_widget(self):
        print('foo')
