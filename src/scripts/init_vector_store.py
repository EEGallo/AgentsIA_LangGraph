# scripts/init_vector_store.py
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

vs = client.vector_stores.create(name="curso-langgraph")
print("Vector store ID:", vs.id)

client.vector_stores.files.create(
    vector_store_id=vs.id,
    file_id="file-3LwQZkX4aAumM4dk2HBKsq",
)

print("Archivo asociado correctamente.")
