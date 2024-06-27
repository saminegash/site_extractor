from argparse import ArgumentParser

from hydra.utils import instantiate  # type: ignore
from omegaconf import OmegaConf  # type: ignore

from sherpa_ai.agents import QAAgent  # type: ignore
from sherpa_ai.events import EventType  # type: ignore
from extractor import extractor


def get_qa_agent_from_config_file(
    config_path: str,
) -> QAAgent:
    """
    Create a QAAgent from a config file.
    Args:
        config_path: Path to the config file
    Returns:
        QAAgent: A QAAgent instance
    """

    config = OmegaConf.load(config_path)

    agent_config = instantiate(config.agent_config)
    qa_agent: QAAgent = instantiate(config.qa_agent, agent_config=agent_config)

    return qa_agent


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--config", type=str, default="agent_config.yaml")
    args = parser.parse_args()

    qa_agent = get_qa_agent_from_config_file(args.config)
    extractor()

    while True:
        question = input("Ask me a question: ")

        # Add the question to the shared memory. By default, the agent will take the last
        # message in the shared memory as the task.
        qa_agent.shared_memory.add(EventType.task, "human", question)
        result = qa_agent.run()
        print(result)
