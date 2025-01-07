# aria/core/audio_manager.py
import speech_recognition as sr
import subprocess
import os
import threading
from elevenlabs.client import ElevenLabs

class AudioManager:
    def __init__(self, settings, signal_emitter):
        self.settings = settings
        self.signal_emitter = signal_emitter
        self.eleven = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
        
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True
        
        for key, value in settings.RECOGNIZER_SETTINGS.items():
            setattr(self.recognizer, key, value)
        
        self.is_speaking = False
    
    def listen_for_speech(self, source, timeout=10, phrase_time_limit=10):
        """Listen for speech input using the speech recognizer."""
        return self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    
    def transcribe_audio(self, audio):
        """Transcribe audio to text using Google Speech Recognition."""
        return self.recognizer.recognize_google(audio).lower()
    
    def speak(self, text):
        """Generate and play speech from text using ElevenLabs."""
        if self.is_speaking:
            return
            
        try:
            self.is_speaking = True
            
            def generate_and_play():
                try:
                    audio = self.eleven.generate(
                        text=text,
                        **self.settings.VOICE_SETTINGS
                    )
                    
                    with open("temp_audio.mp3", "wb") as f:
                        for chunk in audio:
                            f.write(chunk)
                    
                    self.signal_emitter.thinking_signal.emit(False)
                    self.signal_emitter.response_ready_signal.emit(text)
                    subprocess.run(['afplay', 'temp_audio.mp3'], check=True)
                    
                finally:
                    if os.path.exists("temp_audio.mp3"):
                        os.remove("temp_audio.mp3")
                    self.is_speaking = False
            
            threading.Thread(target=generate_and_play, daemon=True).start()
            
        except Exception as e:
            print(f"Speaking error: {e}")
            self.is_speaking = False