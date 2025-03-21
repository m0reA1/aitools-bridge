<h1 align="center">
  <a href="https://github.com/m0reA1/aitools-bridge">
    <img src="docs/images/logo.svg" alt="Logo" height="256">
  </a>
</h1>

<div align="center">
  <b>AITools Bridge</b>
  <br />
  <br />
  <a href="https://github.com/m0reA1/aitools-bridge/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/m0reA1/aitools-bridge/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  ·
  <a href="https://github.com/m0reA1/aitools-bridge/discussions">Ask a Question</a>
</div>

<div align="center">
<br />

[![license](https://img.shields.io/github/license/m0reA1/aitools-bridge)](LICENSE) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/m0reA1/aitools-bridge/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) [![made with hearth by ](https://img.shields.io/badge/made%20with%20%E2%99%A5%20by-m0reA1-ff1414.svg?style=flat-square)](https://github.com/m0reA1)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
- [Getting Started](#getting-started)
  - [Usage](#usage)
- [Example](#example)
  - [Prerequisites](#prerequisites)
- [Development](#development)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Citation](#citation)
- [Contacts](#contacts)

</details>

---

## About

<table>
<tr>
<td>

<b>aitools-bridge</b> is a minimalist framework (or a decorator) designed to seamlessly integrate existing tools with the advanced AI ecosystem. The goal is to make it easier for users to wrap [AI-compatible functions](https://platform.openai.com/docs/guides/function-calling). As an adaptive _bridge_, it brings current tools into the AI era while expanding the capabilities of AI.

</td>
</tr>
</table>

![preview](docs/images/preview.svg)

## Getting Started

### Usage

1. Install

```sh
pip install aitools-bridge
```

2. Find any function you want to integrate with AI and make a small change

_if your function has a complete docstring, following [Google](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings), [NumPy](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard), or [Sphinx](https://www.sphinx-doc.org/en/master/index.html) style._

```python
from bridge import ToolsBridge

@ToolsBridge.register()
def get_weather(location: str):
    """Get current temperature for a given location.

    Args:
        location: City and country e.g. Bogotá, Colombia
    """
    pass
```

_if not, please use args: <u>description</u> & <u>param_descriptions</u>._

```python
from bridge import ToolsBridge

@ToolsBridge.register(
  description="Get current temperature for a given location",
  param_descriptions={
    "location": "City and country e.g. Bogotá, Colombia"
  }
)
def get_weather(location: str):
    pass
```

3. Export the tools to AI API and enjoy the experience!

```python
completion = openai.OpenAI().chat.completions.create(
  ...
  tools=ToolsBridge.get_tools(),
)

print(completion.choices[0].message.tool_calls)
```
<u>output</u>
```json
[{
    "id": "call_*",
    "type": "function",
    "function": {
        "name": "get_weather",
        "arguments": "{\"location\":\"Paris, France\"}"
    }
}]
```

## Example

### Prerequisites

Make sure you have installed both [Poetry](https://python-poetry.org/) and [Ollama](https://ollama.com/).

```sh
poetry -V

ollama list
```

1. Install dependencies

```sh
make sync
```

2. Run examples
   
```sh
make examples
```

![examples](docs/images/examples.svg)

>**tool.py** is just an ordinary Python function. However, after adding _ToolsBridge.register_, this function evolves into an AI tool (**ai_tool.py**) that can be passed to an LLM for collaborative processing, allowing it to demonstrate its capabilities (or intelligence) in the right context. This transforms it from a pure code-level function call into an interactive conversation between humans and AI. Instead of merely returning a function output, the user receives meaningful answers.

## Development

This project welcomes contributions and suggestions. Before making any changes, please follow the steps below

```sh
make sync

make tests  # tests
make format # formatter
make lint   # linter
```

## License

This project is licensed under the **Apache License V2.0**. See [LICENSE](LICENSE) for more information.

## Acknowledgements

​A special thanks to these outstanding open-source community.

- [OpenAI](https://github.com/openai)
- [Meta Llama](https://github.com/meta-llama)
- [Ollama](https://github.com/ollama)
- [pydantic](https://github.com/pydantic/pydantic)
- [poetry](https://github.com/python-poetry/poetry)

## Citation

If you use [**aitools-bridge**](https://github.com/m0reA1/aitools-bridge) in your project, please cite:

```bibtex
@software{aitools-bridge2025,
  author = {m0reA1},
  title = {aitools-bridge: a minimalist framework designed to seamlessly integrate existing tools with the advanced AI ecosystem},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/m0reA1/aitools-bridge}
}
```

## Contacts

If you have any questions, please contact us at [more.aitools@gmail.com](more.aitools@gmail.com).
