import os
from rapidfuzz import process

class Chatbot:
    def __init__(self):
        self.responses = {
            "hello": {
                "description": (
                    "Hi there! These are the available terms you can browse through:\n"
                    "- Prelims\n"
                    "- Midterms\n"
                    "- Semi-Finals Term\n"
                    "- Finals\n"
                    "Type 'exit' to exit the program or 'main menu' to return to this menu!"
                )
            },
            "prelims": {
                "description": "Here are the available topics in the Preliminary Term:",
                "topics": {
                    "syntax": {
                        "description": (
                            "Syntax refers to the rules that define the structure of a programming language.\n"
                            "Type 'syntax example' to see examples or 'main menu' to return to the main menu."
                        ),
                        "example": (
                            "Examples of syntax:\n"
                            "- input(): Requests for user input\n"
                            "- len(): Returns the length of an object\n"
                            "- min(), max(): Returns the minimum or maximum values\n"
                            "- round(): Rounds off numbers\n"
                            "- type(): Returns the variable type\n"
                            "Type 'exit' to exit the program or 'main menu' to return to this menu!"
                        ),
                    },
                    "variables": {
                        "description": (
                            "Variables are containers for storing data values.\n"
                            "Type 'variables example' to see examples or 'main menu' to return to the main menu."
                        ),
                        "example": (
                            "Example of variables:\n"
                            "x = 10\n"
                            "y = 'Hello'\n"
                            "print(x)\n"
                            "print(y)\n"
                            "Output:\n10\nHello"
                            "Type 'exit' to exit the program or 'main menu' to return to this menu!"
                        ),
                    },
                },
            },
            "midterms": {
                "description": "Here are the available topics in the Midterms Term:",
                "topics": {
                    "if else statement": {
                        "description": (
                            "The if-else statement is a decision-making statement that executes code based on specified conditions.\n"
                            "Type 'if else statement example' to see examples or 'main menu' to return to the main menu."
                        ),
                        "example": (
                            "Example of if-else statement:\n"
                            "x = 10\n"
                            "y = 20\n"
                            "if y > x:\n"
                            "    print('y is greater than x')\n"
                            "else:\n"
                            "    print('x is greater than y')\n"
                            "Output:\ny is greater than x\n"
                            "Type 'exit' to exit the program or 'main menu' to return to this menu!"
                        ),
                    },
                    "nested decision": {
                        "description": (
                            "Python's nested if-else statements allow you to test multiple conditions.\n"
                            "Type 'nested decision example' to see examples or 'main menu' to return to the main menu."
                        ),
                        "example": (
                            "Example of nested decision:\n"
                            "x = 10\n"
                            "if x > 5:\n"
                            "    if x < 15:\n"
                            "        print('x is between 5 and 15')\n"
                            "    else:\n"
                            "        print('x is 15 or more')\n"
                            "else:\n"
                            "    print('x is 5 or less')\n"
                            "Output:\nx is between 5 and 15\n\n"
                            "Type 'exit' to exit the program or 'main menu' to return to this menu!"
                        ),
                    },
                },
            },
            "semis": {
                "description": "Here are the available topics in the Semi-Final Term:",
                "topics": {
                    "loops": {
                        "description": (
                            "Loops allow you to execute a block of code multiple times.\n"
                            "Type 'loops example' to see examples or 'main menu' to return to the main menu."
                        ),
                        "example": (
                            "Example of a loop:\n"
                            "for i in range(3):\n"
                            "    print(i)\n"
                            "Output:\n0\n1\n2\n"
                            "Type 'exit' to exit the program or 'main menu' to return to this menu!"
                        ),
                    },
                    "lists": {
                        "description": (
                            "Lists are used to declare items, and you can add, remove, and change items in the list.\n"
                            "It uses brackets or [ ]\n\n"
                            "Type 'lists example' to see examples or 'main menu' to return to the main menu."
                        ),
                        "example": (
                            "Example of a list:\n"
                            "list = ['apple', 'banana']\n"
                            "print(list)\n\n"
                            "Output:\n['apple', 'banana']\n"
                            "Type 'exit' to exit the program or 'main menu' to return to this menu!"
                        ),
                    },
                    "dictionaries": {
                        "description": (
                            "Dictionaries store key-value pairs, and you use the key to find the corresponding value.\n"
                            "Dictionaries are also known as 'dict' and use curly brackets { }\n\n"
                            "Type 'dict example' to see examples or 'main menu' to return to this menu."
                        ),
                        "example": (
                            "Example of a dictionary:\n"
                            "student = {\n"
                            "    'name': 'Anna',\n"
                            "    'age': 21,\n"
                            "    'favorite_color': 'Blue'\n"
                            "}\n"
                            "print(student)\n\n"
                            "Output:\n{'name': 'Anna', 'age': 21, 'favorite_color': 'Blue'}\n"
                            "Type 'exit' to exit the program or 'main menu' to return to this menu!"
                        ),
                    },
                    "functions": {
                        "description": (
                            "Functions are reusable blocks of code that perform a specific task.\n"
                            "Type 'functions example' to see examples or 'main menu' to return to the main menu."
                        ),
                        "example": (
                            "Example of a function:\n"
                            "def greet(name):\n"
                            "    return f'Hello, {name}!'\n"
                            "print(greet('Alice'))\n"
                            "Output:\nHello, Alice!\n"
                            "Type 'exit' to exit the program or 'main menu' to return to this menu!"
                        ),
                    },
                },
            },
            "finals": {
                "description": "Here are the available topics in the Final Term:",
                "topics": {
                    "classes and objects": {
                        "description": (
                            "Classes and objects are the foundation of object-oriented programming.\n"
                            "Type 'classes and objects example' to see examples or 'main menu' to return to this menu."
                        ),
                        "example": (
                            "Example of a class and object:\n"
                            "class Person:\n"
                            "    def __init__(self, name, age):\n"
                            "        self.name = name\n"
                            "        self.age = age\n\n"
                            "    def greet(self):\n"
                            "        return f'Hi, I am {self.name}, and I am {self.age} years old.'\n\n"
                            "person = Person('Alice', 25)\n"
                            "print(person.greet())\n"
                            "Output:\nHi, I am Alice, and I am 25 years old.\n"
                            "Type 'exit' to exit the program or 'main menu' to return to this menu!"
                        ),
                    },
                },
            },
            "exit": "Goodbye! Have a great day.",
        }
        self.fallback_message = "I'm sorry, I don't understand that. Can you try asking something else?"

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def get_best_match(self, user_input, choices):
        match = process.extractOne(user_input, choices)
        if match and match[1] >= 60:
            return match[0]
        return None

    def get_response(self, user_input):
        user_input = user_input.lower().strip()

        # Handle returning to the main menu
        if user_input == "main menu":
            return self.responses["hello"]["description"]

        # Handle "example" queries correctly
        if "example" in user_input:
            # Check all sections and topics for 'example' and match the term
            for section_key in self.responses.keys():
                if section_key in ["prelims", "midterms", "semis", "finals"]:
                    topics = self.responses[section_key].get("topics", {})
                    for topic_key, topic_data in topics.items():
                        if topic_key in user_input:
                            return topic_data.get("example", self.fallback_message)

        # Try to match with the main sections like prelims, midterms, etc.
        match = self.get_best_match(user_input, self.responses.keys())
        if match:
            match_key = match
            if match_key in {"prelims", "midterms", "semis", "finals"}:
                return self.get_topic_response(match_key)
            return self.responses[match_key]["description"]

        # Check for subtopics and examples in all sections
        for section in ["prelims", "midterms", "semis", "finals"]:
            topics = self.responses[section].get("topics", {})
            match = self.get_best_match(user_input, topics.keys())
            if match:
                topic_key = match
                if "example" in user_input:
                    return topics[topic_key].get("example", "No example available.")
                return topics[topic_key].get("description", "")

        return self.fallback_message

    def get_topic_response(self, section_key):
        """Handle sections with nested topics like Prelims, Midterms, Semis, and Finals."""
        section_details = self.responses.get(section_key, {})
        description = section_details.get("description", "No description available.")
        topics = section_details.get("topics", {})
        if topics:
            topic_list = "\n".join(f"- {topic}" for topic in topics.keys())
            return f"{description}\n{topic_list}"
        return f"{description}\n(No topics available.)"

    def run(self):
        print("Chatbot:", self.responses["hello"]["description"])
        while True:
            user_input = input("\nYou: ").strip()
            self.clear_screen()
            if user_input.lower() == "exit":
                print("Chatbot:", self.responses["exit"])
                break
            response = self.get_response(user_input)
            print("Chatbot:", response)


# Run the chatbot
if __name__ == "__main__":
    try:
        bot = Chatbot()
        bot.run()
    except KeyboardInterrupt:
        print("\nChatbot: Program interrupted. Goodbye!")
    except Exception as e:
        print(f"Chatbot encountered an error: {e}")