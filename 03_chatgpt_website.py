import openai
import gradio

#Joshua's API Key
openai.api_key = "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"

#load chat_history here
store_conversation = [
    "User: Good Morning",
    "User: Your Name Now is Anna",
    "User: Your Age is Now 25",
    "User: Your Favorite color is Pink",
    "User: Your Like video game",
]

def CustomChatGPT(user_input):
    store_conversation.append("User: " + user_input)
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = "\n".join(store_conversation)
    )
    ChatGPT_reply = response.choices[0].text.strip()
    store_conversation.append("AI: " + ChatGPT_reply)
    saveChatHistory(store_conversation)
    return ChatGPT_reply

def saveChatHistory(conversation):
    with open("chat_history.txt", "w") as file:
        file.write("\n".join(conversation))

# gradio
demo = gradio.Interface(
    fn = CustomChatGPT,
    inputs = "text",
    outputs = "text",
    title = "Chat With Your AI Waifu",
    description="Type a message to chat with the AI Waifu."
)

demo.launch(share = True)

