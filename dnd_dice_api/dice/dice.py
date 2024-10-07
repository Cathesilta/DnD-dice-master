import random

class Dice:

    sides = []
    
    def __init__(self):
        if not self.sides:
            raise NotImplementedError("Derived dice classes must define the 'sides' attribute.")
        
        
    def roll_true_random(self):
        """
        Rolls the dice using a true random mechanism, 
        where every roll is independent of others.
        """
        if not self.sides:
            raise ValueError("Sides of the dice are not defined.")
        return random.choice(self.sides)
    
    def roll_false_random(self, n, target_value):
        """
        Rolls the dice using a false random mechanism.
        If rolled 'n' times, the value will approximate to 'target_value'.
        The target_value can be thought of as a designed bias.
        
        Arguments:
        - n: Number of times the dice will be rolled.
        - target_value: The average or target value the developer wants to approximate.
        """
        if not self.sides:
            raise ValueError("Sides of the dice are not defined.")
        
        result = []
        current_sum = 0

        for i in range(n):
            # Calculate remaining rolls and how much we need to get closer to the target.
            remaining_rolls = n - i
            needed_sum = target_value * n - current_sum

            if remaining_rolls > 1:
                # Determine an upper and lower bound for the next roll.
                lower_bound = max(min(self.sides), needed_sum // remaining_rolls - 1)
                upper_bound = min(max(self.sides), needed_sum // remaining_rolls + 1)
                next_roll = random.randint(lower_bound, upper_bound)
            else:
                # On the last roll, ensure the sum meets the target_value * n.
                next_roll = needed_sum

            # Ensure the roll is a valid side of the dice.
            next_roll = min(max(self.sides), max(min(self.sides), next_roll))

            result.append(next_roll)
            current_sum += next_roll

        return result
    
    
    
class D20(Dice):
    sides = list(range(1, 21))
    
class D12(Dice):
    sides = list(range(1, 13))
    
class D10(Dice):
    sides = list(range(1, 11))
    
class D8(Dice):
    sides = list(range(1, 9))
    
class D6(Dice):
    sides = list(range(1, 7))
    
class D4(Dice):
    sides = list(range(1, 5))
    
class D10_without_1(Dice):
    sides = list(range(2,11))