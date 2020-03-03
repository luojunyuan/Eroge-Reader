# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 5.14.1
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x06\x91\
i\
mport QtQuick 2.\
14\x0d\x0aimport QtQui\
ck.Layouts 1.14\x0d\
\x0aimport QtQuick.\
Controls 2.14\x0d\x0a\x0d\
\x0aApplicationWind\
ow {\x0d\x0a    id: ro\
ot\x0d\x0a    visible:\
 true\x0d\x0a    title\
: qsTr('bulid')\x0d\
\x0a\x0d\x0a    width: 48\
0\x0d\x0a    height: 6\
00\x0d\x0a    flags: Q\
t.FramelessWindo\
wHint\x0d\x0a    \x0d\x0a   \
 header: ToolBar\
 {\x0d\x0a        RowL\
ayout {\x0d\x0a       \
     anchors.fil\
l: parent\x0d\x0a     \
       ToolButto\
n {\x0d\x0a           \
     icon.source\
: 'images/baseli\
ne-menu-24px.svg\
'\x0d\x0a             \
   onClicked: si\
deNav.open()\x0d\x0a  \
          }\x0d\x0a   \
         Drawer \
{\x0d\x0a             \
   id: sideNav\x0d\x0a\
                \
width: 200\x0d\x0a    \
            heig\
ht: parent.heigh\
t\x0d\x0a             \
   ColumnLayout \
{\x0d\x0a             \
       width: pa\
rent.width\x0d\x0a    \
                \
Label {\x0d\x0a       \
                \
 text: 'Drawer'\x0d\
\x0a               \
         horizon\
talAlignment: Te\
xt.AlignHCenter\x0d\
\x0a               \
         vertica\
lAlignment: Text\
.AlignVCenter\x0d\x0a \
                \
       font.pixe\
lSize: 20\x0d\x0a     \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
               }\
\x0d\x0a              \
      Button {\x0d\x0a\
                \
        text: 'L\
ist '\x0d\x0a         \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
               f\
lat: true\x0d\x0a     \
                \
   background.an\
chors.fill: this\
\x0d\x0a              \
          spacin\
g: 40\x0d\x0a         \
           }\x0d\x0a  \
              }\x0d\
\x0a            }\x0d\x0a\
            Labe\
l {\x0d\x0a           \
     text: qsTr(\
'change title')\x0d\
\x0a               \
 elide: Label.El\
ideRight\x0d\x0a      \
          horizo\
ntalAlignment: Q\
t.AlignHCenter\x0d\x0a\
                \
verticalAlignmen\
t: Qt.AlignVCent\
er\x0d\x0a            \
    Layout.fillW\
idth: true\x0d\x0a    \
        }\x0d\x0a     \
   }\x0d\x0a    }\x0d\x0a\x0d\x0a \
   TextArea {\x0d\x0a \
       id: text\x0d\
\x0a        placeho\
lderText: qsTr(\x22\
Enter name\x22)\x0d\x0a//\
        text: qs\
Tr(\x22sadfsdfsdfsd\
\x22)\x0d\x0a    }\x0d\x0a\x0d\x0a}\x0d\x0a\
\
\x00\x00\x06j\
i\
mport QtQuick 2.\
14\x0d\x0aimport QtQui\
ck.Layouts 1.14\x0d\
\x0aimport QtQuick.\
Controls 2.14\x0d\x0a\x0d\
\x0aApplicationWind\
ow {\x0d\x0a    id: ro\
ot\x0d\x0a    visible:\
 true\x0d\x0a    title\
: qsTr('bulid')\x0d\
\x0a\x0d\x0a    width: 48\
0\x0d\x0a    height: 6\
00\x0d\x0a\x0d\x0a    header\
: ToolBar {\x0d\x0a   \
     RowLayout {\
\x0d\x0a            an\
chors.fill: pare\
nt\x0d\x0a            \
ToolButton {\x0d\x0a  \
              ic\
on.source: 'imag\
es/baseline-menu\
-24px.svg'\x0d\x0a    \
            onCl\
icked: sideNav.o\
pen()\x0d\x0a         \
   }\x0d\x0a          \
  Drawer {\x0d\x0a    \
            id: \
sideNav\x0d\x0a       \
         width: \
200\x0d\x0a           \
     height: par\
ent.height\x0d\x0a    \
            Colu\
mnLayout {\x0d\x0a    \
                \
width: parent.wi\
dth\x0d\x0a           \
         Label {\
\x0d\x0a              \
          text: \
'Drawer'\x0d\x0a      \
                \
  horizontalAlig\
nment: Text.Alig\
nHCenter\x0d\x0a      \
                \
  verticalAlignm\
ent: Text.AlignV\
Center\x0d\x0a        \
                \
font.pixelSize: \
20\x0d\x0a            \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
        }\x0d\x0a     \
               B\
utton {\x0d\x0a       \
                \
 text: 'List '\x0d\x0a\
                \
        Layout.f\
illWidth: true\x0d\x0a\
                \
        flat: tr\
ue\x0d\x0a            \
            back\
ground.anchors.f\
ill: this\x0d\x0a     \
                \
   spacing: 40\x0d\x0a\
                \
    }\x0d\x0a         \
       }\x0d\x0a      \
      }\x0d\x0a       \
     Label {\x0d\x0a  \
              te\
xt: qsTr('change\
 title')\x0d\x0a      \
          elide:\
 Label.ElideRigh\
t\x0d\x0a             \
   horizontalAli\
gnment: Qt.Align\
HCenter\x0d\x0a       \
         vertica\
lAlignment: Qt.A\
lignVCenter\x0d\x0a   \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
 }\x0d\x0a        }\x0d\x0a \
   }\x0d\x0a\x0d\x0a    Text\
Area {\x0d\x0a        \
id: text\x0d\x0a      \
  placeholderTex\
t: qsTr(\x22Enter n\
ame\x22)\x0d\x0a//       \
 text: qsTr(\x22sad\
fsdfsdfsd\x22)\x0d\x0a   \
 }\x0d\x0a\x0d\x0a}\x0d\x0a\
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
\x00\x10\
\x04K\xc2<\
\x00a\
\x00t\x00t\x00a\x00c\x00h\x00W\x00i\x00n\x00d\x00o\x00w\x00.\x00q\x00m\x00l\
\x00\x06\
\x07\x03}\xc3\
\x00i\
\x00m\x00a\x00g\x00e\x00s\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
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
\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01p\x9f\xff\x93U\
\x00\x00\x00B\x00\x02\x00\x00\x00\x01\x00\x00\x00\x06\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00T\x00\x00\x00\x00\x00\x01\x00\x00\x06\x95\
\x00\x00\x01p\x9e\x16\xd6\x0b\
\x00\x00\x00j\x00\x00\x00\x00\x00\x01\x00\x00\x0d\x03\
\x00\x00\x01pq\x88~f\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
