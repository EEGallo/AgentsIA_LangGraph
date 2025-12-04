# OPCIÓN 1: Ollama (100% gratuito, local)
# Instalar: pip install langchain-ollama
# Luego ejecutar: ollama pull llama3.2 (o mistral, qwen2.5, etc.)

from langchain.agents import create_agent
from langchain_ollama import ChatOllama

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# Modelo gratuito usando Ollama (local)
model = ChatOllama(
    model="llama3.2",  # o "mistral", "qwen2.5", "phi3", etc.
    temperature=0.1,
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)