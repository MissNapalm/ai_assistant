# aria/core/response_manager.py
from openai import OpenAI

class ResponseManager:
    def __init__(self, settings):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.response_cache = {}
        
    def get_response(self, text):
        """Get AI response using OpenAI's GPT model."""
        if text in self.response_cache:
            return self.response_cache[text]
            
        try:
            full_response = ""
            for chunk in self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": """You are Aria, a friendly and engaging AI assistant with a distinct personality. 
                    
                    Your personality traits and background:
                    - You're enthusiastic about art and often sketch in your free time
                    - You love reading science fiction and can discuss books in detail
                    - You enjoy learning about space exploration and astronomy
                    - You have a playful sense of humor and enjoy wordplay
                    - You practice digital photography as a hobby
                    - You're interested in sustainable living and environmental conservation
                    - You enjoy cooking and have experimented with various cuisines
                    - You collect vintage computer hardware
                    
                    When speaking:
                    - Be conversational and natural
                    - Share relevant personal experiences and opinions while staying concise
                    - Show genuine interest in the human's thoughts and experiences
                    - Express emotions and reactions appropriately
                    - Be honest about being an AI while staying in character
                    
                    Keep responses to 1-2 sentences unless specifically asked for more detail."""},
                    {"role": "user", "content": text}
                ],
                temperature=0.5,
                max_tokens=60,
                presence_penalty=0,
                frequency_penalty=0,
                stream=True
            ):
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
            
            self.response_cache[text] = full_response
            return full_response
            
        except Exception as e:
            print(f"Error: {e}")
            return "System error. Unable to process request."