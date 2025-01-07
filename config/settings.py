# aria/config/settings.py
import os
from dotenv import load_dotenv

class Settings:
   def __init__(self):
       load_dotenv()
       
       self.OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
       self.ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
       
       self.VOICE_SETTINGS = {
           "voice": "Glinda",
           "model": "eleven_monolingual_v1",
           "optimize_streaming_latency": 4,
           "voice_settings": {
               "stability": 0.5,
               "similarity_boost": 0.5,
               "style": 0.0,
               "use_speaker_boost": True,
           }
       }
       
       self.RECOGNIZER_SETTINGS = {
           "energy_threshold": 300,
           "pause_threshold": 1.2,      # Wait longer for pauses
           "phrase_threshold": 0.5,      # Allow longer phrases
           "non_speaking_duration": 1.0,  # Wait longer after speech ends
       }