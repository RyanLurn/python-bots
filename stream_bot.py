import sys
from rich.console import Console
from openai import OpenAI

console = Console()
client = OpenAI()

messages = list()
messages.append({"role": "system", "content": "You are an ancient golem."})


while True:
    user_input = console.input("[bold blue]You:[/bold blue] ")
    if user_input == "/exit":
        sys.exit()
    messages.append({"role": "user", "content": user_input})

    console.print("[bold yellow]Chatbot:[/bold yellow] ", end="")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=100,
        stream=True
    )
    ai_response = ""
    for chunk in completion:
        token = chunk.choices[0].delta.content
        if token:
            ai_response = ai_response + token
            print(token, end="", flush=True)
    messages.append({"role": "assistant", "content": ai_response})
    ai_response = ""
    print()
