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

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=100
    )
    ai_response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_response})
    console.print(f"[bold yellow]Chatbot:[/bold yellow] {ai_response}")
