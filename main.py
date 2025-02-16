from welcome.display_intro import display_intro
from welcome.display_exit import display_exit
from game_flow.main_loop import main_loop

def start():
    display_intro()
    main_loop()
    display_exit()


if __name__ == '__main__':
    start()