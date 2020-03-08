import QtQuick 2.14
import QtQuick.Layouts 1.14
import QtQuick.Controls 2.14
import QtQuick.Window 2.14
import Qt.labs.platform 1.1

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
    onClosing: ApplicationWindow.window.visibility = Window.Minimized

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
            ListElement { gameName: 'addGame'; path: '' }
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
                                if (gameName === 'addGame') {
                                    console.log('do nothing')
                                    return
                                }

                                ApplicationWindow.window.visibility = Window.Hidden
                                console.log('Send gameStart signal with path ' + path)
                                root.gameStart(path)
                                tray.showMessage("Eroge Reader", "reader is hidden here!", SystemTrayIcon.Information, 500 )
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

    SystemTrayIcon {
        id: tray

        visible: true
        icon.mask: true
        icon.source: "images/octcat.png"
        tooltip: qsTr("システムトレイさんぷる")

        //@@@ Memo:
        // 現状、一度表示したメニューはメニューアイテムをクリックしないと消去されない...
        // メニュー消去のためのコードが必要???

        menu: Menu {
            MenuItem {
                text: qsTr("Panel")
                onTriggered: root.visibility = Window.Windowed
            }
            MenuItem { separator: true }
            MenuItem {
                text: qsTr("Quit")
                onTriggered: Qt.quit()
            }
        }
        onActivated: {
            switch ( reason ) {
            case SystemTrayIcon.Trigger:
                console.log("left clicked.")
                break
            case SystemTrayIcon.MiddleClick:
                console.log("middle clicked.")
                break
            case SystemTrayIcon.Context:
                console.log("right clicked.")
                break;
            case SystemTrayIcon.DoubleClick:
                onTriggered: root.visible = !root.visible
                break
            default:
                console.log( reason )
                break
            }
        }
        onMessageClicked: console.log('message clicked')
    }

}
