import sys, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def random_choice():
    outcomes = dict(
        heads=0,
        tails=0,
    )
    slides = list(outcomes.keys())
    for _ in range(10_000):
        outcomes[random.choice(slides)] += 1
    print('heads:', outcomes['heads'])
    print('tails:', outcomes['tails'])

if __name__ == "__main__":
    random_choice()