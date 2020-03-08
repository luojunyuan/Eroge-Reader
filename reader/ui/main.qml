import QtQuick 2.14
import QtQuick.Layouts 1.14
import QtQuick.Controls 2.14
import QtQuick.Window 2.14

import Main 1.0

ApplicationWindow {
    id: root

    visible: true
    title: qsTr('bulid')
    width: 480
    height: 600
    header: ToolBar {
        RowLayout {
            anchors.fill: parent
            ToolButton {
                icon.source: 'images/baseline-menu-24px.svg'
                onClicked: sideNav.open()

                SideDrawer {
                    id: sideNav
                    // TODO: need to reduce drag height
                    height: ApplicationWindow.window.height
                    onClicked: root.test()
                }
            }

            Label {
                text: qsTr('change title')
                elide: Label.ElideRight
                horizontalAlignment: Qt.AlignHCenter
                verticalAlignment: Qt.AlignVCenter
                Layout.fillWidth: true
            }
        }
    }

    signal gameStart(string gamePath)
    signal test()

    ScrollView {
        id: gamePanel

        anchors.fill: parent


        GridView {
            cellWidth: 160
            cellHeight: 250
            clip: true

            model: gameModel
            delegate: gameCard
        }
        ListModel {
            id: gameModel

            ListElement { gameName: 'アマツツミ'; path: 'C:\\Users\\ljy77\\Saved Games\\アマツツミ\\cmvs32.exe' }
        }
        Component {
            id: gameCard

            Item {
                width: GridView.view.cellWidth
                height: GridView.view.cellHeight

                Column {
                    anchors.fill: parent
                    padding: 5

                    Rectangle{
                        id: img

                        anchors.horizontalCenter: parent.horizontalCenter
                        width: 140
                        height: 200
                        color: 'red'
                        border.color: 'black'
                        border.width: 2

                        MouseArea {
                            anchors.fill: parent

                            onClicked: {
                                console.log(index + ' clicked')
                                ApplicationWindow.window.visibility = Window.Minimized
                                root.gameStart(path)
                            }
                        }
                    }
                    Label {
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: gameName
                    }
                }
            }
        }
    }
}
