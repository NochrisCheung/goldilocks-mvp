from abc import ABC, abstractmethod
import os
from pathlib import Path
from typing import Any, Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

class LLMClient(ABC):
    """Abstract base class for LLM interactions"""
    
    @abstractmethod
    def generate_response(self, prompt: str) -> Optional[Dict[str, Any]]:
        """Generate response from LLM"""
        pass
    

class DeepSeekClient(LLMClient):
    """Client for DeepSeek LLM
    
    """
    
    def __init__(
        self,
        model: str = "deepseek-chat",
        temperature: float = 0.7,
        max_tokens: int = 2048,
        system_prompt: str = "You are a helpful assistant.",
        response_format: Optional[Dict[str, Any]] = None,
        is_stream: bool = False
    ):
        """
        Initialize DeepSeek client
        
        Args:
            model (str): The DeepSeek model to use
            temperature (float): Controls randomness (0-1)
            max_tokens (int): Maximum tokens in the response
        """
        self.client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.system_prompt = system_prompt
        self.response_format = response_format
        self.is_stream = is_stream
    
    def generate_response(self, prompt: str) -> Optional[Dict[str, Any]]:
        """Generate response from LLM"""
        params = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stream": self.is_stream
        }
        
        if self.response_format:
            params["response_format"] = self.response_format

        response = self.client.chat.completions.create(**params)

        return response.choices[0].message.content