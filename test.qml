import QtQuick 2.0
import QtQuick.Controls 2.0
import MyTest 1.0

ApplicationWindow {
    id: root
    visible: true
    width: 300
    height: 300

    TextField {
        anchors.centerIn: parent
        validator: customValidator
    }
    
    CustomValidator {
        id: customValidator
    }
}
