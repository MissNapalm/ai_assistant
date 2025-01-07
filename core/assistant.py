# aria/core/assistant.py
import threading
import time
import speech_recognition as sr
import math

class VoiceAssistant:
   def __init__(self, audio_manager, response_manager, easter_egg_manager, signal_emitter):
       self.audio_manager = audio_manager
       self.response_manager = response_manager
       self.easter_egg_manager = easter_egg_manager
       self.signal_emitter = signal_emitter
       
       self.is_listening = False
       self.stop_listening = threading.Event()
       self.last_speech_time = 0
       self.cooldown_period = 2.0
       self.last_processed_text = None
       self.last_speech_content = None

   def process_audio(self, audio):
       try:
           # Don't process if the system is speaking or in cooldown
           current_time = time.time()
           if self.audio_manager.is_speaking or (current_time - self.last_speech_time) < self.cooldown_period:
               return
               
           text = None
           for _ in range(3):
               try:
                   text = self.audio_manager.transcribe_audio(audio)
                   break
               except sr.UnknownValueError:
                   time.sleep(0.1)
           
           if not text:
               return
               
           # Prevent processing duplicate inputs or self-echo
           if text == self.last_processed_text:
               return
               
           # Skip if text matches recent assistant response
           if self.last_speech_content and text.lower() in self.last_speech_content.lower():
               return

           self.last_processed_text = text
           self.signal_emitter.transcribe_signal.emit(text)
           self.signal_emitter.update_text_signal.emit(text, True)
           
           if text == "exit":
               self.audio_manager.speak("Shutting down. Goodbye.")
               self.stop_listening.set()
               return
           
           easter_egg = self.easter_egg_manager.get_response(text)
           if easter_egg:
               self.audio_manager.speak(easter_egg)
               self.last_speech_time = time.time()
               self.last_speech_content = easter_egg
               return
           
           response = self.response_manager.get_response(text)
           self.audio_manager.speak(response)
           self.last_speech_time = time.time()
           self.last_speech_content = response
           
       except Exception as e:
           print(f"Processing error: {e}")
       finally:
           self.is_listening = False

   def run(self):
       self.signal_emitter.listening_signal.emit(True)
       self.audio_manager.speak("Initializing Aria system. Ready for input.")
       self.last_speech_time = time.time()
       self.stop_listening.clear()
       
       while not self.stop_listening.is_set():
           try:
               with sr.Microphone() as source:
                   self.audio_manager.recognizer.adjust_for_ambient_noise(source, duration=1.0)
                   
                   while self.audio_manager.is_speaking:
                       time.sleep(0.1)
                   
                   self.is_listening = True
                   self.signal_emitter.listening_signal.emit(True)
                   
                   try:
                       audio = self.audio_manager.listen_for_speech(source)
                       threading.Thread(
                           target=self.process_audio,
                           args=(audio,),
                           daemon=True
                       ).start()
                   
                   except sr.WaitTimeoutError:
                       self.is_listening = False
           
           except Exception as e:
               print(f"Listening error: {e}")
               self.is_listening = False
               time.sleep(0.1)