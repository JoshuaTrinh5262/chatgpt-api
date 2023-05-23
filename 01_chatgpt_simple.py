import openai

openai.api_key = "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"

messages = [{
    "role": "user",
    "content": "Give me 3 ideas for apps I could build with openai apis"
}]

prompt = "Give me 4 ideas for apps I could build with openai apis"

completion = openai.Completion.create(
    model = "text-davinci-003",
    prompt = prompt,
    max_tokens=500,
)
reply = completion.choices[0].text.strip()
print(reply)