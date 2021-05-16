曾经的挣扎。。



# File Struct

```powershell
main.py
resources.qrc

\---reader
    |   reader.py
    |   otherfile.py
    |
    \---ui
        |   main.qml
        |   qml_example.qmlproject
        |
        \---images
                baseline-menu-24px.svg
```



## 用 PyInstaller 打包发布

手动打包源代码：

> `.qrc` 文件必须和加载qrc文件的python文件在同一目录。

``` powershell
pyside2-rcc resources.qrc -o resources.py
pyinstaller main.py -y --windowed --additional-hooks-dir pyi_hooks/
```
