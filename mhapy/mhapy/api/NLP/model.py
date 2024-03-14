from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def give_score(self, text:str)->int:
        pass
    
