from app import app
import openai

openai.api_key = "sk-"

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/penguin')
def penguin():
    turbo = "gpt-3.5-turbo"
    davinci_text = "text-davinci-003"
    completion = openai.ChatCompletion.create(model=turbo, messages=[{"role": "user", "content":"Summarize the theory of relativity for a 5 year old"}])
    return completion.choices[0].message.content
