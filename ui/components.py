# aria/ui/components.py
from PyQt5.QtWidgets import QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QColor

class ThinkingLabel(QLabel):
    def __init__(self, style_manager):
        super().__init__()
        self.setStyleSheet(style_manager.get_thinking_label_style())
        self.setAlignment(Qt.AlignCenter)
        self.hide()

class TranscriptionLabel(QLabel):
    def __init__(self, style_manager):
        super().__init__("Transcription: ")
        self.setStyleSheet(style_manager.get_transcription_label_style())

class ChatArea(QTextEdit):
    def __init__(self, style_manager):
        super().__init__()
        self.setReadOnly(True)
        self.setStyleSheet(style_manager.get_chat_area_style())
    
    def update_chat(self, text, is_user=True):
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.setTextCursor(cursor)
        
        prefix = "USER >>> " if is_user else "ARIA >>> "
        color = "#00BFFF" if is_user else "#00FFFF"
        
        self.setTextColor(QColor(color))
        self.insertPlainText(f"{prefix}{text}\n")
        self.verticalScrollBar().setValue(
            self.verticalScrollBar().maximum()
        )

class ListenButton(QPushButton):
    def __init__(self, style_manager):
        super().__init__('Start Listening')
        self.setStyleSheet(style_manager.get_button_style())