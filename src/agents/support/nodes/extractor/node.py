from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

from agents.support.state import State
from agents.support.nodes.extractor.promp import SYSTEM_PROMP

#Definimos el LLM
class ContactInfo(BaseModel):
    """Contact information for a person."""

    name: str | None = Field(default=None, description="The name of the person")
    email: str | None = Field(default=None, description="The email address of the person")
    phone: str | None = Field(default=None, description="The phone number of the person")
    age: int | None = Field(default=None, description="The age of the person in years")

llm = init_chat_model("openai:gpt-4o", temperature=0)
llm = llm.with_structured_output(ContactInfo)


#Definimos el nodo
def extractor(state: State):
    history = state["messages"]
    customer_name = state.get("customer_name", None)
    new_state = {}
    if customer_name is None or len(history) >= 10:
        schema = llm.invoke([("system", SYSTEM_PROMP)] +  history)
        new_state["customer_name"] = schema.name
        new_state["phone"] = schema.phone
        new_state["age"] = schema.age
    return new_state