from abc import ABC, abstractmethod


class BaseAI(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass