import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)
import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)
from PyQt5.QtGui import QIcon
import sys
import json
import subprocess
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
CREATE_NO_WINDOW = 134217728
current_lang = 'en'

class WorkerThread(QThread):
    log_signal = pyqtSignal(str)

    def __init__(self, lang_dict):
        super().__init__()
        self.lang_dict = lang_dict

    def tr(self, key):
        return self.lang_dict.get(current_lang, {}).get(key, f'[{key}]')

    def run(self):
        self.log_signal.emit(f"\n{self.tr('log_start')}")
        try:
            result = subprocess.run(['tasklist'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=CREATE_NO_WINDOW)
            if 'RuntimeBroker.exe' not in result.stdout:
                self.log_signal.emit(self.tr('log_none'))
                return
            kill_result = subprocess.run(['taskkill', '/f', '/im', 'RuntimeBroker.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=CREATE_NO_WINDOW)
            for line in kill_result.stdout.splitlines():
                if '成功' in line or 'success' in line.lower():
                    self.log_signal.emit(f"<span style='color:#88ff88'>{line}</span>")
                elif '錯誤' in line or 'error' in line.lower():
                    self.log_signal.emit(f"<span style='color:#ff6666'>{line}</span>")
            self.log_signal.emit(self.tr('log_done'))
        except Exception as e:
            self.log_signal.emit(f"{self.tr('log_error')} {e}")

class RuntimeBrokerManager(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__), 'icon.ico')))
        self.setStyleSheet(qss)

        def get_resource_path(filename):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, filename)
            return os.path.join(os.path.abspath('.'), filename)
        lang_path = get_resource_path('lang.json')
        with open(lang_path, 'r', encoding='utf-8') as f:
            self.lang_dict = json.load(f)
        language_names = {'en': 'English', 'zh': '中文（繁體）', 'ja': '日本語', 'ko': '한국어', 'es': 'Español', 'fr': 'Français', 'de': 'Deutsch', 'it': 'Italiano', 'pt': 'Português', 'ru': 'Русский', 'vi': 'Tiếng Việt', 'th': 'ไทย', 'pl': 'Polski', 'nl': 'Nederlands', 'sv': 'Svenska', 'da': 'Dansk', 'no': 'Norsk', 'cs': 'Čeština', 'tr': 'Türkçe', 'id': 'Bahasa Indonesia', 'ms': 'Bahasa Melayu', 'uk': 'Українська'}
        self.language_selector = QComboBox()
        for code in self.lang_dict:
            display_name = language_names.get(code, code.upper())
            self.language_selector.addItem(display_name, code)
        global current_lang
        default_lang = 'en'
        index = self.language_selector.findData(default_lang)
        if index != -1:
            self.language_selector.setCurrentIndex(index)
            current_lang = default_lang
        self.language_selector.currentIndexChanged.connect(self.change_language)
        self.label = QLabel(self.tr_text('label'))
        self.button = QPushButton(self.tr_text('button'))
        self.button.clicked.connect(self.kill_runtime_broker)
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout = QVBoxLayout()
        layout.addWidget(self.language_selector)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.log)
        self.setLayout(layout)
        self.setWindowTitle(self.tr_text('title'))
        self.resize(600, 420)

    def tr_text(self, key):
        return self.lang_dict.get(current_lang, {}).get(key, f'[{key}]')

    def change_language(self):
        global current_lang
        current_lang = self.language_selector.currentData()
        self.refresh_ui()

    def refresh_ui(self):
        self.setWindowTitle(self.tr_text('title'))
        self.label.setText(self.tr_text('label'))
        self.button.setText(self.tr_text('button'))

    def kill_runtime_broker(self):
        self.button.setEnabled(False)
        self.worker = WorkerThread(self.lang_dict)
        self.worker.log_signal.connect(self.log.append)
        self.worker.finished.connect(lambda: self.button.setEnabled(True))
        self.worker.start()
qss = '\nQWidget {\n    background-color: #1e1e2f;\n    color: #ffffff;\n    font-family: "Segoe UI";\n    font-size: 11pt;\n}\nQPushButton {\n    background-color: #3a3f58;\n    color: white;\n    border: 1px solid #7aa2f7;\n    border-radius: 8px;\n    padding: 8px 16px;\n}\nQPushButton:hover {\n    background-color: #5b6b91;\n}\nQTextEdit {\n    background-color: #2b3045;\n    color: #d0d8f0;\n    border: 1px solid #4c5a78;\n    border-radius: 6px;\n    padding: 6px;\n}\nQLabel {\n    font-size: 13pt;\n    font-weight: bold;\n    margin-bottom: 8px;\n}\nQComboBox {\n    background-color: #2b3045;\n    color: #ffffff;\n    border: 1px solid #4c5a78;\n    border-radius: 6px;\n    padding: 6px;\n}\n'
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RuntimeBrokerManager()
    win.show()
    sys.exit(app.exec_())