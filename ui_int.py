# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newWCSSHMYnEb.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 439)
        MainWindow.setMinimumSize(QSize(960, 0))
        font = QFont()
        font.setFamilies([u"MiSans"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QWidget(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.LeftMenuContainer.setMinimumSize(QSize(150, 0))
        self.verticalLayout = QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuFrame = QFrame(self.LeftMenuContainer)
        self.LeftMenuFrame.setObjectName(u"LeftMenuFrame")
        self.LeftMenuFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LeftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, 0, -1)
        self.InfoButtonFrame = QFrame(self.LeftMenuFrame)
        self.InfoButtonFrame.setObjectName(u"InfoButtonFrame")
        self.InfoButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.InfoButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.InfoButtonFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.InfoButton = QPushButton(self.InfoButtonFrame)
        self.InfoButton.setObjectName(u"InfoButton")
        self.InfoButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.InfoButton.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"ui/svg/airplay.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.InfoButton.setIcon(icon)
        self.InfoButton.setIconSize(QSize(24, 24))
        self.InfoButton.setCheckable(False)
        self.InfoButton.setChecked(False)
        self.InfoButton.setAutoRepeat(False)
        self.InfoButton.setAutoExclusive(False)
        self.InfoButton.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.InfoButton)


        self.verticalLayout_2.addWidget(self.InfoButtonFrame)

        self.SliderButtonFrame = QFrame(self.LeftMenuFrame)
        self.SliderButtonFrame.setObjectName(u"SliderButtonFrame")
        self.SliderButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SliderButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.SliderButtonFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.SliderButton = QPushButton(self.SliderButtonFrame)
        self.SliderButton.setObjectName(u"SliderButton")
        icon1 = QIcon()
        icon1.addFile(u"ui/svg/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SliderButton.setIcon(icon1)
        self.SliderButton.setIconSize(QSize(24, 24))
        self.SliderButton.setCheckable(False)
        self.SliderButton.setAutoExclusive(False)

        self.horizontalLayout_5.addWidget(self.SliderButton)


        self.verticalLayout_2.addWidget(self.SliderButtonFrame)

        self.AppsButtonFrame = QFrame(self.LeftMenuFrame)
        self.AppsButtonFrame.setObjectName(u"AppsButtonFrame")
        self.AppsButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AppsButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.AppsButtonFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.AppsButton = QPushButton(self.AppsButtonFrame)
        self.AppsButton.setObjectName(u"AppsButton")
        icon2 = QIcon()
        icon2.addFile(u"ui/svg/box.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AppsButton.setIcon(icon2)
        self.AppsButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.AppsButton)


        self.verticalLayout_2.addWidget(self.AppsButtonFrame)

        self.AboutButtonFrame = QFrame(self.LeftMenuFrame)
        self.AboutButtonFrame.setObjectName(u"AboutButtonFrame")
        self.AboutButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AboutButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.AboutButtonFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.AboutButton = QPushButton(self.AboutButtonFrame)
        self.AboutButton.setObjectName(u"AboutButton")
        icon3 = QIcon()
        icon3.addFile(u"ui/svg/help-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AboutButton.setIcon(icon3)
        self.AboutButton.setIconSize(QSize(24, 24))
        self.AboutButton.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.AboutButton)


        self.verticalLayout_2.addWidget(self.AboutButtonFrame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout.addWidget(self.LeftMenuFrame)


        self.horizontalLayout.addWidget(self.LeftMenuContainer)

        self.RightMenuContainer = QWidget(self.centralwidget)
        self.RightMenuContainer.setObjectName(u"RightMenuContainer")
        self.verticalLayout_3 = QVBoxLayout(self.RightMenuContainer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 6)
        self.ContButtonsWidget = QWidget(self.RightMenuContainer)
        self.ContButtonsWidget.setObjectName(u"ContButtonsWidget")
        self.ContButtonsWidget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.ContButtonsWidget)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ContButtonFrame = QFrame(self.ContButtonsWidget)
        self.ContButtonFrame.setObjectName(u"ContButtonFrame")
        self.ContButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ContButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.ContButtonFrame)
        self.horizontalLayout_8.setSpacing(18)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.AppVILabel = QLabel(self.ContButtonFrame)
        self.AppVILabel.setObjectName(u"AppVILabel")

        self.horizontalLayout_8.addWidget(self.AppVILabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.hideButton = QPushButton(self.ContButtonFrame)
        self.hideButton.setObjectName(u"hideButton")
        icon4 = QIcon()
        icon4.addFile(u"ui/svg/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hideButton.setIcon(icon4)
        self.hideButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.hideButton)

        self.closeButton = QPushButton(self.ContButtonFrame)
        self.closeButton.setObjectName(u"closeButton")
        icon5 = QIcon()
        icon5.addFile(u"ui/svg/x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeButton.setIcon(icon5)
        self.closeButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.closeButton)


        self.horizontalLayout_7.addWidget(self.ContButtonFrame)


        self.verticalLayout_3.addWidget(self.ContButtonsWidget)

        self.stackedWidget = QStackedWidget(self.RightMenuContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.InfoPageWidget = QWidget()
        self.InfoPageWidget.setObjectName(u"InfoPageWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.InfoPageWidget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.InfoFrame = QFrame(self.InfoPageWidget)
        self.InfoFrame.setObjectName(u"InfoFrame")
        self.InfoFrame.setMinimumSize(QSize(320, 0))
        self.verticalLayout_4 = QVBoxLayout(self.InfoFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.InfoWidget = QWidget(self.InfoFrame)
        self.InfoWidget.setObjectName(u"InfoWidget")
        self.verticalLayout_5 = QVBoxLayout(self.InfoWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.InfosubFrame = QFrame(self.InfoWidget)
        self.InfosubFrame.setObjectName(u"InfosubFrame")
        self.InfosubFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.InfosubFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.InfosubFrame)
        self.verticalLayout_8.setSpacing(18)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ActiveModelLabel = QLabel(self.InfosubFrame)
        self.ActiveModelLabel.setObjectName(u"ActiveModelLabel")

        self.verticalLayout_8.addWidget(self.ActiveModelLabel)

        self.PauseStatusLabel = QLabel(self.InfosubFrame)
        self.PauseStatusLabel.setObjectName(u"PauseStatusLabel")

        self.verticalLayout_8.addWidget(self.PauseStatusLabel)

        self.FoundModelsLabel = QLabel(self.InfosubFrame)
        self.FoundModelsLabel.setObjectName(u"FoundModelsLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FoundModelsLabel.sizePolicy().hasHeightForWidth())
        self.FoundModelsLabel.setSizePolicy(sizePolicy)
        self.FoundModelsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_8.addWidget(self.FoundModelsLabel)


        self.verticalLayout_5.addWidget(self.InfosubFrame)


        self.verticalLayout_4.addWidget(self.InfoWidget)


        self.horizontalLayout_6.addWidget(self.InfoFrame)

        self.ButtonsFrame = QFrame(self.InfoPageWidget)
        self.ButtonsFrame.setObjectName(u"ButtonsFrame")
        self.ButtonsFrame.setMinimumSize(QSize(320, 0))
        self.verticalLayout_6 = QVBoxLayout(self.ButtonsFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ButtonsWidget = QWidget(self.ButtonsFrame)
        self.ButtonsWidget.setObjectName(u"ButtonsWidget")
        self.verticalLayout_7 = QVBoxLayout(self.ButtonsWidget)
        self.verticalLayout_7.setSpacing(9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.ModelFrame = QFrame(self.ButtonsWidget)
        self.ModelFrame.setObjectName(u"ModelFrame")
        self.ModelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ModelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.ModelFrame)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.langframe = QFrame(self.ModelFrame)
        self.langframe.setObjectName(u"langframe")
        self.langframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.langframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.langframe)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.SelectLangLabel = QLabel(self.langframe)
        self.SelectLangLabel.setObjectName(u"SelectLangLabel")

        self.horizontalLayout_15.addWidget(self.SelectLangLabel)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_10)

        self.SelectLangBox = QComboBox(self.langframe)
        self.SelectLangBox.setObjectName(u"SelectLangBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SelectLangBox.sizePolicy().hasHeightForWidth())
        self.SelectLangBox.setSizePolicy(sizePolicy1)
        self.SelectLangBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.SelectLangBox.setFrame(True)

        self.horizontalLayout_15.addWidget(self.SelectLangBox)


        self.verticalLayout_19.addWidget(self.langframe)

        self.modelframe = QFrame(self.ModelFrame)
        self.modelframe.setObjectName(u"modelframe")
        self.modelframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.modelframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.modelframe)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.SelectModelLabel = QLabel(self.modelframe)
        self.SelectModelLabel.setObjectName(u"SelectModelLabel")

        self.horizontalLayout_16.addWidget(self.SelectModelLabel)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_9)

        self.SelectModelBox = QComboBox(self.modelframe)
        self.SelectModelBox.setObjectName(u"SelectModelBox")

        self.horizontalLayout_16.addWidget(self.SelectModelBox)


        self.verticalLayout_19.addWidget(self.modelframe)

        self.vmodframe = QFrame(self.ModelFrame)
        self.vmodframe.setObjectName(u"vmodframe")
        self.vmodframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.vmodframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.vmodframe)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.SelectVModLabel = QLabel(self.vmodframe)
        self.SelectVModLabel.setObjectName(u"SelectVModLabel")

        self.horizontalLayout_17.addWidget(self.SelectVModLabel)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_8)

        self.SelectVModBox = QComboBox(self.vmodframe)
        self.SelectVModBox.setObjectName(u"SelectVModBox")

        self.horizontalLayout_17.addWidget(self.SelectVModBox)


        self.verticalLayout_19.addWidget(self.vmodframe)


        self.verticalLayout_7.addWidget(self.ModelFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.ControlFrame = QFrame(self.ButtonsWidget)
        self.ControlFrame.setObjectName(u"ControlFrame")
        self.ControlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ControlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.ControlFrame)
        self.verticalLayout_17.setSpacing(18)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pauseFrame = QFrame(self.ControlFrame)
        self.pauseFrame.setObjectName(u"pauseFrame")
        self.pauseFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pauseFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.pauseFrame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.PauseLabel = QLabel(self.pauseFrame)
        self.PauseLabel.setObjectName(u"PauseLabel")

        self.horizontalLayout_13.addWidget(self.PauseLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.PauseButton = QPushButton(self.pauseFrame)
        self.PauseButton.setObjectName(u"PauseButton")
        self.PauseButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.PauseButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.PauseButton)


        self.verticalLayout_17.addWidget(self.pauseFrame)

        self.modFrame = QFrame(self.ControlFrame)
        self.modFrame.setObjectName(u"modFrame")
        self.modFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.modFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.modFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.ModLabel = QLabel(self.modFrame)
        self.ModLabel.setObjectName(u"ModLabel")

        self.horizontalLayout_12.addWidget(self.ModLabel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.ModButton = QPushButton(self.modFrame)
        self.ModButton.setObjectName(u"ModButton")
        self.ModButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ModButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.ModButton)


        self.verticalLayout_17.addWidget(self.modFrame)

        self.nlFrame = QFrame(self.ControlFrame)
        self.nlFrame.setObjectName(u"nlFrame")
        self.nlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.nlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.nlFrame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.NoLlamaLabel = QLabel(self.nlFrame)
        self.NoLlamaLabel.setObjectName(u"NoLlamaLabel")
        self.NoLlamaLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_14.addWidget(self.NoLlamaLabel)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.NoLlamaButton = QPushButton(self.nlFrame)
        self.NoLlamaButton.setObjectName(u"NoLlamaButton")
        self.NoLlamaButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.NoLlamaButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.NoLlamaButton)


        self.verticalLayout_17.addWidget(self.nlFrame)


        self.verticalLayout_7.addWidget(self.ControlFrame)


        self.verticalLayout_6.addWidget(self.ButtonsWidget)


        self.horizontalLayout_6.addWidget(self.ButtonsFrame)

        self.stackedWidget.addWidget(self.InfoPageWidget)
        self.SliderPageWidget = QWidget()
        self.SliderPageWidget.setObjectName(u"SliderPageWidget")
        self.verticalLayout_9 = QVBoxLayout(self.SliderPageWidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.SliderFrame = QFrame(self.SliderPageWidget)
        self.SliderFrame.setObjectName(u"SliderFrame")
        self.SliderFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SliderFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.SliderFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.SliderWidget = QWidget(self.SliderFrame)
        self.SliderWidget.setObjectName(u"SliderWidget")
        self.horizontalLayout_18 = QHBoxLayout(self.SliderWidget)
        self.horizontalLayout_18.setSpacing(18)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.slf = QFrame(self.SliderWidget)
        self.slf.setObjectName(u"slf")
        self.slf.setFrameShape(QFrame.Shape.StyledPanel)
        self.slf.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.slf)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.paramFrame = QFrame(self.slf)
        self.paramFrame.setObjectName(u"paramFrame")
        self.paramFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.paramFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.paramFrame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.ReloadModels = QPushButton(self.paramFrame)
        self.ReloadModels.setObjectName(u"ReloadModels")
        icon6 = QIcon()
        icon6.addFile(u"ui/svg/slack.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ReloadModels.setIcon(icon6)
        self.ReloadModels.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.ReloadModels)

        self.ReloadApps = QPushButton(self.paramFrame)
        self.ReloadApps.setObjectName(u"ReloadApps")
        icon7 = QIcon()
        icon7.addFile(u"ui/svg/rotate-cw.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ReloadApps.setIcon(icon7)
        self.ReloadApps.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.ReloadApps)

        self.ReloadConfig = QPushButton(self.paramFrame)
        self.ReloadConfig.setObjectName(u"ReloadConfig")
        icon8 = QIcon()
        icon8.addFile(u"ui/svg/database.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ReloadConfig.setIcon(icon8)
        self.ReloadConfig.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.ReloadConfig)

        self.LinkChangeButton = QPushButton(self.paramFrame)
        self.LinkChangeButton.setObjectName(u"LinkChangeButton")
        icon9 = QIcon()
        icon9.addFile(u"ui/svg/link.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LinkChangeButton.setIcon(icon9)
        self.LinkChangeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.LinkChangeButton)


        self.verticalLayout_20.addWidget(self.paramFrame)

        self.allSlfFrame = QFrame(self.slf)
        self.allSlfFrame.setObjectName(u"allSlfFrame")
        self.allSlfFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.allSlfFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.allSlfFrame)
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Sliders = QFrame(self.allSlfFrame)
        self.Sliders.setObjectName(u"Sliders")
        self.Sliders.setMinimumSize(QSize(0, 0))
        self.Sliders.setFrameShape(QFrame.Shape.StyledPanel)
        self.Sliders.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Sliders)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.speedFrame = QFrame(self.Sliders)
        self.speedFrame.setObjectName(u"speedFrame")
        self.speedFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.speedFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.speedFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.speedSliderInfo = QFrame(self.speedFrame)
        self.speedSliderInfo.setObjectName(u"speedSliderInfo")
        self.horizontalLayout_10 = QHBoxLayout(self.speedSliderInfo)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.speedLabel = QLabel(self.speedSliderInfo)
        self.speedLabel.setObjectName(u"speedLabel")

        self.horizontalLayout_10.addWidget(self.speedLabel)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.speedKeyLabelVAL = QLabel(self.speedSliderInfo)
        self.speedKeyLabelVAL.setObjectName(u"speedKeyLabelVAL")

        self.horizontalLayout_10.addWidget(self.speedKeyLabelVAL)


        self.verticalLayout_13.addWidget(self.speedSliderInfo)

        self.speedSlider = QSlider(self.speedFrame)
        self.speedSlider.setObjectName(u"speedSlider")
        self.speedSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_13.addWidget(self.speedSlider)


        self.verticalLayout_11.addWidget(self.speedFrame)

        self.protect0Frame = QFrame(self.Sliders)
        self.protect0Frame.setObjectName(u"protect0Frame")
        self.protect0Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.protect0Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.protect0Frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.protect0SliderInfo = QFrame(self.protect0Frame)
        self.protect0SliderInfo.setObjectName(u"protect0SliderInfo")
        self.horizontalLayout_9 = QHBoxLayout(self.protect0SliderInfo)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.protect0Label = QLabel(self.protect0SliderInfo)
        self.protect0Label.setObjectName(u"protect0Label")

        self.horizontalLayout_9.addWidget(self.protect0Label)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)

        self.protectKeyLabelVAL = QLabel(self.protect0SliderInfo)
        self.protectKeyLabelVAL.setObjectName(u"protectKeyLabelVAL")

        self.horizontalLayout_9.addWidget(self.protectKeyLabelVAL)


        self.verticalLayout_12.addWidget(self.protect0SliderInfo)

        self.protect0Slider = QSlider(self.protect0Frame)
        self.protect0Slider.setObjectName(u"protect0Slider")
        self.protect0Slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_12.addWidget(self.protect0Slider)


        self.verticalLayout_11.addWidget(self.protect0Frame)

        self.temp0Frame = QFrame(self.Sliders)
        self.temp0Frame.setObjectName(u"temp0Frame")
        self.temp0Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.temp0Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.temp0Frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.temp0SliderInfo = QFrame(self.temp0Frame)
        self.temp0SliderInfo.setObjectName(u"temp0SliderInfo")
        self.horizontalLayout_11 = QHBoxLayout(self.temp0SliderInfo)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tempLabel = QLabel(self.temp0SliderInfo)
        self.tempLabel.setObjectName(u"tempLabel")

        self.horizontalLayout_11.addWidget(self.tempLabel)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.tempKeyLabelVAL = QLabel(self.temp0SliderInfo)
        self.tempKeyLabelVAL.setObjectName(u"tempKeyLabelVAL")

        self.horizontalLayout_11.addWidget(self.tempKeyLabelVAL)


        self.verticalLayout_14.addWidget(self.temp0SliderInfo)

        self.temp0Slider = QSlider(self.temp0Frame)
        self.temp0Slider.setObjectName(u"temp0Slider")
        self.temp0Slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_14.addWidget(self.temp0Slider)


        self.verticalLayout_11.addWidget(self.temp0Frame)


        self.horizontalLayout_20.addWidget(self.Sliders)

        self.Checking = QFrame(self.allSlfFrame)
        self.Checking.setObjectName(u"Checking")
        self.Checking.setFrameShape(QFrame.Shape.StyledPanel)
        self.Checking.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.Checking)
        self.verticalLayout_18.setSpacing(18)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(6, 6, 6, 6)
        self.changeContextIndexFrame = QFrame(self.Checking)
        self.changeContextIndexFrame.setObjectName(u"changeContextIndexFrame")
        self.changeContextIndexFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.changeContextIndexFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.changeContextIndexFrame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 3)
        self.ContextIndexLabel = QLabel(self.changeContextIndexFrame)
        self.ContextIndexLabel.setObjectName(u"ContextIndexLabel")

        self.horizontalLayout_22.addWidget(self.ContextIndexLabel)

        self.IndexspinBox = QSpinBox(self.changeContextIndexFrame)
        self.IndexspinBox.setObjectName(u"IndexspinBox")
        self.IndexspinBox.setMinimumSize(QSize(80, 0))
        self.IndexspinBox.setMaximumSize(QSize(80, 16777215))
        self.IndexspinBox.setWrapping(False)
        self.IndexspinBox.setFrame(True)
        self.IndexspinBox.setReadOnly(False)
        self.IndexspinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.IndexspinBox.setAccelerated(False)
        self.IndexspinBox.setMinimum(1)

        self.horizontalLayout_22.addWidget(self.IndexspinBox)

        self.saveIndexButton = QPushButton(self.changeContextIndexFrame)
        self.saveIndexButton.setObjectName(u"saveIndexButton")
        self.saveIndexButton.setMaximumSize(QSize(24, 24))
        icon10 = QIcon()
        icon10.addFile(u"ui/svg/check.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveIndexButton.setIcon(icon10)
        self.saveIndexButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_22.addWidget(self.saveIndexButton)


        self.verticalLayout_18.addWidget(self.changeContextIndexFrame)

        self.resourceFrame = QFrame(self.Checking)
        self.resourceFrame.setObjectName(u"resourceFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.resourceFrame.sizePolicy().hasHeightForWidth())
        self.resourceFrame.setSizePolicy(sizePolicy2)
        self.resourceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.resourceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.resourceFrame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 0, 9, 0)
        self.resourceMonitor = QLabel(self.resourceFrame)
        self.resourceMonitor.setObjectName(u"resourceMonitor")
        self.resourceMonitor.setMaximumSize(QSize(315, 117))
        self.resourceMonitor.setScaledContents(True)
        self.resourceMonitor.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.resourceMonitor.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.resourceMonitor)


        self.verticalLayout_18.addWidget(self.resourceFrame)

        self.clearContextFrame = QFrame(self.Checking)
        self.clearContextFrame.setObjectName(u"clearContextFrame")
        self.clearContextFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.clearContextFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.clearContextFrame)
        self.horizontalLayout_23.setSpacing(9)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.clearContextButton = QPushButton(self.clearContextFrame)
        self.clearContextButton.setObjectName(u"clearContextButton")
        icon11 = QIcon()
        icon11.addFile(u"ui/svg/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearContextButton.setIcon(icon11)
        self.clearContextButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.clearContextButton)

        self.promptEditButton = QPushButton(self.clearContextFrame)
        self.promptEditButton.setObjectName(u"promptEditButton")
        self.promptEditButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon12 = QIcon()
        icon12.addFile(u"ui/svg/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.promptEditButton.setIcon(icon12)
        self.promptEditButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.promptEditButton)

        self.ollamaNameChangeButton = QPushButton(self.clearContextFrame)
        self.ollamaNameChangeButton.setObjectName(u"ollamaNameChangeButton")
        icon13 = QIcon()
        icon13.addFile(u"ui/svg/ollama-white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ollamaNameChangeButton.setIcon(icon13)
        self.ollamaNameChangeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.ollamaNameChangeButton)


        self.verticalLayout_18.addWidget(self.clearContextFrame)

        self.linksFrame = QFrame(self.Checking)
        self.linksFrame.setObjectName(u"linksFrame")
        self.linksFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.linksFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.linksFrame)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.GitHubbtn = QPushButton(self.linksFrame)
        self.GitHubbtn.setObjectName(u"GitHubbtn")
        icon14 = QIcon()
        icon14.addFile(u"ui/svg/github.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.GitHubbtn.setIcon(icon14)
        self.GitHubbtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.GitHubbtn)

        self.Supportbtn = QPushButton(self.linksFrame)
        self.Supportbtn.setObjectName(u"Supportbtn")
        icon15 = QIcon()
        icon15.addFile(u"ui/svg/thumbs-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Supportbtn.setIcon(icon15)
        self.Supportbtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.Supportbtn)


        self.verticalLayout_18.addWidget(self.linksFrame)


        self.horizontalLayout_20.addWidget(self.Checking)


        self.verticalLayout_20.addWidget(self.allSlfFrame)


        self.horizontalLayout_18.addWidget(self.slf)


        self.verticalLayout_10.addWidget(self.SliderWidget)


        self.verticalLayout_9.addWidget(self.SliderFrame)

        self.stackedWidget.addWidget(self.SliderPageWidget)
        self.AboutPageWidget = QWidget()
        self.AboutPageWidget.setObjectName(u"AboutPageWidget")
        self.verticalLayout_15 = QVBoxLayout(self.AboutPageWidget)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.AboutPageFrame = QFrame(self.AboutPageWidget)
        self.AboutPageFrame.setObjectName(u"AboutPageFrame")
        self.AboutPageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AboutPageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.AboutPageFrame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.AboutLabel = QLabel(self.AboutPageFrame)
        self.AboutLabel.setObjectName(u"AboutLabel")
        self.AboutLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_16.addWidget(self.AboutLabel)


        self.verticalLayout_15.addWidget(self.AboutPageFrame)

        self.stackedWidget.addWidget(self.AboutPageWidget)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.RightMenuContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.InfoButton.setDefault(False)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.InfoButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#if QT_CONFIG(shortcut)
        self.InfoButton.setShortcut(QCoreApplication.translate("MainWindow", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.SliderButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#if QT_CONFIG(shortcut)
        self.SliderButton.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.AppsButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#if QT_CONFIG(shortcut)
        self.AppsButton.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.AboutButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#if QT_CONFIG(shortcut)
        self.AboutButton.setShortcut(QCoreApplication.translate("MainWindow", u"B", None))
#endif // QT_CONFIG(shortcut)
        self.AppVILabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.hideButton.setText(QCoreApplication.translate("MainWindow", u"Minimize to tray", None))
#if QT_CONFIG(shortcut)
        self.hideButton.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"Close app", None))
#if QT_CONFIG(shortcut)
        self.closeButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.ActiveModelLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.PauseStatusLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.FoundModelsLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.SelectLangLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.SelectModelLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.SelectVModLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.PauseLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.PauseButton.setText(QCoreApplication.translate("MainWindow", u"button", None))
        self.ModLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ModButton.setText(QCoreApplication.translate("MainWindow", u"button", None))
        self.NoLlamaLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.NoLlamaButton.setText(QCoreApplication.translate("MainWindow", u"button", None))
        self.ReloadModels.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.ReloadApps.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.ReloadConfig.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.LinkChangeButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.speedLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.speedKeyLabelVAL.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.protect0Label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.protectKeyLabelVAL.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tempKeyLabelVAL.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ContextIndexLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.saveIndexButton.setText("")
        self.resourceMonitor.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.clearContextButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.promptEditButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.ollamaNameChangeButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.GitHubbtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Supportbtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.AboutLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

