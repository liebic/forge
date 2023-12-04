"""Simulates a game of mario kart through randomized events and text-based prompts.
"""
import random
import re
class MarioKart:
    """
    A class representing mario kart, that includes a list of players and 
    available characters.

    Attributes: 
    players(list): A list of players in the game
    available_characters(list): A list of characters a player can choose from
    
    Returns: prints available players
    """
    def __init__(self, players_info=[]): 
      """Initialize a MarioKart instance.
      """
      self.players = [] #initializing an empty list of players names
      self.available_characters = ["Mario", "Luigi", "Princess Peach", "Bowser"]
      
      for player, character in players_info:
        self.choosing_character(player, character)
      
    def set_players(self, players_names):
      """Set the list of players who are participating in the MarioKart game.

      Args:
          players_names (list): A list containing the names of the players

      Raises:
          TypeError: If the player_names is not on the list
          ValueError: If the number of players is more than 4
      """
      if not isinstance(players_names, list): #making sure players name is on the list
        raise TypeError("The players_list must be on the list! Try again.")
      if len(players_names) > 4: #checking to see if the number of players exceed 4
        raise ValueError("Cannot have more than four players, sorry! Try \
          playing again next round.")
      self.players = players_names
      
    def get_available_characters(self):
      """Return the list of available characters

      Returns:
          list: A list containing the names of the available characters.
      """
      return self.available_characters
    
    def choosing_character(self, player, character):
      """A player is choosing what character they'll play as.

      Args:
          player (str): The name of the player choosing the character.
          character (str): The name of the character being chosen.
          
      Side effects:
        prints results of character selection
      """
      # printing available characters before the player chooses
      print("Available characters are: ")
      for char in self.available_characters:
        print(char)
        
      player = input("")
      
      if character in self.available_characters:
        self.available_characters.remove(character)
        self.players.append((player, character)) # adding the player and their
          #chosen character to the list of characters
        print(f"{player} has chosen {character}!")
      else:
        print(f"Sorry, {character} has already been chosen. Please choose another.")
    
    
    def mystery_box(player_rank):
      """Determines the type of item that a player will recieve from a mystery box
      
      Args:
        player_rank(int): The placement of the player in the race.
    """
      with open("items.txt", 'r') as file:
        for item in file:
          if re.match(r'[A-Za-z]+(-?)[A-Za-z]+', item):
            each_item = item.split(" ")
        if player_rank == 1:
            rand_item = random.choice(each_item[0:4])
        elif player_rank == 2:
            rand_item = random.choice(each_item[0:7])
        elif player_rank == 3:
            rand_item = random.choice(each_item[0:11])
        elif player_rank == 4:
          rand_item = random.choice(each_item[0:14])
        return print(f'Player in {player_rank} place received: {rand_item}')
      def prob_hit_player(num_players, player_rank, speed):
        ''' Determines the probability a player is hit by another player. 
        Args: 
        num_players(int): number of players playing 
        player_rank(int): The placement of the player in the race.
        speed (int): speed of player. This will be a number between 1 and 100.  
        Returns: an f string that contains the prob of player hitting another player'''
        if speed > 100:
            return "Choose a speed between 0 and 100 mph."
        #create rank_factor. This depicts that the probability of hitting another player will likey change as player rank changes.
        rank_factor= player_rank/num_players
        #create speed_factor. This depicts that the probability of hitting another player will change  as a player's speed changes 
        speed_factor = speed/100
        probability_hit_player=(rank_factor+speed_factor)/2
        #ensure probability is between 0 and 1 
        probability_hit_player=max(0, min(1,probability_hit_player))
        probability_hit_player=round(probability_hit_player,2)
        return f"The probability of hitting another player is {probability_hit_player}."

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def adjust_position(self, position_change):
        self.position += position_change

    def player_position(player, is_hit_by_special_item, is_using_special_item):
        """
        Determine the player's position and whether they are in the top 3 after using a special item or being hit by one.

        Args:
        player (Player): The Player object for the player.
        is_hit_by_special_item (bool): True if the player is hit by a special item, False if not.
        is_using_special_item (bool): True if the player is using a special item, False if not.

        Returns:
        player position indicating whether they are in the top 3 or not.
        """
        if is_hit_by_special_item:
            player.adjust_position(-2)
        if is_using_special_item:
            player.adjust_position(3)

        players = sorted(players, key=lambda p: p.position, reverse=True)
        player_index = players.index(player)
        player_position = player_index + 1 

        in_top_3 = player_index < 3

        return print(f"{player.name}: Position {player_position}, In Top 3: {in_top_3}")

def burn_out_probability(player):
  """Calculates the probability of a player burning out at the start of a race.

  Args:
    player: A Player object.

  Returns:
    A float representing the probability of the player burning out.
  """
  base_probability = random.random() # base probability selected randomly
  speed_factor = player.speed / 10.0  # speed is on a scale of 0 to 10

  # calculates burn-out probability by base and player speed
  burn_out_probability = base_probability * speed_factor

  # keeps probability as a float between 0 and 1
  burn_out_probability = max(0.0, min(1.0, burn_out_probability))

  return burn_out_probability

if __name__ == "__main__":
  mario_kart_game = MarioKart()