# aria/config/settings.py
import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        load_dotenv()
        
        self.OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        self.ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
        
        self.VOICE_SETTINGS = {
            "voice": "Daniel",
            "model": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.75,
                "similarity_boost": 0.75,
                "style": 0.0,
                "use_speaker_boost": True,
            }
        }
        
        self.RECOGNIZER_SETTINGS = {
            "energy_threshold": 300,
            "pause_threshold": 0.8,
            "phrase_threshold": 0.3,
            "non_speaking_duration": 0.5
        }