import sys
import signal

from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType

from custom_validator import CustomValidator

if __name__ == '__main__':
    signal.signal(signal.SIGINT, lambda *args: QApplication.shutdown())

    app = QApplication(sys.argv)

    qmlRegisterType(CustomValidator, 'MyTest', 1, 0, CustomValidator.__name__)

    engine = QQmlApplicationEngine()
    engine.load('./test.qml')

    sys.exit(app.exec_())
