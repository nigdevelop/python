"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
#import poc_holds_testsuite
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    #print hand
    high_score = 0
    high_index = 0
    score_dict = {}
    for card_val in hand:
        score_dict[card_val]= card_val + score_dict.get(card_val, 0)
    for val, val_score in score_dict.items():
        if(val_score>high_score):
            high_score = val_score
            high_index = val
    return score_dict[high_index]


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    all_seq = gen_all_sequences(range(1, num_die_sides+1), num_free_dice)
    exp_val = 0.0
    for seq in all_seq:
        tmp_list = list(seq)
        tmp_list.extend(list(held_dice))
        exp_val += score(tmp_list)           
    return exp_val/len(all_seq)

def contains_list(sublist, parentlist):
    """
    Checks if sublist part of parent list.

    Returns True is sublist elemnts in parent list. False otherwise'
    """    
    for element in sublist:
        if element in parentlist:
            parentlist.remove(element)
        else:
            return False
    return True
            
            
def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    outcomes = hand
    answer_set = set([()])
    for dummy_idx in range(len(hand)-1):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                new_sequence.sort()
                if contains_list(new_sequence, list(hand)):
                    temp_set.add(tuple(new_sequence))
        answer_set = answer_set.union(temp_set)        
    answer_set.add(hand)    
    return answer_set


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    high_score = 0.9
    high_score_tuple = ()
    for item in gen_all_holds(hand):
        exp_val = expected_value(item, num_die_sides, len(hand) - len(item))
        if exp_val>high_score:
            high_score = exp_val
            high_score_tuple = item
            #print item, expected_value(item, num_die_sides, len(hand) - len(item))
    return (high_score, high_score_tuple)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    print score(hand)
    print expected_value((2 , 2), 6, 2)
    
#run_example()



#import poc_holds_testsuite
print strategy((1,), 6)
#poc_holds_testsuite.run_suite(gen_all_holds)
#print gen_all_holds(tuple([1,2,2]))


                                       
    
    
    



