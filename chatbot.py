from flask import Flask, request, jsonify, render_template
from fuzzywuzzy import process

app = Flask(__name__)
# we first got a template from chatgpt for a chatbot that could is interactive

topics = {
    "Introduction to Programming": {
        "description": "Covers the basics of programming, including syntax, variables, and data types.",
        "subtopics": {
            "Syntax": "Syntax refers to the rules that define the structure of a programming language.",
            "Variables": "Variables are containers for storing data values.",
            "Data Types": "Data types specify the type of data a variable can hold (e.g., int, float, string)."
        }
    },
    "Computer Basics": {
        "description": "Explains the basic components and functioning of a computer.",
        "subtopics": {
            "Hardware": "The physical components of a computer, such as CPU, RAM, and storage.",
            "Software": "Programs and operating systems that run on computers.",
            "Operating Systems": "The software that manages hardware and software resources."
        }
    },
    "Problem Solving": {
        "description": "Focuses on techniques for solving computational problems.",
        "subtopics": {
            "Algorithms": "Step-by-step instructions to solve a problem.",
            "Flowcharts": "Diagrams that visually represent a process or algorithm.",
            "Pseudocode": "A plain-language description of the steps in an algorithm."
        }
    }
}

def find_best_match(user_message, choices):
    """Find the best match for the user message in the given choices."""
    match, score = process.extractOne(user_message, choices)
    return match if score > 60 else None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "").strip().lower()
    
    # Handle "topics" query
    if "topics" in user_message:
        topics_list = "\n".join(topics.keys())
        return jsonify({"response": f"Here are the available topics:\n{topics_list}"})

    # Match main topics
    topic_match = find_best_match(user_message, topics.keys())
    if topic_match:
        topic_details = topics[topic_match]
        description = topic_details["description"]
        subtopics = "\n".join(topic_details["subtopics"].keys())
        return jsonify({"response": f"{description}\nAvailable subtopics:\n{subtopics}"})
    
    # Match subtopics within each topic
    for topic, details in topics.items():
        subtopic_match = find_best_match(user_message, details["subtopics"].keys())
        if subtopic_match:
            subtopic_detail = details["subtopics"][subtopic_match]
            return jsonify({"response": f"{subtopic_match}: {subtopic_detail}"})
    
    # Fallback response
    return jsonify({"response": "I'm sorry, I don't understand your question. Try asking about programming, computer basics, or problem-solving."})

if __name__ == "__main__":
    app.run(debug=True)