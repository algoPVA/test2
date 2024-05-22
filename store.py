from dataclasses import dataclass

@dataclass
class Store:
    score: int

    def get_score(self):
        return self.score
    
    def change_score(self,delta):
        self.score += delta


store = Store(0)