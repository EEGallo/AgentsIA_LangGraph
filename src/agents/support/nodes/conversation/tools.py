from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Falta OPENAI_API_KEY en el entorno.")
    return OpenAI(api_key=api_key)


client = get_client()

# --- CREAMOS EL VECTOR STORE (DEMO: en cada arranque) ---
vs = client.vector_stores.create(name="curso-langgraph")
VECTOR_STORE_ID = vs.id

client.vector_stores.files.create(
    vector_store_id=VECTOR_STORE_ID,
    file_id="file-3LwQZkX4aAumM4dk2HBKsq",  # tu file_id
)

# --- DEFINIMOS LA TOOL DE FILE SEARCH ---
file_search_tool = {
    "type": "file_search",
}

tools = [file_search_tool]

tool_resources = {
    "file_search": {
        "vector_store_ids": [VECTOR_STORE_ID],
    }
}
