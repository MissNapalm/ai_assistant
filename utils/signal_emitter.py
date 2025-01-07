# aria/utils/signal_emitter.py
from PyQt5.QtCore import QObject, pyqtSignal

class SignalEmitter(QObject):
    update_text_signal = pyqtSignal(str, bool)
    listening_signal = pyqtSignal(bool)
    thinking_signal = pyqtSignal(bool)
    transcribe_signal = pyqtSignal(str)
    response_ready_signal = pyqtSignal(str)