from langgraph.graph import MessagesState

class State(MessagesState):
    customer_name: str | None = None
    my_age: int | None = None
    phone: str | None = None
    age: int | None = None