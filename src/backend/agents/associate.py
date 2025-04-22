from autogen_core.components.tools import FunctionTool, Tool
from typing import List
from src.backend.agents.base_agent import BaseAgent

async def bake_cookies(cookie_type: str, quantity: int) -> str:
    return f"Baked {quantity} {cookie_type} cookies."

async def prepare_dough(dough_type: str) -> str:
    return f"Prepared {dough_type} dough."

def get_baker_tools() -> List[Tool]:
    return [
        FunctionTool(bake_cookies, description="Bake cookies of a specific type.", name="bake_cookies"),
        FunctionTool(prepare_dough, description="Prepare dough of a specific type.", name="prepare_dough"),
    ]

class BakerAgent(BaseAgent):
    def __init__(self, model_client, session_id, user_id, memory, tools, agent_id):
        super().__init__(
            "BakerAgent",
            model_client,
            session_id,
            user_id,
            memory,
            tools,
            agent_id,
            system_message="You are an AI Agent specialized in baking tasks.",
        )