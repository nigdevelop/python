"""
A simple testing suite for Solitaire Mancala
Note that tests are not exhaustive and should be supplemented
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # create a game
    game = game_class
    
    # test the initial configuration of the board using the str method
    suite.run_test(str(game), str([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]), "Test #0: init")
    
    suite.run_test(game.get_grid_height(), 4, "Test #1: get_grid_height")
    suite.run_test(game.get_grid_width(), 4, "Test #2: get_grid_width")
    
    game.set_tile(2, 3, 16)
    suite.run_test(game.get_tile(2, 3), 16, "Test #3: get_tile")
    suite.run_test(str(game), str([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 16], [0, 0, 0, 0]]), "Test #0: init")

    game.reset()
    suite.run_test(str(game), str([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]), "Test #0: init")

    #game = TwentyFortyEight(4, 4)
    game.set_tile(0, 0, 2)
    game.set_tile(0, 1, 0)
    game.set_tile(0, 2, 0)
    game.set_tile(0, 3, 0)
    game.set_tile(1, 0, 0)
    game.set_tile(1, 1, 2)
    game.set_tile(1, 2, 0)
    game.set_tile(1, 3, 0)
    game.set_tile(2, 0, 0)
    game.set_tile(2, 1, 0)
    game.set_tile(2, 2, 2)
    game.set_tile(2, 3, 0)
    game.set_tile(3, 0, 0)
    game.set_tile(3, 1, 0)
    game.set_tile(3, 2, 0)
    game.set_tile(3, 3, 2)
    print str(game)
    game.move(1)
    print str(game)
    
  
    

