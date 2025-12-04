from agents.support.nodes.conversation.promp import SYSTEM_PROMP
from agents.support.state import State
from langchain.chat_models import init_chat_model

# LLM base SIN tools
llm = init_chat_model("openai:gpt-4.1-mini", temperature=0)


def conversation(state: State):
    new_state = {}

    # Historial y último mensaje del usuario
    history = state["messages"]
    last_message = history[-1]

    # Prompt: sistema + último mensaje del usuario
    messages = [
        ("system", SYSTEM_PROMP),
        ("user", last_message.content),  # .content es lo correcto acá
    ]

    # Llamada al modelo (sin tools)
    ai_message = llm.invoke(messages)

    # LangGraph se encarga de agregarlo al historial
    new_state["messages"] = [ai_message]
    return new_state
