import os
from rapidfuzz import process


class Chatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "prelims": {
                "description": "Here are the available topics in the Preliminary Term:",
                "topics": {
                    "syntax": "Syntax refers to the rules that define the structure of a programming language.",
                    "variables": "Variables are containers for storing data values.",
                    "data types": "Data types specify the type of data a variable can hold (e.g., int, float, string).",
                },
            },
            "help": "I can help you with programming, topics on technology, or general questions. Type 'exit' to quit.",
            "exit": "Goodbye! Have a great day.",
        }
        self.fallback_message = "I'm sorry, I don't understand that. Can you try asking something else?"

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_best_match(self, user_input, choices):
        """Find the best match for user input from available choices."""
        match = process.extractOne(user_input, choices)
        return match if match and match[1] >= 60 else None

    def get_response(self, user_input):
        """Fetch response based on user input."""
        user_input = user_input.lower().strip()

        # Check for matches with main responses
        match = self.get_best_match(user_input, self.responses.keys())
        if match:
            match_key = match[0]
            response = self.responses.get(match_key)

            # Handle nested Prelims
            if match_key == "prelims":
                prelim_details = response
                description = prelim_details["description"]
                topics = "\n".join(f"- {topic}" for topic in prelim_details["topics"].keys())
                return f"{description}\n{topics}"

            return response

        # Check for subtopics under Prelims
        prelim_topics = self.responses["prelims"]["topics"]
        match = self.get_best_match(user_input, prelim_topics.keys())
        if match:
            match_key = match[0]
            return prelim_topics[match_key]

        # Fallback response
        return self.fallback_message

    def run(self):
        """Run the chatbot interaction loop."""
        print("Chatbot: Hello! Type 'help' to see what I can do. Type 'exit' to quit.")
        while True:
            user_input = input("\nYou: ").strip()
            self.clear_screen()  # Clear the screen
            if user_input.lower() == "exit":
                print("Chatbot:", self.responses["exit"])
                break
            response = self.get_response(user_input)
            print("Chatbot:", response)


# Run the chatbot
if __name__ == "__main__":
    bot = Chatbot()
    bot.run()