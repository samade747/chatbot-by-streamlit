from datetime import datetime
import json

class ChatHistory:
    def __init__(self):
        self.history = []
    
    def add_message(self, role, content):
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        self.history.append(message)
    
    def clear_history(self):
        self.history = []
    
    def get_history(self):
        return self.history
    
    def export_history(self, filename="chat_history.json"):
        with open(filename, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def import_history(self, filename="chat_history.json"):
        try:
            with open(filename, 'r') as f:
                self.history = json.load(f)
        except FileNotFoundError:
            self.history = [] 