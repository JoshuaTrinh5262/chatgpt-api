import openai
import gradio
import api

openai.api_key = "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"

# Open the text file in read mode
with open("chat_history.txt", "r") as file:
    # Read all lines from the file into a list
    lines = file.readlines()

#load chat_history here
store_conversation = [line.strip() for line in lines]

print(store_conversation)

def CustomChatGPT(user_input):
    store_conversation.append("User1: " + user_input)
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = "\n".join(store_conversation),
        max_tokens = 50,
        n = 1,
        stop = None,
        temperature = 0.5,
    )

    ChatGPT_reply = response.choices[0].text.strip()
    store_conversation.append(ChatGPT_reply)
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

