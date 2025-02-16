import time
def display_start_game_details(player1, player2, total_rounds):
    wait_time = 1.5
    print()
    print("Starting game...")
    time.sleep(wait_time)
    print(f"Player 1: {player1.name}")
    time.sleep(wait_time)
    print(f"Player 2: {player2.name}")
    time.sleep(wait_time)
    print(f"Rounds needed to win: {total_rounds}")
    time.sleep(2.5)