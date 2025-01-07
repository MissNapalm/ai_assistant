# aria/utils/easter_eggs.py
import random

class EasterEggManager:
    def __init__(self):
        self.EASTER_EGGS = {
            "hello aria": [
                "Hi there! How can I help you today?",
                "Greetings! Ready to chat?",
                "Hello! What's on your mind?",
            ],
            "how are you": [
                "I'm doing great, thanks for asking!",
                "Feeling fantastic and ready to assist!",
                "Operational and excited to help you out!",
            ],
            "tell me a joke": [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "I told my computer I needed a break, and now it won't stop sending me Kit-Kat ads.",
                "Why do Python programmers wear glasses? Because they can't C.",
            ],
            # Add other easter eggs here
        }
    
    def get_response(self, text):
        """Check if the input text matches any Easter egg phrases."""
        text = text.lower().strip()
        
        if text in self.EASTER_EGGS:
            responses = self.EASTER_EGGS[text]
            return random.choice(responses) if isinstance(responses, list) else responses
            
        for phrase, response in self.EASTER_EGGS.items():
            if phrase in text:
                return random.choice(response) if isinstance(response, list) else response
                
        return None