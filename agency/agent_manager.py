import openai
import os
from typing import List
from agency import Agent 
from dotenv import load_dotenv
load_dotenv(verbose=True)

openai.api_key = os.environ["OPENAI_API_KEY"]

class AgentManager:
    def __init__(self):
        self.agents = []

    def add_agent(self, role: str, name: str):
        agent = Agent(role, name)
        self.agents.append(agent)

    def generate_response(self, agent_index: int, messages: List[dict], model="gpt-3.5-turbo", stop_phrases=None) -> str:
        agent = self.agents[agent_index]
        #messages.append({"role": "system", "content": agent.role, "name": agent.name})

        response = openai.ChatCompletion.create(
            model=model,
            messages=agent.context + messages,
            temperature=0.5,
            # max_tokens=450,
            stop=stop_phrases
        )

        return response.choices[0].message["content"]
