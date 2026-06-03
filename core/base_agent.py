from abc import ABC, abstractmethod
class BaseAgent(ABC):
    def __init__(self, role='general'): self.role = role; self.memory = []
    def run(self, task): return f'[{self.role}] {task}'
    def add_memory(self, item): self.memory.append(item)