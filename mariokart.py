"""Simulates a game of mario kart through randomized events and text-based prompts.
"""
class MarioKart:
    """
    A class representing mario kart, that includes a list of players and available characters.

    Attributes: 
    players(list): A list of players in the game
    available_characters(list): A list of characters a player can choose from
    
    Returns: prints available players
    """
    def __init__(self):
    
    
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
    