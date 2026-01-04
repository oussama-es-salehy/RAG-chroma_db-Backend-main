from agents.prompt import SYSTEM_PROMPT
from services.rag_creation import load_chroma
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os

load_dotenv()

client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"])
)

MODEL = "openai/gpt-4.1"

db = load_chroma()

# === MEMORY ===
conversation_memory = []
MAX_MEMORY = 6  # 3 tours (user + assistant)

def rag_answer(question: str) -> str:
    global conversation_memory

    # Recherche contextuelle
    docs = db.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        SystemMessage(content=f"Retrieved context:\n{context}")
    ]

    # Ajouter la mémoire
    messages.extend(conversation_memory)

    # Nouveau message utilisateur
    user_msg = UserMessage(content=question)
    messages.append(user_msg)

    # Appel au modèle
    response = client.complete(
        model=MODEL,
        messages=messages,
        temperature=0.5,
    )

    answer = response.choices[0].message.content

    # Mise à jour de la mémoire
    conversation_memory.append(user_msg)
    conversation_memory.append(AssistantMessage(content=answer))

    # Limite mémoire
    if len(conversation_memory) > MAX_MEMORY:
        conversation_memory = conversation_memory[-MAX_MEMORY:]

    return answer

def get_conversation_serializable():
    """
    Convertit la mémoire en liste de dicts {'role': 'user/assistant', 'message': 'texte'}
    """
    serialized = []
    for msg in conversation_memory:
        if isinstance(msg, UserMessage):
            serialized.append({"role": "user", "message": msg.content})
        elif isinstance(msg, AssistantMessage):
            serialized.append({"role": "assistant", "message": msg.content})
    return serialized
