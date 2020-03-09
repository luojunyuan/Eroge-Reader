
import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Window 2.14


Window {
    id: root
    width: 900
    height: 600
    title: qsTr("Text Windows")
//    flags: Qt.SplashScreen | Qt.WindowStaysOnTopHint
    flags: Qt.WA_TransparentForMouseEvents | Qt.WindowStaysOnTopHint
    color: 'transparent'

    Column {
        ToolBar {
            id: bar
            width: root.width
        }
        Rectangle {
            color: 'red'
            height: 200
        }
        TextEdit {
            text: qsTr("ddddddddd")
        }

       Rectangle {
           id: bar

           width: root.width
           color: 'red'
           opacity: 0.27 // #44

           MouseArea {
               acceptedButtons: Qt.LeftBut
               anchors.fill: parentton
               property point clickPos: "0,0"
               onPressed: { //接收鼠标按下事件
                       clickPos  = Qt.point(mouse.x,mouse.y)
               }
               onPositionChanged: {
               // 此信号持续调用
                       //鼠标偏移量
                       var delta = Qt.point(mouse.x-clickPos.x, mouse.y-clickPos.y)

                       root.setX(root.x+delta.x)
                       root.setY(root.y+delta.y)
               }
           }
       }

    }
}
