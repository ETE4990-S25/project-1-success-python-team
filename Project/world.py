import random

def event_generator():
    """Yields random world events."""
    events = ["You found a treasure chest!", "A wild beast appears!", "You discovered an ancient ruin."]
    while True:
        yield random.choice(events)

# Example Usage
exploration = event_generator()
for _ in range(3):
    print(next(exploration))
