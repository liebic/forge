"""Simulates a game of mario kart through randomized events and text-based prompts.
"""
class MarioKart:
    """
    A class representing mario kart, that includes a list of players and 
    available characters.

    Attributes: 
    players(list): A list of players in the game
    available_characters(list): A list of characters a player can choose from
    
    Returns: prints available players
    """
    def __init__(self):
      """Initialize a MarioKart instance.
      """
      self.players = [] #initializing an empty list of players names
      self.available_characters = ["Mario", "Luigi", "Princess Peach", "Bowser"]
      
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




def player_position():
    """ Determine what play the player is after using special item.
    
    Returns: Player Position and whether or not they are in top 3.
    """

def burn_out_probability(player):
  """Calculates the probability of a player burning out at the start of a race.

  Args:
    player: A Player object.

  Returns:
    A float representing the probability of the player burning out.
  """
  
def prob_hit_player(player_rank, speed):
    ''' Determines the probability a player is hit by another player. 
    
      Args: 
        player_rank(int): The placement of the player in the race.
        speed (int): speed of player 
    
      Returns: the prob of player hitting another player
    '''
    
    
def prob_hit_player(player_rank, speed):
      ''' Determines the probability a player is hit by another player. 
      
      Args: 
        player_rank(int): The pacement of the player in the race.
        speed (int): speed of player 
      '''
    