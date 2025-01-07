# aria/ui/styles.py
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class StyleManager:
    @staticmethod
    def get_main_window_style():
        return """
        QMainWindow {
            background-color: #000C1F;
            color: #00FFFF;
        }
        """
    
    @staticmethod
    def get_thinking_label_style():
        return """
        color: #00FFFF;
        font-size: 18px;
        font-weight: bold;
        background-color: rgba(0, 30, 60, 0.8);
        border: 2px solid #00FFFF;
        border-radius: 10px;
        padding: 15px;
        margin: 0 50px;
        text-align: center;
        """
    
    @staticmethod
    def get_transcription_label_style():
        return """
        color: #00BFFF;
        font-size: 14px;
        padding: 10px;
        font-weight: bold;
        background-color: rgba(0, 20, 40, 0.5);
        border-radius: 5px;
        """
    
    @staticmethod
    def get_chat_area_style():
        return """
        QTextEdit {
            background-color: #001020;
            color: #00FFFF;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 14px;
            border: 2px solid #00BFFF;
            border-radius: 10px;
            padding: 15px;
        }
        QScrollBar:vertical {
            background-color: rgba(0, 30, 60, 0.5);
            width: 15px;
            margin: 15px 0 15px 0;
            border-radius: 7px;
        }
        QScrollBar::handle:vertical {
            background-color: #00BFFF;
            min-height: 20px;
            border-radius: 7px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0;
        }
        """
    
    @staticmethod
    def get_button_style():
        return """
        QPushButton {
            background-color: rgba(0, 30, 60, 0.8);
            color: #00FFFF;
            border: 2px solid #00BFFF;
            border-radius: 10px;
            padding: 12px;
            font-size: 16px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        QPushButton:hover {
            background-color: rgba(0, 50, 100, 0.9);
            border-color: white;
        }
        QPushButton:pressed {
            background-color: rgba(0, 20, 40, 0.9);
        }
        """