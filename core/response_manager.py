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
                    {"role": "system", "content": "You are Aria, a concise AI assistant. Always respond in 1-2 sentences maximum, even for complex questions. Never use lists or bullet points."},
                    {"role": "user", "content": text}
                ],
                stream=True,
                max_tokens=100
            ):
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
            
            self.response_cache[text] = full_response
            return full_response
            
        except Exception as e:
            print(f"Error: {e}")
            return "System error. Unable to process request."