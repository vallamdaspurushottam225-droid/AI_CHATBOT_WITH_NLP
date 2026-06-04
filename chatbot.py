import nltk
from nltk.tokenize import word_tokenize

# Download NLTK tokenizer data
nltk.download('punkt')
nltk.download('punkt_tab')

# Chatbot responses
responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello!",
    "name": "I am an AI chatbot.",
    "python": "Python is a programming language.",
    "ai": "AI means Artificial Intelligence.",
    "nlp": "NLP stands for Natural Language Processing.",
    "bye": "Goodbye!"
}

# Starting message
print("================================")
print("     AI CHATBOT WITH NLP")
print("================================")
print("Type 'bye' to stop the chatbot")

# Chatbot loop
while True:

    # User input
    user_input = input("\nYou: ").lower()

    # Tokenizing words
    words = word_tokenize(user_input)

    # Exit condition
    if "bye" in words:
        print("Bot:", responses["bye"])
        break

    response_found = False

    # Checking keywords
    for keyword in responses:

        if keyword in words:

            print("Bot:", responses[keyword])

            response_found = True
            break

    # Default response
    if not response_found:
        print("Bot: Sorry, I am still learning.")