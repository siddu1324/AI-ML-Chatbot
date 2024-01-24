class SimpleChatbot:
    def __init__(self):
        self.context = []
        self.questions_asked = 0

    def update_context(self, message):
        self.context.append(message)
        if len(self.context) > 10:  # Keep only the last 10 interactions
            self.context.pop(0)

    def greet(self):
        greeting = "Hello! I'm a simple chatbot. How can I help you today?"
        self.update_context(f"Bot: {greeting}")
        return greeting

    def farewell(self):
        farewell_message = "Goodbye! It was nice talking to you."
        self.update_context(f"Bot: {farewell_message}")
        return farewell_message

    def handle_question(self, question):
        self.update_context(f"User: {question}")
        response = ""
        if 'how are you' in question.lower():
            response = "I'm a bot, so I don't have feelings, but thanks for asking!"
        elif 'name' in question.lower():
            response = "I'm just a simple chatbot without a name."
        elif 'weather' in question.lower():
            response = "Sorry, I can't check current weather, but it's always sunny in the digital world!"
        elif 'time' in question.lower():
            response = "I can't tell the current time, but I'm here whenever you need me!"
        elif 'joke' in question.lower():
            response = "Why was the computer cold? It left its Windows open!"
        else:
            response = "I'm sorry, I don't understand that. Could you try asking something else?"
        self.update_context(f"Bot: {response}")
        return response

    def ask_question(self):
        question = ""
        self.questions_asked += 1
        if self.questions_asked == 1:
            question = "What's your name?"
        elif self.questions_asked == 2:
            question = "How are you doing today?"
        elif self.questions_asked == 3:
            question = "Do you like chatting with bots?"
        else:
            question = "I've asked my three questions. Do you have any questions for me?"
        self.update_context(f"Bot: {question}")
        return question

    def respond_to_answer(self, answer):
        self.update_context(f"User: {answer}")
        response = ""
        if self.questions_asked == 1:
            response = f"Nice to meet you, {answer}."
        elif self.questions_asked == 2:
            response = f"Glad to hear you're doing {answer}."
        elif self.questions_asked == 3:
            response = "It's great that you " + ("do" if "yes" in answer.lower() else "don't") + " like chatting with bots."
        self.update_context(f"Bot: {response}")
        return response

    def handle_error(self):
        error_message = "I'm not sure how to respond to that. Could you ask something else?"
        self.update_context(f"Bot: {error_message}")
        return error_message

    def recall_context(self):
        return " ".join(self.context)

# Main interaction loop
bot = SimpleChatbot()
print(bot.greet())

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "bye"]:
        print(bot.farewell())
        break

    # Check if bot has questions to ask
    elif bot.questions_asked < 3:
        print("Bot:", bot.respond_to_answer(user_input))
        print("Bot:", bot.ask_question())  # Ask the next question

    # Handle user's questions or statements
    else:
        print("Bot:", bot.handle_question(user_input))
