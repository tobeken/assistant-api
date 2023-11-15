import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key= os.environ["OPENAI_API_KEY"]

assistant = openai.beta.assistants.create(
    name="UXデザイナー",
    instructions="あなたはUXデザイナーです．シンプルなペルソナを作ることができます",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

thread = openai.beta.threads.create()
# print(thread)



while True:

    message = openai.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=input("入力してください:")
)
    run = openai.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    )

    status ="queued"

    while status != "completed":
        run = openai.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
        )
        status = run.status

    messages = openai.beta.threads.messages.list(
        thread_id=thread.id,
        
    )

    for message in reversed(messages.data):
        print(message.role +": " + message.content[0].text.value)
