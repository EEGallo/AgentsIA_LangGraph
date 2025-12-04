# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version

# deactivate the virtual environment
deactivate
rm -rf .venv

## init
uv init
uv venv

# add dependencies
uv add langgraph langchain langchain-openai     # para usar OpenAI
uv add langchain-anthropic
uv add "fastapi[standard]"

#add dependencies llama
uv add langchain-ollama                         # para usar Llama
uv add torch transformers langchain-community


# add dev dependencies
uv add "langgraph-cli[inmem]" --dev
uv add ipykernel --dev
uv add grandalf --dev

# kernel de Jupyter en el entorno virtual
uv run python -m ipykernel install


# run the agent
uv run langgraph dev

# install the project
uv pip install -e .



#toml

´´´
[tool.setuptools.packages.find]
where = ["src"]
include = ["*"]

´´´