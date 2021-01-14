from data.run import run_game
from data.scenes.StartScene import *

def main():
    run_game(1280, 720, 60, StartScene())


if __name__ == '__main__':
    main()