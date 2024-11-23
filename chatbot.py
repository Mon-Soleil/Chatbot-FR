import time

class Chatbot:
    def __init__(self):
        # Dictionary-based responses
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "help": "I can help you with programming, topics on technology, or general questions.",
            "programming": "I can guide you on Python, JavaScript, or other programming topics. Which one would you like to discuss?",
            "python": "Python is a powerful programming language great for beginners and experts alike. Would you like to learn about data types, loops, or libraries?",
            "exit": "Goodbye! Have a great day.",
        
        }
        self.fallback_message = "I'm sorry, I don't understand that. Can you try asking something else?"

    def get_response(self, user_input):
        """Fetch response based on user input."""
        user_input = user_input.lower().strip()
        return self.responses.get(user_input, self.fallback_message)

    def run(self):
        """Run the chatbot interaction loop."""
        print("Chatbot: Hello! Type 'help' to see what I can do. Type 'exit' to quit.")
        while True:
            user_input = input("\nYou: ")
            if user_input.lower().strip() == "exit":
                print("Chatbot:", self.responses["exit"])
                break
            response = self.get_response(user_input)
            print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    bot = Chatbot()
    bot.run()