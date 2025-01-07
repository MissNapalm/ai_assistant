# aria/main.py
import sys
from PyQt5.QtWidgets import QApplication
from config.settings import Settings
from core.assistant import VoiceAssistant
from core.audio_manager import AudioManager
from core.response_manager import ResponseManager
from ui.main_window import MainWindow
from utils.easter_eggs import EasterEggManager
from utils.signal_emitter import SignalEmitter

def main():
    app = QApplication(sys.argv)
    
    # Initialize components
    settings = Settings()
    signal_emitter = SignalEmitter()
    
    audio_manager = AudioManager(settings, signal_emitter)
    response_manager = ResponseManager(settings)
    easter_egg_manager = EasterEggManager()
    
    assistant = VoiceAssistant(
        audio_manager,
        response_manager,
        easter_egg_manager,
        signal_emitter
    )
    
    # Create and show main window
    window = MainWindow(assistant, signal_emitter)
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()