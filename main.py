
from dotenv import load_dotenv
from colorama import Fore, Style, init
from agency.agent_manager import AgentManager

load_dotenv(verbose=True)

init()

def read_role_from_file(filename: str) -> str:
    with open(filename, "r") as f:
        role = f.read().strip()
    return role


def chatbots_conversation(agent_manager: AgentManager, num_turns: int = 10):
    messages = []

    for agent in agent_manager.agents:
        agent.start_agent(handler="mr_handler")

    for i in range(num_turns):
        # Bot 1 responds
        bot1_response = agent_manager.generate_response(0, messages, stop_phrases=[agent_manager.agents[1].name])
        print(f"{Fore.YELLOW}{bot1_response}{Style.RESET_ALL}")
        messages.append({"role": "assistant", "content": bot1_response, "name": agent_manager.agents[0].name })

        # Bot 2 responds
        bot2_response = agent_manager.generate_response(1, messages, stop_phrases=[agent_manager.agents[0].name])
        print(f"{Fore.BLUE}{bot2_response}{Style.RESET_ALL}")
        messages.append({"role": "assistant", "content": bot2_response, "name": agent_manager.agents[1].name })

if __name__ == "__main__":
    manager = AgentManager()
    manager.add_agent(read_role_from_file("miss_writer_role.txt"), "Miss_Writer")
    manager.add_agent(read_role_from_file("mr_editor_role.txt"), "Mr_Editor")

    chatbots_conversation(manager)

