import game
import goldgame_ui

import unittest
class test_game (unittest.Testcase):
        def test_game_victory_should_add_to_points(self):
                
                player_1 = game.Player('Mr Hero Man','player_1', 0)
        
                
                goldgame_ui.victory()
                expected = 1
                actual = player_1.points

                self.assertEqual(actual, expected)

                
                
