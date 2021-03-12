import sys
from googletrans import Translator
import pyperclip
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Google Translate Tool')
        self.setStyleSheet('background-color: #121212;')
        self.setMinimumSize(520, 255)
        self.setMaximumSize(520, 255)

        self.translation_widget = TranslationWidget()
        self.setCentralWidget(self.translation_widget)


class TranslationWidget(QtWidgets.QWidget):
    def __init__(self):
        self.translator = Translator()

        super(TranslationWidget, self).__init__()
        self.main_layout = QtWidgets.QVBoxLayout()

        # 英語→日本語
        self.en_jp_radio = QtWidgets.QRadioButton('英語 → 日本語', self)
        self.en_jp_radio.setChecked(True)
        self.en_jp_radio.move(30, 20)
        self.en_jp_radio.setStyleSheet('color: white;')
        self.main_layout.addWidget(self.en_jp_radio)

        # 日本語→英語
        self.jp_en_radio = QtWidgets.QRadioButton('日本語 → 英語', self)
        self.jp_en_radio.move(150, 20)
        self.jp_en_radio.setStyleSheet('color: white;')
        self.main_layout.addWidget(self.jp_en_radio)

        # 翻訳前テキスト
        self.before_translation = QtWidgets.QTextEdit(self)
        self.before_translation.resize(470, 60)
        self.before_translation.move(25, 40)
        self.before_translation.setStyleSheet(
            'background-color: #121212;'
            'color: white;'
        )
        self.before_translation.setText('')
        self.before_translation.setPlaceholderText('翻訳前のテキスト')
        self.main_layout.addWidget(self.before_translation)

        # ペーストボタン
        self.paste_btn = QtWidgets.QPushButton('ペースト', self)
        self.paste_btn.resize(100, 30)
        self.paste_btn.move(30, 120)
        self.paste_btn.setStyleSheet(
            'background-color: white;'
            'border-radius: 5px 5px 5px 5px;'
        )
        self.paste_btn.clicked.connect(self.paste_text)
        self.main_layout.addWidget(self.paste_btn)

        # コピーボタン
        self.copy_btn = QtWidgets.QPushButton('コピー', self)
        self.copy_btn.resize(100, 30)
        self.copy_btn.move(150, 120)
        self.copy_btn.setStyleSheet(
            'background-color: white;'
            'border-radius: 5px 5px 5px 5px;'
        )
        self.copy_btn.clicked.connect(self.copy_text)
        self.main_layout.addWidget(self.copy_btn)

        # クリアボタン
        self.clear_btn = QtWidgets.QPushButton('クリア', self)
        self.clear_btn.resize(100, 30)
        self.clear_btn.move(270, 120)
        self.clear_btn.setStyleSheet(
            'background-color: white;'
            'border-radius: 5px 5px 5px 5px;'
        )
        self.clear_btn.clicked.connect(self.clear_text)
        self.main_layout.addWidget(self.clear_btn)

        # 翻訳ボタン
        self.translation_btn = QtWidgets.QPushButton('翻訳', self)
        self.translation_btn.resize(100, 30)
        self.translation_btn.move(390, 120)
        self.translation_btn.setStyleSheet(
            'background-color: white;'
            'border-radius: 5px 5px 5px 5px;'
        )
        self.translation_btn.clicked.connect(self.google_translation)
        self.main_layout.addWidget(self.translation_btn)

        # 翻訳後テキスト
        self.after_translation_text = QtWidgets.QTextEdit(self)
        self.after_translation_text.resize(470, 60)
        self.after_translation_text.move(25, 170)
        self.after_translation_text.setStyleSheet(
            'background-color: #121212;'
            'color: white;'
        )
        self.after_translation_text.setText('')
        self.after_translation_text.setReadOnly(True)
        self.after_translation_text.setPlaceholderText('翻訳後のテキスト')
        self.main_layout.addWidget(self.after_translation_text)

    def paste_text(self):
        self.before_translation.setText(pyperclip.paste())

    def copy_text(self):
        pyperclip.copy(self.after_translation_text.toPlainText())

    def clear_text(self):
        self.en_jp_radio.setChecked(True)
        self.before_translation.setText('')
        self.after_translation_text.setText('')

    def google_translation(self):
        if self.before_translation.toPlainText():
            self.after_translation_text.setReadOnly(False)
            if self.en_jp_radio.isChecked():
                result = self.translator.translate(
                    self.before_translation.toPlainText(), src='en', dest='ja'
                )
            else:
                result = self.translator.translate(
                    self.before_translation.toPlainText(), src='ja', dest='en'
                )
            self.after_translation_text.setText(result.text)
            self.after_translation_text.setReadOnly(True)
        else:
            self.after_translation_text.setText('')


app = QtWidgets.QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
