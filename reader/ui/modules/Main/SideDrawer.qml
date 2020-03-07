// SideDrawer.qml
/* qmlscene is not work */
import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.14

Drawer {
    id: root

    signal clicked()

    width: 200
    height: layout.implicitHeight

    ColumnLayout {
        id: layout

        width: parent.width
        Label {
            text: 'Drawer'
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.pixelSize: 20
            Layout.fillWidth: true
        }
        Button {
            text: 'List '
            Layout.fillWidth: true
            flat: true
            background.anchors.fill: this
            spacing: 40
            onClicked: root.clicked()
        }
    }
}
