##########################################################################################################################################
# NECESSARY IMPORTS
##########################################################################################################################################

from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
import pandas as pd    
import numpy as np    
import unittest    
    
##########################################################################################################################################    
# UNIT TESTS  
##########################################################################################################################################
# 14 tests
##########################################################################################################################################

class MonteCarloTestSuite(unittest.TestCase):
    
    
    # Die class tests (6)
    
    def test_weight_change_output(self):
        '''
        purpose: demonstrating that changing the weight of a face on a die does what it is supposed to do
        input: weight of face 1 changed to 5
        output: Die object with face 1's weight changed to 5
        '''
        die1 = Die([1,2,3,4])
        die1.weight_change(1,5)
        self.assertEqual(die1.show_die().weights.tolist(), [5,1,1,1])
        
    def test_weight_change_input1(self):
        '''
        purpose: demonstrating that changing to an invalid weight will throw an exception
        input: weight of face 1 changed to 'a'
        output: exception because weight can't be changed to 'a'
        '''
        with self.assertRaises(Exception):
            die = Die([1,2,3,4])
            die.weight_change(1,'a')
            
    def test_weight_change_input2(self):
        '''
        purpose: demonstrating that changing the weight of an invalid face will throw an exception
        input: weight of face 9 changed to 4
        output: exception because face 9 doesn't exist
        '''
        with self.assertRaises(Exception):
            die = Die([1,2,3,4])
            die.weight_change(9,4)
    
    def test_roll_output(self):
        '''
        purpose: demonstrating that the length of the roll outputs will be equal to the number of rolls requested
        input: rolling a die 4 times
        output: a list of 4 die roll outcomes
        '''
        die2 = Die([1,2,3,4,5,6])
        outp = die2.roll(4)
        self.assertEqual(len(outp), 4)
        
    def test_roll_input(self):
        '''
        purpose: demonstrating that if no number of rolls is given, it will automatically roll the die object once
        input: a roll() call with no input
        output: length of roll results being 1
        '''
        die2 = Die([1,2,3,4,5,6])
        outp = die2.roll()
        self.assertEqual(len(outp), 1)
    
    def test_show_die(self):
        '''
        purpose: demonstrating that when a dataframe is created in the Die class, it is shown correctly through this method
        input: a dataframe created through the methods and a dataframe created by hand - both should be identical
        output: the two dataframes being equivalent
        '''
        die3 = Die([1,2,3])
        expected_df = pd.DataFrame({'faces':[1,2,3],'weights':[1.0,1.0,1.0],'face_index':[1,2,3]})
        expected_df.set_index('face_index', inplace=True)
        self.assertTrue(die3.show_die().equals(expected_df))
        
        
    # Game class tests (5)    
    
    def test_play(self):
        '''
        purpose: demonstrating that playing a game creates the appropriately-shaped dataframe with 3 columns (3 dice) and 20 rows (20 rolls)
        input: 3 dice, 20 rolls
        output: correct, 20x3 dataframe - displayed with show_results
        '''
        dice_to_use = [Die([1,2,3,4,5,6]),Die([1,2,3,4,5,6]),Die([1,2,3,4,5,6])]
        this_game = Game(dice_to_use)
        this_game.play(20)
        aaa = this_game.show_results()
        expected_shape = (20,3)
        self.assertEqual(aaa.shape, expected_shape)
        
    def test_show_results_wide_input1(self):
        '''
        purpose: demonstrating that the dataframe will be output in wide form if no input is given to the method
        input: nothing, Game object
        output: wide-form dataframe
        '''
        dice_to_use = [Die([1,2,3,4,5,6]),Die([1,2,3,4,5,6]),Die([1,2,3,4,5,6])]
        this_game = Game(dice_to_use)
        this_game.play(20)
        aaa = this_game.show_results()
        expected_shape = (20,3)
        self.assertEqual(aaa.shape, expected_shape)
        
    def test_show_results_wide_input2(self):
        '''
        purpose: demonstrating that the dataframe will be output in wide form if 'wide' input is given to the method
        input: 'wide'
        output: wide-form dataframe
        '''
        dice_to_use = [Die([1,2,3,4,5,6]),Die([1,2,3,4,5,6]),Die([1,2,3,4,5,6])]
        this_game = Game(dice_to_use)
        this_game.play(20)
        aaa = this_game.show_results('wide')
        expected_shape = (20,3)
        self.assertEqual(aaa.shape, expected_shape)
    
    def test_show_results_narrow(self):
        '''
        purpose: demonstrating that the dataframe will be output in narrow form if 'narrow' input is given to the method 
        input: 'narrow'
        output: narrow-form dataframe
        '''
        dice_to_use = [Die([1,2,3,4,5,6]),Die([1,2,3,4,5,6]),Die([1,2,3,4,5,6])]
        this_game = Game(dice_to_use)
        this_game.play(20)
        aaa = this_game.show_results('narrow')
        expected_shape = (60,1)
        self.assertEqual(aaa.shape, expected_shape)
        
    def test_show_results_wide_bad_input(self):
        '''
        purpose: demonstrating that the method will throw an exception if invalid input is fed to the method
        input: 'hello there'
        output: exception
        '''
        with self.assertRaises(Exception):
            dice_to_use = [Die([1,2,3,4,5,6]),Die([1,2,3,4,5,6]),Die([1,2,3,4,5,6])]
            this_game = Game(dice_to_use)
            this_game.play(20)
            aaa = this_game.show_results('hello there')  
        
        
    # Analyzer class tests (3)    
        
    def test_jackpot(self):
        '''
        purpose: demonstrating that the jackpot method will return an integer value for number of jackpots in the Game
        input: none, Game object
        output: an integer for number of 'True' values (jackpots)
        '''
        dice_to_use = [Die([1,2,3,4]),Die([1,2,3,4]),Die([1,2,3,4])]
        this_game = Game(dice_to_use)
        this_game.play(5000)
        this_one = Analyzer(this_game)
        answer = this_one.jackpot()
        self.assertTrue(type(answer) == int)
        
    def test_combo(self):
        '''
        purpose: demonstrating that the only column of data for the combo method is the number of times that combination occurred in the game (because the combination values themselves make up the index)
        input: none, Game object
        output: a dataframe with 1 column of frequency data and a 3-column-wide index for combination face values
        '''
        dice_to_use = [Die([1,2,3,4]),Die([1,2,3,4]),Die([1,2,3,4])]
        this_game = Game(dice_to_use)
        this_game.play(5000)
        this_one = Analyzer(this_game)
        answer = this_one.combo()
        self.assertTrue(len(answer.columns) == 1)
    
    def test_face_counts(self):
        '''
        purpose: demonstrating that the face_counts method returns a dataframe with a number of columns equal to the number of faces on the Dice being used (for possible roll outcomes) and a number of rows equal to the number of rolls
        input: none, Game object
        output: dataframe with 4 columns (4 faces on each die) and 50 rows (rolled 50 times)
        '''
        dice_to_use = [Die([1,2,3,4]),Die([1,2,3,4]),Die([1,2,3,4])]
        this_game = Game(dice_to_use)
        this_game.play(50)
        this_one = Analyzer(this_game)
        answer = this_one.face_counts()
        expected = (50, 4)
        self.assertTrue(answer.shape == expected)
        
        
unittest.main(argv=['first-arg-is-ignored'], exit=False);   

# results piped to montecarlo_tests_output.txt
# !python montecarlo_tests.py 2> montecarlo_tests_output.txt