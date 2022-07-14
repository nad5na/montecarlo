# montecarlo
Monte Carlo Project


METADATA
------------------------------------------------------------------------------------------------------------------------------------------------
Author: Noah Dunn

Project: Monte Carlo Simulator

Affiliation: UVA MSDS

------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------


SYNOPSIS
------------------------------------------------------------------------------------------------------------------------------------------------
Demo for installing:
    

Demo for importing:
    

Demo for creating and using Die class/methods:

    # creating a new die object with 6 faces, all of which have weights initialized to 1.0
        new_die = Die([1,2,3,4,5,6])
    # changing the weight of face 6 to be 5.0
        new_die.weight_change(6,5)
    # rolling the die object 10 times, yielding a list of the 10 outcomes
        new_die.roll(10)
    # displays the dataframe of the die faces matched with their respective weights
        new_die.show_die()

Demo for creating and using Game class/methods:

    # creating a new Game object using 3 die objects - they can be different dice but need to have the same number of faces
        new_game = Game([new_die,new_die,new_die])
    # rolling each of the dice 500 times and keeping track of each die's outcome for each roll
        new_game.play(500)
    # displaying the information (in a dataframe) from the play() method in wide form (#rolls rows by #dice columns)
        new_game.show_results()
    # displaying the information (in a dataframe) from the play() method in narrow form (1 column for face values, multi-columned index for die and roll number)
        new_game.show_results('narrow')

Demo for creating and using Analyzer class/methods:

    # creating a new analyzer object from a game
        new_analyer = Analyzer(new_game)
    # saving the integer number of jackpots into the 'jackpots' variable
        jackpots = new_analyzer.jackpots()
    # saving the multi-columned dataframe of combinations and their frequencies into the 'combo' variable
        combos = new_analyzer.combos()
    # saving the dataframe with roll number as index and columns for each possible face value and the number of times it was rolled into the 'face_counts' variable
        face_counts = new_analyzer.face_counts()
    
------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------


API DESCRIPTION
------------------------------------------------------------------------------------------------------------------------------------------------
# Die() class:

docstring:  

            purpose: creates a die object with various faces, face weights, and number of rolls and returns the rolled die object
            
            inputs: array of faces for the die object, weight to change/new weight, number of times die object is rolled
            
            outputs: die objects that have been rolled a certain amount of times with certain face weights
            
            methods: 
                     
                     weight_change(): changes weight of 1 die face
            
                     roll(): rolls the die a certain amount of times
                     
                     show_die(): shows the die faces and respective weights
attributes: 

            none
            
methods:

    __init__() method:
        parameters: (faces_init) array/list of die object 'face' values with dtype either strings or numbers
        return values: none
        docstring:  purpose: initializes the die object and sets all face weights equal to 1 originally
                    inputs: an array of faces that the die object will have (length = number of faces)
                    outputs: saves the faces and weights to the die_df dataframe that the other 3 methods will use
        
    weight_change() method:
        parameters: (face_to_change) a string or number in the array of faces from __init__ - it is checked to make sure input is in faces array
                    (new_weight) a float or float-convertible object - it is checked to make sure input is convertible to a float
        return values: none, weight for specific face is changed
        docstring:  purpose: changes the weight (probabilistic) of a single face, it also checks to make sure that inputs are valid
                    inputs: face that will have weight changed, the weight that the face will now have
                    outputs: the die object with updated face weights
        
    roll() method:
        parameters: (num_rolls) an integer or integer-convertible value for number of rolls, initialized to 1 if no input is taken
        return values: list of the outcomes (face values) from each roll for the Die object
        docstring:  purpose: 'rolls' the die object num_rolls times- basically a random sample from the vector of faces according to the weights.
                    inputs: number of times the die object is rolled
                    outputs: list of the values that arose from each roll of the die during that run
       
    show_die() method:
        parameters: none
        return values: dataframe
        docstring:  purpose: to display a dataframe of the die object's current state
                    inputs: none
                    outputs: a dataframe with roll number as the index & columns for faces and face weights
        
        
# Game() class:

docstring:  

            purpose: take a number of Die objects (all with same faces) and roll them a certain amount of times, keeping track of outputs
            
            inputs: list of the dice objects that will be used, number of rolls for each die object, form for the output the game dataframe will be returned
            
            outputs: dataframe (wide or narrow) of the outcome of the 'roll' of each die object for each roll
            
            methods: play(): rolls a number of Die objects a number of times and keeps track of the outcomes
                     show_results(): displays the outcomes from play() in either a wide table format or narrow table format               
attributes: 

            none

methods:

    __init__() method:
        parameters: list of created Die() objects
        return values: none
        docstring:  purpose: takes list of Die objects and gets them ready to be rolled a certain amount of times
                    inputs: list of Die objects
                    outputs: none
        
    play() method:
        parameters: number (convertible to int) for how man times the Die object is to be rolled
        return values: none
        docstring:  purpose: take a group of Die objects, 'roll' them a certain amount of times, and create a dataframe with the outcomes
                    inputs: number of rolls that each Die object will undergo
                    outputs: a private dataframe of N rolls by M Die objects with the roll number as the index
        
    show_results() method:
        parameters: none
        return values: dataframe
        docstring:  purpose: return the database from the 'play' method in a specified format
                    inputs: either 'wide' (or nothing) or 'narrow'
                    outputs: either a wide dataframe (N rolls by M dice) or a narrow dataframe (indexes for rolls & dice, one column for roll outcomes)
        

# Analyzer() class:

docstring:      
            
            purpose: performs various analyses on the results from a Game of Die objects
            
            inputs: a Game object in which a certain amount of 'dice' have been rolled a certain number of times
            
            outputs/methods: 
                             
                             jackpot - number of times that all faces of die objects rolled were equal
                             
                             combo - a dataframe of the distinct permutations* (I spoke with the professor on Tuesday and he said that due to confusion on Monday when someone was told to use permutations instead of combinations, I could leave this method as computing the permutations) from the dice rolls and the amount of times that they occured in the Game, with permutations as the index
                             
                             face counts - a dataframe with roll number from the game as the index, and columns for each possible Die face value populated (in each roll row, respectively) with the number of times that face appeared during that roll    
attributes: 

            (df_to_ret) an object that will hold the dataframe produced by the combo() method
            
            (face_counts) an object that will hold the dataframe produced by the face_counts() method
            
            (eq_rows) an object that will hold the dataframe produced byt the jackpot() method
methods:

    __init__() method:
        parameters: a Game() object that has been created
        return values: none
        docstring:  purpose: initializing the analyzer object
                    inputs: a Game object in which a certain amount of 'dice' have been rolled a certain number of times
                    outputs: number of times that all faces of die objects rolled were equal
        
    jackpot() method:
        parameters: none
        return values: integer for number of time a jackpot occurred during that Game()
        docstring:  purpose: determine how many times all of the Die objects were rolled and had the same face value
                    inputs: none (Game in initializer)
                    outputs: integer for how many times the jackpot occurred
                         also has a dataframe 'eq_rows' that is basically a list of True/False for jackpot for each roll, roll as index with one column of True/False
                         also has a dataframe 'eq_rows_trues' that is the same as 'eq_rows' but only with the rows that returned True
        
    combo() method: 
        parameters: none
        return values: dataframe with combos as the index and combo counts as the data column
        docstring:  purpose: determine distinct permutations of faces rolled in each Game and how many times each occurred
                    inputs: none (Game in initializer)
                    outputs: a dataframe with index columns for each face value from that roll, and a column with number of times that combination happened
        
    face_counts() method:
        parameters: none
        return values: dataframe with roll_number as index and amount of times each face was rolled as data columns
        docstring:  purpose: determine how many times each face value is rolled within a group of Die objects for each roll
                    inputs: none (Game in initializer)
                    outputs: a dataframe with roll number from the game as the index, and columns for each possible Die face value populated (in each roll row, respectively) with the number of times that face appeared during that roll
                    
------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------


MANIFEST
------------------------------------------------------------------------------------------------------------------------------------------------
Files:

    mc_package
    
        montecarlo.py
        
        montecarlo_tests.py
        
        montecarlo_tests_output.txt
        
        montecarlo_demo.ipynb
        
    setup.py
    
    README.mg
    
    LICENSE
    
    .gitignore
    
------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------
