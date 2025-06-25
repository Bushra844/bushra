class Chatbot:
    """A simple object-oriented chatbot."""

    def __init__(self, name, knowledge_base=None):
        self.name = name 
        self.knowledge_base = knowledge_base or {}  # Dictionary for storing knowledge

    def learn(self, question, answer):
        """Adds a question-answer pair to the chatbot's knowledge."""
        self.knowledge_base[question.lower()] = answer
        print(f"{self.name} learned: '{question}' -> '{answer}'")

    def respond(self, user_input):
        """Generates a response to user input."""
        user_input_lower = user_input.lower()
        if user_input_lower in self.knowledge_base:
            return self.knowledge_base[user_input_lower]
        else:
            return "I don't understand. Can you teach me?"

    def chat(self):
        """Starts a conversation with the user."""
        print(f"Hi, I'm {self.name}. Ask me anything!")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print(f"{self.name}: Goodbye!")
                break
            response = self.respond(user_input)
            print(f"{self.name}: {response}")
            if response == "I don't understand. Can you teach me?":
                answer = input("Teach me: ")
                self.learn(user_input, answer)

# Example usage
chatbot = Chatbot("Bot")

# Initial knowledge
chatbot.learn("What is your name?", "My name is Bot.")
chatbot.learn("How are you?", "I'm doing well, thank you!")

chatbot.chat()
