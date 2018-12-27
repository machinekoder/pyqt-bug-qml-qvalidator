from PyQt5.QtGui import QValidator


class CustomValidator(QValidator):
    def __init__(self, parent=None):
        super(CustomValidator, self).__init__(parent)

    def validate(self, s, pos):
        return QValidator.Acceptable, s, pos

    def fixup(self, s):
        return s
