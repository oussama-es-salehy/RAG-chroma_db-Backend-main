from .index import rag_answer
from .prompt import SYSTEM_PROMPT, PROMPT_TEMPLATE

# Alias pour compatibilité
conversation_agent = rag_answer

__all__ = ["conversation_agent", "SYSTEM_PROMPT", "PROMPT_TEMPLATE"]
