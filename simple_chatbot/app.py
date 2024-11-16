from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def get_response(user_input):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", 
            "content": "You everything about the football history."},
            {"role": "user", 
            "content":user_input}
        ]
        )

    return completion.choices[0].message.content

def main():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("Ask Me: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot: ", response)


if __name__ == "__main__":
    main()