from data.run import run_game
from data.scenes.StartScene import *

def main():
    run_game(1200, 800, 60, StartScene())


if __name__ == '__main__':
    main()