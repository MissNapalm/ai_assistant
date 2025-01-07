# aria/ui/main_window.py
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QMouseEvent
from .components import ThinkingLabel, TranscriptionLabel, ChatArea, ListenButton
from .styles import StyleManager
import threading

class MainWindow(QMainWindow):
    def __init__(self, assistant, signal_emitter):
        super().__init__()
        self.assistant = assistant
        self.signal_emitter = signal_emitter
        self.style_manager = StyleManager()
        
        # Set up dragging variables
        self._dragging = False
        self._drag_start_position = QPoint()
        
        # Connect signals
        self.signal_emitter.update_text_signal.connect(self.update_chat)
        self.signal_emitter.transcribe_signal.connect(self.update_transcription)
        self.signal_emitter.thinking_signal.connect(self.update_thinking_indicator)
        self.signal_emitter.response_ready_signal.connect(self.display_response)
        
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Aria AI Assistant')
        self.setGeometry(100, 100, 800, 600)
        
        # Create main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Create UI components
        self.thinking_label = ThinkingLabel(self.style_manager)
        self.transcription_label = TranscriptionLabel(self.style_manager)
        self.chat_area = ChatArea(self.style_manager)
        self.listen_btn = ListenButton(self.style_manager)
        
        # Add components to layout
        main_layout.addWidget(self.thinking_label)
        main_layout.addWidget(self.transcription_label)
        main_layout.addWidget(self.chat_area)
        main_layout.addWidget(self.listen_btn)
        
        # Set up main widget
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        # Set window style
        self.setStyleSheet(self.style_manager.get_main_window_style())
        
        # Connect button click
        self.listen_btn.clicked.connect(self.start_listening)
        
        # Set up window properties
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setContentsMargins(10, 10, 10, 10)
    
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._dragging = True
            self._drag_start_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.LeftButton and self._dragging:
            self.move(event.globalPos() - self._drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._dragging = False
            event.accept()
    
    def update_thinking_indicator(self, is_thinking):
        if is_thinking:
            self.thinking_label.setText("Thinking...")
            self.thinking_label.show()
        else:
            self.thinking_label.hide()

    def display_response(self, text):
        self.update_chat(text, False)

    def update_transcription(self, text):
        self.transcription_label.setText(f"Transcription: {text}")

    def update_chat(self, text, is_user=True):
        self.chat_area.update_chat(text, is_user)

    def start_listening(self):
        self.listen_btn.setEnabled(False)
        threading.Thread(target=self.assistant.run, daemon=True).start()
        QTimer.singleShot(5000, lambda: self.listen_btn.setEnabled(True))