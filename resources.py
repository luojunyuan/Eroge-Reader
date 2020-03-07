# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 5.14.1
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x0b\x06\
i\
mport QtQuick 2.\
14\x0d\x0aimport QtQui\
ck.Layouts 1.14\x0d\
\x0aimport QtQuick.\
Controls 2.14\x0d\x0ai\
mport QtQuick.Wi\
ndow 2.14\x0d\x0a\x0d\x0aimp\
ort Main 1.0\x0d\x0a\x0d\x0a\
ApplicationWindo\
w {\x0d\x0a    id: roo\
t\x0d\x0a\x0d\x0a    visible\
: true\x0d\x0a    titl\
e: qsTr('bulid')\
\x0d\x0a    width: 480\
\x0d\x0a    height: 60\
0\x0d\x0a    header: T\
oolBar {\x0d\x0a      \
  RowLayout {\x0d\x0a \
           ancho\
rs.fill: parent\x0d\
\x0a            Too\
lButton {\x0d\x0a     \
           icon.\
source: 'images/\
baseline-menu-24\
px.svg'\x0d\x0a       \
         onClick\
ed: sideNav.open\
()\x0d\x0a\x0d\x0a          \
      SideDrawer\
 {\x0d\x0a            \
        id: side\
Nav\x0d\x0a           \
         // TODO\
: need to reduce\
 drag height\x0d\x0a  \
                \
  height: Applic\
ationWindow.wind\
ow.height\x0d\x0a     \
               o\
nClicked: root.t\
est()\x0d\x0a         \
       }\x0d\x0a      \
      }\x0d\x0a\x0d\x0a     \
       Label {\x0d\x0a\
                \
text: qsTr('chan\
ge title')\x0d\x0a    \
            elid\
e: Label.ElideRi\
ght\x0d\x0a           \
     horizontalA\
lignment: Qt.Ali\
gnHCenter\x0d\x0a     \
           verti\
calAlignment: Qt\
.AlignVCenter\x0d\x0a \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
   }\x0d\x0a        }\x0d\
\x0a    }\x0d\x0a\x0d\x0a    si\
gnal gameStart(s\
tring gamePath)\x0d\
\x0a    signal test\
()\x0d\x0a\x0d\x0a    Scroll\
View {\x0d\x0a        \
id: gamePanel\x0d\x0a\x0d\
\x0a        anchors\
.fill: parent\x0d\x0a\x0d\
\x0a\x0d\x0a        GridV\
iew {\x0d\x0a         \
   cellWidth: 16\
0\x0d\x0a            c\
ellHeight: 250\x0d\x0a\
            clip\
: true\x0d\x0a\x0d\x0a      \
      model: gam\
eModel\x0d\x0a        \
    delegate: ga\
meCard\x0d\x0a        \
}\x0d\x0a        ListM\
odel {\x0d\x0a        \
    id: gameMode\
l\x0d\x0a\x0d\x0a           \
 ListElement { g\
ameName: '\xe3\x82\xa2\xe3\x83\x9e\
\xe3\x83\x84\xe3\x83\x84\xe3\x83\x9f'; path\
: 'C:\x5c\x5cUsers\x5c\x5clj\
y77\x5c\x5cSaved Games\
\x5c\x5c\xe3\x82\xa2\xe3\x83\x9e\xe3\x83\x84\xe3\x83\x84\xe3\x83\
\x9f\x5c\x5ccmvs32.exe' }\
\x0d\x0a        }\x0d\x0a   \
     Component {\
\x0d\x0a            id\
: gameCard\x0d\x0a\x0d\x0a  \
          Item {\
\x0d\x0a              \
  width: GridVie\
w.view.cellWidth\
\x0d\x0a              \
  height: GridVi\
ew.view.cellHeig\
ht\x0d\x0a\x0d\x0a          \
      Column {\x0d\x0a\
                \
    anchors.fill\
: parent\x0d\x0a      \
              pa\
dding: 5\x0d\x0a\x0d\x0a    \
                \
Rectangle{\x0d\x0a    \
                \
    id: img\x0d\x0a\x0d\x0a \
                \
       anchors.h\
orizontalCenter:\
 parent.horizont\
alCenter\x0d\x0a      \
                \
  width: 140\x0d\x0a  \
                \
      height: 20\
0\x0d\x0a             \
           color\
: 'red'\x0d\x0a       \
                \
 border.color: '\
black'\x0d\x0a        \
                \
border.width: 2\x0d\
\x0a\x0d\x0a             \
           Mouse\
Area {\x0d\x0a        \
                \
    anchors.fill\
: parent\x0d\x0a\x0d\x0a    \
                \
        onClicke\
d: {\x0d\x0a          \
                \
      console.lo\
g(index + ' clic\
ked')\x0d\x0a         \
                \
       root.game\
Start(path)\x0d\x0a   \
                \
             // \
le.excute_game_w\
ith_le(path)\x0d\x0a  \
                \
              Ap\
plicationWindow.\
window.visibilit\
y = Window.Minim\
ized\x0d\x0a          \
                \
  }\x0d\x0a           \
             }\x0d\x0a\
                \
    }\x0d\x0a         \
           Label\
 {\x0d\x0a            \
            anch\
ors.horizontalCe\
nter: parent.hor\
izontalCenter\x0d\x0a \
                \
       text: gam\
eName\x0d\x0a         \
           }\x0d\x0a  \
              }\x0d\
\x0a            }\x0d\x0a\
        }\x0d\x0a    }\
\x0d\x0a}\x0d\x0a\
\x00\x00\x02\xfa\
/\
/ SideDrawer.qml\
\x0d\x0a/* qmlscene is\
 not work */\x0d\x0aim\
port QtQuick 2.1\
4\x0d\x0aimport QtQuic\
k.Controls 2.14\x0d\
\x0aimport QtQuick.\
Layouts 1.14\x0d\x0a\x0d\x0a\
Drawer {\x0d\x0a    id\
: root\x0d\x0a\x0d\x0a    si\
gnal clicked()\x0d\x0a\
\x0d\x0a    width: 200\
\x0d\x0a    height: la\
yout.implicitHei\
ght\x0d\x0a\x0d\x0a    Colum\
nLayout {\x0d\x0a     \
   id: layout\x0d\x0a\x0d\
\x0a        width: \
parent.width\x0d\x0a  \
      Label {\x0d\x0a \
           text:\
 'Drawer'\x0d\x0a     \
       horizonta\
lAlignment: Text\
.AlignHCenter\x0d\x0a \
           verti\
calAlignment: Te\
xt.AlignVCenter\x0d\
\x0a            fon\
t.pixelSize: 20\x0d\
\x0a            Lay\
out.fillWidth: t\
rue\x0d\x0a        }\x0d\x0a\
        Button {\
\x0d\x0a            te\
xt: 'List '\x0d\x0a   \
         Layout.\
fillWidth: true\x0d\
\x0a            fla\
t: true\x0d\x0a       \
     background.\
anchors.fill: th\
is\x0d\x0a            \
spacing: 40\x0d\x0a   \
         onClick\
ed: root.clicked\
()\x0d\x0a        }\x0d\x0a \
   }\x0d\x0a}\x0d\x0a\
\x00\x00\x00,\
m\
odule Main\x0d\x0aSide\
Drawer 1.0 ./Sid\
eDrawer.qml\
\x00\x00\x02\xfa\
/\
/ SideDrawer.qml\
\x0d\x0a/* qmlscene is\
 not work */\x0d\x0aim\
port QtQuick 2.1\
4\x0d\x0aimport QtQuic\
k.Controls 2.14\x0d\
\x0aimport QtQuick.\
Layouts 1.14\x0d\x0a\x0d\x0a\
Drawer {\x0d\x0a    id\
: root\x0d\x0a\x0d\x0a    si\
gnal clicked()\x0d\x0a\
\x0d\x0a    width: 200\
\x0d\x0a    height: la\
yout.implicitHei\
ght\x0d\x0a\x0d\x0a    Colum\
nLayout {\x0d\x0a     \
   id: layout\x0d\x0a\x0d\
\x0a        width: \
parent.width\x0d\x0a  \
      Label {\x0d\x0a \
           text:\
 'Drawer'\x0d\x0a     \
       horizonta\
lAlignment: Text\
.AlignHCenter\x0d\x0a \
           verti\
calAlignment: Te\
xt.AlignVCenter\x0d\
\x0a            fon\
t.pixelSize: 20\x0d\
\x0a            Lay\
out.fillWidth: t\
rue\x0d\x0a        }\x0d\x0a\
        Button {\
\x0d\x0a            te\
xt: 'List '\x0d\x0a   \
         Layout.\
fillWidth: true\x0d\
\x0a            fla\
t: true\x0d\x0a       \
     background.\
anchors.fill: th\
is\x0d\x0a            \
spacing: 40\x0d\x0a   \
         onClick\
ed: root.clicked\
()\x0d\x0a        }\x0d\x0a \
   }\x0d\x0a}\x0d\x0a\
\x00\x00\x00,\
m\
odule Main\x0d\x0aSide\
Drawer 1.0 ./Sid\
eDrawer.qml\
\x00\x00\x00\xc7\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22>\x0d\x0a    <path d=\
\x22M0 0h24v24H0z\x22 \
fill=\x22none\x22/>\x0d\x0a \
   <path d=\x22M3 1\
8h18v-2H3v2zm0-5\
h18v-2H3v2zm0-7v\
2h18V6H3z\x22/>\x0d\x0a</\
svg>\x0d\x0a\
"

qt_resource_name = b"\
\x00\x06\
\x07\x8bz\xc2\
\x00r\
\x00e\x00a\x00d\x00e\x00r\
\x00\x02\
\x00\x00\x07\xb9\
\x00u\
\x00i\
\x00\x06\
\x07\x03}\xc3\
\x00i\
\x00m\x00a\x00g\x00e\x00s\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x07\
\x04[\xc2#\
\x00m\
\x00o\x00d\x00u\x00l\x00e\x00s\
\x00\x04\
\x00\x057\xfe\
\x00M\
\x00a\x00i\x00n\
\x00\x0e\
\x02\x963\x5c\
\x00S\
\x00i\x00d\x00e\x00D\x00r\x00a\x00w\x00e\x00r\x00.\x00q\x00m\x00l\
\x00\x06\
\x07\x84+\x02\
\x00q\
\x00m\x00l\x00d\x00i\x00r\
\x00\x16\
\x03d\xbe\x87\
\x00b\
\x00a\x00s\x00e\x00l\x00i\x00n\x00e\x00-\x00m\x00e\x00n\x00u\x00-\x002\x004\x00p\
\x00x\x00.\x00s\x00v\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x12\x00\x02\x00\x00\x00\x03\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00D\x00\x02\x00\x00\x00\x03\x00\x00\x00\x07\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x1c\x00\x02\x00\x00\x00\x01\x00\x00\x00\x06\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00.\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01p\xb5\x96\xac\xdb\
\x00\x00\x00\x9a\x00\x00\x00\x00\x00\x01\x00\x00\x11f\
\x00\x00\x01pq\x88~f\
\x00\x00\x00X\x00\x02\x00\x00\x00\x02\x00\x00\x00\x0a\
\x00\x00\x01p\xaaC\x96\xc6\
\x00\x00\x00f\x00\x00\x00\x00\x00\x01\x00\x00\x0b\x0a\
\x00\x00\x01p\xb5\x96&3\
\x00\x00\x00\x88\x00\x00\x00\x00\x00\x01\x00\x00\x0e\x08\
\x00\x00\x01p\xaa]\x88\xd3\
\x00\x00\x00f\x00\x00\x00\x00\x00\x01\x00\x00\x0e8\
\x00\x00\x01p\xb5\x96&3\
\x00\x00\x00\x88\x00\x00\x00\x00\x00\x01\x00\x00\x116\
\x00\x00\x01p\xaa]\x88\xd3\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
