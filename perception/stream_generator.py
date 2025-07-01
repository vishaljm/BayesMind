import time
import random

class Stimulus:
    def __init__(self, symbol, duration):
        self.symbol = symbol
        self.duration = duration

    def __repr__(self):
        return f"Stimulus(symbol='{self.symbol}' duration={self.duration}s)"
    
def generate_stimuli(symbols=["A", "B", "C"], rhythm=[0.5, 1.0, 1.5]):
        while True:
            symbol = random.choice(symbols)
            duration = random.choice(rhythm)
            yield Stimulus(symbol, duration)

stream = generate_stimuli()
for _ in range(10):
     stimulus = next(stream)
     print(stimulus)
