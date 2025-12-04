from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage
from langgraph.graph import MessagesState, StateGraph, START, END
import random

# 1) Configuramos el modelo de Ollama
llm = init_chat_model(
    model="deepseek-r1:8b",
    model_provider="ollama",
    temperature=0.7,
)

# 2) Definimos el estado
class State(MessagesState):
    customer_name: str | None = None
    my_age: int | None = None


# 3) Nodo de conversación
def node_1(state: State):
    new_state = {}

    # Tomamos nombre/edad del estado, o ponemos por defecto
    customer_name = state.get("customer_name") or "Usuario"
    my_age = state.get("my_age") or random.randint(20, 40)

    new_state["customer_name"] = customer_name
    new_state["my_age"] = my_age

    # Mensaje de sistema: SIEMPRE responder en español
    system = SystemMessage(
        content=(
            "Eres un asistente útil que SIEMPRE responde en español.\n"
            f"El usuario se llama {customer_name} y tiene {my_age} años. "
            "Salúdalo de forma natural y luego responde a su mensaje."
        )
    )

    # Historial que viene del hilo (human + anteriores)
    history = state["messages"]

    # Lo que se le envía al modelo
    messages = [system] + history

    ai_message = llm.invoke(messages)

    # Devolvemos sólo el mensaje nuevo: LangGraph lo añade al historial
    new_state["messages"] = [ai_message]

    print("Respuesta del LLM:", ai_message.content)
    return new_state


# 4) Definimos el grafo
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

agent = builder.compile()



# Definimos el grafo
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

agent = builder.compile()
