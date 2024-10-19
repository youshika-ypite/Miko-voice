import os

from configure__main import Applicator

from ui_appendApp import Ui_MainWindow as ac_Ui_MainWindow

from PySide6.QtWidgets import QLayout, QScrollArea, QGridLayout
from PySide6.QtWidgets import QWidget, QMainWindow, QLabel
from PySide6.QtWidgets import QFrame, QComboBox, QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QTextEdit
from PySide6.QtGui import QMouseEvent, Qt, QIcon

colorCircles = {"red": "🔴", "yellow": "🟡", "green": "🟢"}
toolTips = {
    'green': "Nothing is needed, everything is fine!",
    'red': "You need to enter your own path",
    'yellow': "You need to confirm the found path OR enter it yourself"
    }

class NotifyDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Miko!! notificate")
        self.setWindowIcon(QIcon("ui/icon.png"))

        self.widget = QWidget()
        self.mainlayout = QHBoxLayout(self.widget)

        self.label = QLabel("Text")

        self.mainlayout.addWidget(self.label)

        self.setMinimumWidth(360)
        self.setMaximumWidth(360)
        self.setMinimumHeight(20)
        self.setMaximumHeight(20)

        self.notificateTexts = {
            "voiceWarn": "Please, close and open again app for the changes to free up mem",

            "pathError_f": "Path not found",
            "pathError_w": "Path is incorrect",
            "pathError_e": "Path cannot be empty",
            "pathError_n": "The path does not exist",
            
            "nameError_e": "Name cannot be empty"
            }
        

    def setText(self, text: str = None, key: str = None):
        if text is None: text = self.notificateTexts[key]
        trigger = text
        self.label.setText(trigger)

    def fastNotificate(self, text: str = None, key: str = None):
        """
        ### Keys : values
        * voiceWarn - "Please, close and open again app for the changes to free up mem"
        * pathError_f - "Path not found"
        * pathError_w - "Path is incorrect"
        * pathError_e - "Path cannot be an empty"
        * pathError_n - "The path does not exist"
        * nameError_e - "Name cannot be empty"
        """
        self.setText(text, key)
        self.show()

class AppCreator(QMainWindow):
    def __init__(self, updater, notificator: NotifyDialog) -> None:
        QMainWindow.__init__(self)
        self.ui = ac_Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(f"Miko!!")
        self.setWindowIcon(QIcon("ui/icon.png"))
        self.setStyleSheet("QPushButton:hover {background-color: #00d26a;}")

        self.updater = updater
        self.notificator = notificator
        self.ui.saveButton.clicked.connect(self.save_app)

    def save_app(self):
        _name = self.ui.inputName.toPlainText()
        _path = self.ui.inputPath.toPlainText()

        if _name in ["", " ", None]:
            self.notificator.fastNotificate(key="nameError_e")
            return
        if _path in ["", " ", None]:
            self.notificator.fastNotificate(key="pathError_e")
            return
        if _path[1] != ":" or not _path.endswith(tuple([".exe", ".lnk", ".url"])):
            self.notificator.fastNotificate(key="pathError_w")
            return
        if not os.path.isfile(_path):
            self.notificator.fastNotificate(key="pathError_n")
            return
        
        Applicator.appendApp(_name, _path)
        self.updater()

class PathChanger(QMainWindow):
    def __init__(
            self,
            datapack: dict, updater,
            notificator: NotifyDialog,
            windows: list[QLayout, QWidget] = None
            ) -> None:
        super().__init__()
        
        self.windows = windows
        self.updater = updater
        self.notificator = notificator

        self.activePath = datapack['possible_path']
        self.name = datapack['name']

        self.setWindowTitle("Miko!!"+self.name)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon("ui/icon.png"))
        self.setStyleSheet(
            "QFrame {border-color: black; border-width: 2px}\n"\
            "#tittle {border-style: solid solid dotted solid;}\n"\
            "#input {border-style: none solid none solid;}\n"\
            "#info {border-style: dotted solid solid solid;}\n"\
            "#saveButton:hover {background-color: #00d26a;}\n"\
            "#deltButton:hover {background-color: #ff5252;}\n"\
            "#cancButton:hover {background-color: lightblue;}"
            )
        
        self.oldpos = None

        self.widget = QWidget()
        self.mainlayout = QVBoxLayout(self.widget)

        self.tittleFrame = QFrame()
        self.inputFrame = QFrame()
        self.infoFrame = QFrame()

        self.inputFrame.setObjectName("input")
        self.tittleFrame.setObjectName("tittle")
        self.infoFrame.setObjectName("info")

        self.tittlelayout = QHBoxLayout()
        self.inputlayout = QHBoxLayout()
        self.infolayout = QHBoxLayout()

        self.tittle_infoText = QLabel("Please select your Path to "+self.name)
        self.tittle_pathBox = QComboBox()
        self.tittle_pathBox.addItem(self.activePath)
        self.tittle_pathBox.activated.connect(self.boxTrigger)

        self.tittlelayout.addWidget(self.tittle_infoText)
        self.tittlelayout.addWidget(self.tittle_pathBox)

        self.tittleFrame.setLayout(self.tittlelayout)

        self.input_info = QLabel("OR enter path manualy")
        self.input_inputPath = QTextEdit()
        self.input_inputPath.setMaximumHeight(40)
        self.input_saveButton = QPushButton("Save path")
        self.input_saveButton.clicked.connect(self._savePath)
        self.input_saveButton.setObjectName("saveButton")

        self.inputlayout.addWidget(self.input_info)
        self.inputlayout.addWidget(self.input_inputPath)
        self.inputlayout.addWidget(self.input_saveButton)

        self.inputFrame.setLayout(self.inputlayout)

        self.info_path = QLabel("Active path: "+self.activePath)
        self.info_deltButton = QPushButton("Delete")
        self.info_deltButton.clicked.connect(self._delete)
        self.info_deltButton.setObjectName("deltButton")
        self.info_cancButton = QPushButton("Cancel")
        self.info_cancButton.clicked.connect(self._cancel)
        self.info_cancButton.setObjectName("cancButton")

        self.infolayout.addWidget(self.info_path)
        self.infolayout.addWidget(self.info_deltButton)
        self.infolayout.addWidget(self.info_cancButton)

        self.infoFrame.setLayout(self.infolayout)

        self.mainlayout.addWidget(self.tittleFrame)
        self.mainlayout.addWidget(self.inputFrame)
        self.mainlayout.addWidget(self.infoFrame)

        self.setCentralWidget(self.widget)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldpos = event.globalPos()
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.oldpos is not None:
            diff = event.globalPos() - self.oldpos
            self.move(self.pos() + diff)
            self.oldpos = event.globalPos()
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.oldpos = None

    def getBoxText_(self) -> str: return self.tittle_pathBox.currentText()

    def getPath_(self) -> str:
        _path = self.input_inputPath.toPlainText()
        if any([_path is None, _path == "", _path == " "]):
            selected = self.tittle_pathBox.currentText()
            _path = selected if selected == self.activePath else self.activePath
        if _path[0] == '"': _path = _path.replace('"', '')
        if _path[1] != ":" or not _path.endswith(tuple([".exe", ".lnk", ".url"])) or not os.path.isfile(_path):
            self.notificator.fastNotificate(key="pathError_w")
        return _path
    
    def remove_(self) -> None:
        if self.windows is not None:
            self.windows[0].removeWidget(self.windows[1])
            self.windows[1].deleteLater()

    def _delete(self) -> None:
        Applicator.deleteApp(self.name)
        self.updater()
        self.remove_()
        self.close()

    def _savePath(self) -> None:
        _path = self.getPath_()

        Applicator.deleteNeedAcceptApps(self.name, _path)
        self.updater()
        self.remove_()
        self.close()

    def _cancel(self) -> None: self.close()
    def boxTrigger(self): self.input_inputPath.setText(self.getBoxText_())

def generateApp(data: dict, updater, pch, confirmBtn: bool, notificator: NotifyDialog):

    def remover(layout: QLayout, widget: QWidget):
        layout.removeWidget(widget)
        widget.deleteLater()

    def confirm(layout: QLayout, widget: QWidget):
        remover(layout, widget)
        Applicator.deleteNeedAcceptApps(data["name"], data["possible_path"])
        updater()

    def openDir(_path: str | None):
        if _path is None:
            notificator.fastNotificate(key='pathError_f')
            return
        symbol_ID = 0
        for ind in range(-1, len(_path)*-1, -1):
            if _path[ind] == "\\":
                symbol_ID = ind
                break
        if symbol_ID != 0:
            openPATH = _path[:symbol_ID]
            if os.path.exists(openPATH): os.startfile(openPATH)
            else: notificator.fastNotificate(key="pathError_f")
        else: notificator.fastNotificate(key="pathError_w")

    def _delete(layout: QLayout, widget: QWidget, name: str):
        remover(layout, widget)
        Applicator.deleteApp(name)
        updater()

    def _change(layout: QLayout, widget: QWidget):
        pch(PathChanger(data, updater, notificator, [layout, widget]))

    widget = QWidget()

    mainlayout = QVBoxLayout(widget)
    mainframe = QFrame()
    mainframe_Layout = QVBoxLayout()

    _firstdlayout = QVBoxLayout()
    _firstlayout_adt = QHBoxLayout()
    _secondlayout = QHBoxLayout()

    __firstdFrame, __firstFrame_adt = QFrame(), QFrame()
    __secondFrame = QFrame()

    colorCircle, color = colorCircles["green"], '#00d26a'
    status, toolTip = 'Ready', toolTips['green']
    if data["possible_path"] is None:
        colorCircle, color = colorCircles["red"], '#ff5252'
        status, toolTip = 'Need path', toolTips['red']
    elif data["relative_path"] is None:
        colorCircle, color = colorCircles["yellow"], '#ffda13'
        status, toolTip = 'Need confirm', toolTips['yellow']

    mainframe.setObjectName("mainFrameB")
    mainframe.setStyleSheet(
        "#mainFrameB "\
        "{\n"\
        "   border-style: none none solid solid;\n"\
        "   border-width: 3px;\n"\
        "   border-color: "+color+";\n"\
        "}")
    
    appName, appPath = QLabel(colorCircle+data["name"]), data["possible_path"]
    openButton = QPushButton("Open directory")
    chngButton, _delButton = QPushButton("Change path"), QPushButton("Delete app")
    _appStatus = QLabel(status+"⚠️")
    _appStatus.setToolTip(toolTip)

    _delButton.setStyleSheet("QPushButton:hover {background-color: #ff5252;}")

    openButton.setToolTip(data['possible_path'])

    openButton.clicked.connect(lambda: openDir(appPath))
    _delButton.clicked.connect(lambda: _delete(mainlayout, widget, data["name"]))
    chngButton.clicked.connect(lambda: _change(mainlayout, widget))

    _firstlayout_adt.addWidget(appName)
    _firstlayout_adt.addWidget(_appStatus, alignment=Qt.AlignRight)

    __firstFrame_adt.setLayout(_firstlayout_adt)

    _firstdlayout.addWidget(__firstFrame_adt)
    _firstdlayout.addWidget(openButton)

    if confirmBtn:
        confirmButton = QPushButton("Confirm")
        confirmButton.setStyleSheet("QPushButton:hover {background-color: #00d26a;}")
        confirmButton.clicked.connect(
            lambda: confirm(mainlayout, widget)
        )
        _secondlayout.addWidget(confirmButton)
    _secondlayout.addWidget(chngButton)
    _secondlayout.addWidget(_delButton)

    _firstdlayout.setContentsMargins(0, 0, 0, 0)
    _secondlayout.setContentsMargins(0, 0, 0, 0)

    __firstdFrame.setLayout(_firstdlayout)
    __secondFrame.setLayout(_secondlayout)

    mainframe_Layout.addWidget(__firstdFrame)
    mainframe_Layout.addWidget(__secondFrame)

    mainframe.setLayout(mainframe_Layout)

    mainlayout.addWidget(mainframe)

    return widget

class AppConfigurator(QMainWindow):
    def __init__(self, updater, enumerator):
        super().__init__()

        self.setStyleSheet(
            "QPushButton:hover {background-color: lightblue;}\n"\
            "#infoLayout {border-bottom: 2px solid black;}"
            )
        self.setWindowTitle(f"Miko!! App Configurator")
        self.setWindowIcon(QIcon("ui/icon.png"))

        self.notificator = NotifyDialog()

        self.pchange = None
        self.appCreator = None

        self.widget = QWidget()
        self.appWidget = QWidget()
        self.mainlayout = QVBoxLayout(self.widget)

        self.appLayout = QGridLayout(self.appWidget)

        self.infoFrame = QFrame()
        self.infoLayout = QHBoxLayout()

        self.addAppButton = QPushButton("Add another app")
        self.addAppButton.clicked.connect(lambda: self.newApp(updater))
        
        self.infoLayout.setObjectName("infoLayout")

        self.infoLayout.addWidget(QLabel(
            "| "\
            f"{colorCircles['green']} - Good |"\
            f"{colorCircles['yellow']} - Need confirm to use |"\
            f"{colorCircles['red']} - Need path |"
            ))
        self.infoLayout.addWidget(self.addAppButton)
        self.infoFrame.setLayout(self.infoLayout)

        if enumerator:
            self.apps = [
                generateApp(
                    data, updater, self.pchangershow, confirmBtn=True, notificator=self.notificator
                    ) for data in Applicator.getNeedAcceptApps().values() if 'name' in data
                ]
        else:
            self.apps = [
                generateApp(
                    data, updater, self.pchangershow, confirmBtn=False, notificator=self.notificator
                    ) for data in Applicator.getApps().values() if 'name' in data
                ]

        self.matrix_build()
        self.paintMatrix()

        self.setMinimumWidth(int(self.scroller.width()*1.2))
        self.setMinimumHeight(570)

    def closeEvent(self, event):
        if self.pchange is not None:
            try: self.pchange.close()
            except: pass
        if self.appCreator is not None:
            try: self.appCreator.close()
            except: pass

    def matrix_build(self):
        matrix = [0, 0]
        for i, app in enumerate(self.apps):
            self.appLayout.addWidget(
                app, matrix[0], matrix[1],
                alignment=Qt.AlignTop
                )
            if matrix[1] != 1: matrix[1] += 1
            else:
                matrix[0] += 1
                matrix[1] = 0

    def paintMatrix(self):
        self.scroller = QScrollArea()
        self.scroller.setWidgetResizable(True)

        self.mainlayout.addWidget(self.infoFrame)
        self.mainlayout.addWidget(self.scroller)

        self.scroller.setWidget(self.appWidget)

        self.setCentralWidget(self.widget)

    def pchangershow(self, pchange: PathChanger):
        self.pchange = pchange
        self.pchange.show()

    def newApp(self, updater):
        self.appCreator = AppCreator(updater, self.notificator)
        self.appCreator.show()