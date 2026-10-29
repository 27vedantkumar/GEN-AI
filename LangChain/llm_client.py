import json
import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


load_dotenv()


def load_config(config_path: str = "config.json") -> dict:
    """
    Load configuration from the config.json file.

    Args:
        config_path (str): Path to the configuration file.

    Returns:
        dict: Configuration dictionary.
    """
    with open(config_path, "r") as file:
        return json.load(file)


def get_llm():
    """
    Returns the configured LangChain Chat Model.
    Supported Providers:
        - OpenAI
        - Gemini
        - Anthropic        
    """

    config = load_config()

    provider = config["provider"].lower()

    if provider == "openai":
        return ChatOpenAI(
            model=config["openai"]["model"],
            temperature=config["openai"]["temperature"],
            max_tokens=config["openai"]["max_tokens"],
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    elif provider == "gemini":
        return ChatGoogleGenerativeAI(
            model=config["gemini"]["model"],
            temperature=config["gemini"]["temperature"],
            max_tokens=config["gemini"]["max_tokens"],
            google_api_key=os.getenv("GOOGLE_API_KEY"),
        )

    # elif provider == "anthropic":
    #     return ChatAnthropic(
    #         model=config["anthropic"]["model"],
    #         temperature=config["anthropic"]["temperature"],
    #         max_tokens=config["anthropic"]["max_tokens"],
    #         api_key=os.getenv("ANTHROPIC_API_KEY"),
    #     )
    
    else:
        raise ValueError(f"Unsupported provider: {provider}")