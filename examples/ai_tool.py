from openai import OpenAI
import json

from tool import get_stars
from bridge import ToolsBridge

get_stars = ToolsBridge.register()(get_stars)


def run():
    client = OpenAI(
        base_url="http://localhost:11434/v1",  # ollama_url
        api_key="Ignored",  # required
    )

    messages = [
        {
            "role": "user",
            "content": "How popular is the GitHub repository 'ollama/ollama'?",
        }
    ]
    tools = ToolsBridge.get_tools()

    completion = client.chat.completions.create(
        model="llama3.2",
        messages=messages,
        tools=tools,
    )

    tool_call = completion.choices[0].message.tool_calls[0]

    args = json.loads(tool_call.function.arguments)
    result = globals()[tool_call.function.name](**args)

    messages.append(completion.choices[0].message)
    messages.append(
        {"role": "tool", "tool_call_id": tool_call.id, "content": str(result)}
    )

    completion = client.chat.completions.create(
        model="llama3.2",
        messages=messages,
        tools=tools,
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    run()
