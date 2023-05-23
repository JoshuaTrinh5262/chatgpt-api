import openai
import gradio

openai.api_key = "####"

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def customChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.Completion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

def chatInterface(chat_log):
    return chat_log

# Read the contents of the chat log file
with open("chat_log.txt", "r") as file:
    chat_log = file.read()

demo = gradio.Interface(fn=customChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")
demo = gradio.Interface(fn=chatInterface, outputs = "text", title="Chat Log")

demo.launch(share = True)