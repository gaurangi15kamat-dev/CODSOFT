import random

def simple_chatbot():
    print("Hello! I am a simple chatbot. Let's have a conversation. Type 'exit' to end the chat. ")
while True:
    user_input=input("You: ")
    if user_input.lower()=="exit":
        print("Goodbye!")
        break
    if "hello" in user_input.lower():
        print("Chatbot: Hi there!")
    elif "how are you" in user_input.lower():
        print("Chatbot: I'm just a program, but I'm doing well, thanks for asking!")
    elif "your name" in user_input.lower():
        print("Chatbot: My name is Chatbot. Nice to meet you!")
    elif "weather" in user_input.lower():
        print("Chatbot: I can't check live weather yet, but it's always a good idea to carry an umbrella!")
    elif "time" in user_input.lower():
        from datetime import datetime
        now = datetime.now()
        print("Chatbot: Current time is", now.strftime("%H:%M:%S"))
    elif "are you human" in user_input.lower():
        print("Chatbot: No, I'm just a simple chatbot!")
    elif "Can you help me learn something new?" in user_input.lower():
        print("Chatbot: Absolutely! I can help with a wide variety of topics, including academic help, fun facts, or " \
        "providing summaries on topics like science, history, or tech.")
    else:
        responses=["Interesting!","Tell me more.","I'm not sure I understand.","How does that make you feel?"]
        random_response=random.choice(responses)
        print(f"Chatbot: {random_response}")
if __name__=="__main__":
    simple_chatbot()
    
