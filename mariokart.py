import random
import re

class Player:
    def __init__(self, name, position):
        """
        Initialize a Player instance.

        Parameters:
        - name (str): The name of the player.
        - position (int): The starting position of the player.
        """
        self.name = name
        self.character = None
        self.position = position
        self.speed = random.randint(1, 10)
        self.wins = 0

    def adjust_position(self, finishing_order, item_effect):
        """
        Adjust the player's position based on finishing order and item effect.

        Parameters:
        - finishing_order (int): The finishing order of the player.
        - item_effect (str): The effect of the item received.
        """
        position_change = 0

        if item_effect == "Star":
            position_change = 2
        elif item_effect == "Bullet-Bill":
            position_change = 3

        self.position = max(1, finishing_order + 1 + position_change)

    def player_position(self, finishing_order, item_effect, is_hit_by_special_item, is_using_special_item):
        """
        Update player position based on special items.

        Parameters:
        - finishing_order (int): The finishing order of the player.
        - item_effect (str): The effect of the item received.
        - is_hit_by_special_item (bool): Whether the player is hit by a special item.
        - is_using_special_item (bool): Whether the player is using a special item.
        """
        if is_hit_by_special_item or is_using_special_item:
            self.adjust_position(finishing_order, item_effect)

    def burn_out_probability(self, item_effect):
        """
        Calculate burnout probability based on the item effect.

        Parameters:
        - item_effect (str): The effect of the item received.

        Returns:
        - float: The calculated burnout probability.
        
        Side Effects:
        - Returns burn out probability 
        """
        base_probability = random.random()
        speed_factor = self.speed / 10.0

        if item_effect in ["Mushroom", "Triple-Mushroom"]:
            speed_factor *= 1.2
        elif item_effect == "Golden-Mushroom":
            speed_factor *= 1.5

        burn_out_probability = base_probability * speed_factor
        burn_out_probability = max(0.0, min(1.0, burn_out_probability))
        return burn_out_probability
    
class MarioKart:
    def __init__(self):
        """
        Initialize a MarioKart instance.
        """
        self.players = []
        self.available_characters = ["Mario", "Luigi", "Princess Peach", "Bowser", "Daisy", "Shy Guy", "Toad", "Wario", "Link", "Donkey Kong", "Waluigi", "King Boo", "Yoshi", "Birdo", "Lakitu"]
        self.available_vehicles= ["Bike","Sprinter","Wild Wiggler","Kart","Mach Bike","Biddybuggy","Flame Runner","Spear"]

    def set_players(self, players_names):
        """
        Set the players for the game.

        Parameters:
        - players_names (list): A list of player names.
        """
        if not isinstance(players_names, list):
            raise TypeError("The players_names parameter must be a list! Try again.")
        if len(players_names) > 4:
            raise ValueError("Cannot have more than four players. Try playing again next round.")
        positions = random.sample(range(1, 5), len(players_names))
        self.players = [Player(name, position) for name, position in zip(players_names, positions)]

    def choosing_character(self, player):
        """
        Allow a player to choose a character for the game.

        Parameters:
        - player (Player): The player choosing a character.
        """
        print("\nAvailable characters are: ")
        for char in self.available_characters:
            print(char)
    def choosing_vehicle(self, player):
        """
        Allows a player to choose a vechile that they will play the game with. 
        Parameters: 
        player(Player): The player choosing a character
        Side effects:
        -prints the available vechiles
        -updates the player.vechile and player.character based on whatever the player chooses. 
        -uses print statements to inform the player of various information
        """
        print("Available vehicles are: ", ", ".join(self.available_vehicles))
        while True:
            chosen_vehicle = input(f"{player.name}, choose a vehicle: ").capitalize()
        
            if any(vehicle.lower() == chosen_vehicle.lower() for vehicle in self.available_vehicles):
                self.available_vehicles = [vehicle for vehicle in self.available_vehicles if vehicle.lower() != chosen_vehicle.lower()]
                print(f"{player.name} has chosen {chosen_vehicle}!")
                player.vehicle = chosen_vehicle
                break
            else:
                print(f"Sorry, {chosen_vehicle} has already been chosen for this round. Please choose another.")

        while True:
            character = input(f"{player.name}, choose a character: ").capitalize()

            if character.lower() in [char.lower() for char in self.available_characters]:
                self.available_characters.remove([char for char in self.available_characters if char.lower() == character.lower()][0])
                print(f"{player.name} has chosen {character}!")
                player.character = character
                break
            else:
                print(f"Sorry, {character} is not available or has already been chosen. Please choose another.")

    def run_round(self):
        """
        Allows a round of Mario Kart to be played. 
        Side effects:
        - Burnout probability is used to update player positions
        - player list is sorted based on updated positions 
        -The player with the highest position at the end of the round is considered the winner for that particular round. 
        -information about each plater's position and burnout probability is printed
        """
        print("\nCurrent Player Positions:")
        for player in self.players:
            item_effect = player.mystery_box(player.position)
            burnout_probability = player.burn_out_probability(item_effect)

            print(f'{player} - Burnout Probability: {burnout_probability:.2f}')

            player.player_position(
                self.players.index(player),
                item_effect,
                random.choice([True, False]),
                random.choice([True, False])
            )

        self.players.sort(key=lambda player: player.position)

        round_winner = self.players[0]
        round_winner.wins += 1

    def display_overall_winner(self):
        """
        Display the overall winner of the Mario Kart game.

        Parameters:
        - None

        Returns:
        - None

        Side Effects:
        - Modifies the order of players in the self.players list.
        - Prints information about tiebreaker rounds if there is a tie.
        - Calls the choosing_character method and the run_round method if there is a tie.
        - Calls the plot_final_ranking method to display the final ranking.
        - Prints information about the overall winner.
        """
        self.players.sort(key=lambda player: player.wins, reverse=True)

        tied_players = [player for player in self.players if player.wins == self.players[0].wins]

        if len(tied_players) == 1:
            print("\nTiebreaker Round for Tied Players:")
            for player in tied_players:
                self.choosing_character(player)
            self.run_round()

            self.players.sort(key=lambda player: player.wins, reverse=True)

        print("\nOverall Winner:")
        print(f"{self.players[0].name} ({self.players[0].character})!")

        
    def plot_final_ranking(self, players):
        """
        Plot the final ranking bar graph for all players.

        Parameters:
        players (list): List of Player objects.
        """
        player_names = [player.name for player in players]
        player_wins = [player.wins for player in players]

        sns.barplot(x=player_names, y=player_wins)
        plt.title('Final Ranking')
        plt.xlabel('Players')
        plt.ylabel('Wins')
        plt.show()



if __name__ == "__main__":
    mario_kart_game = MarioKart()

    for _ in range(3):  # Run 3 rounds
        mario_kart_game.set_players(["Player1", "Player2", "Player3", "Player4"])

        for player in mario_kart_game.players:
            mario_kart_game.choosing_character(player)
            mario_kart_game.choosing_vehicle(player)

        mario_kart_game.run_round()

    mario_kart_game.display_overall_winner()
