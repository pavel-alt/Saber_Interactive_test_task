def test_scenario(run_game, game_stat):
    """
    1. Start new game
    2. Make a screenshot
    3. Start the program to record statistics
    4. Make the character go forward
    5. Stop the program to record statistics
    6. Make a screenshot
    7. Exit the game
    8. Recording average fps in a new file
    :param run_game: Game, current game
    :param game_stat: Stat, collection of game statistics
    :return: None
    """
    run_game.start_new_game()
    game_stat.make_screenshot()
    run_game.get_stat()
    run_game.run(duration=5)
    run_game.get_stat()
    game_stat.make_screenshot()
    run_game.game_over()
    game_stat.make_average_fps()
