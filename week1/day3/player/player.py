class Player:
    def __init__(self, information):
        self.name = information['name']
        self.age = information['age']
        self.position = information['position']
        self.team = information['team']
    def __repr__(self):
        return f"Player: {self.name}, {self.age} y/o, position: {self.position}, team: {self.team}"

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
jason = {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"}
kyrie = {"name": "Kyrie Irving", "age":32,"position": "Point Guard", "team": "Brooklyn Nets"}

# Create your Player instances here!
# player_jason = ???

player_kevin = Player(kevin)
print(f"player 1: {player_kevin}")
player_jason = Player(jason)
print(f"Player 2: {player_jason}")
player_kyrie = Player(kyrie)
print(f"Player 3: {player_kyrie}")

players = [{"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"},{"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"},{"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"},{"name": "Damian Lillard", "age":33, "position": "Point Guard", "team": "Portland Trailblazers"},{"name": "Joel Embiid", "age":32, "position": "Power Foward", "team": "Philidelphia 76ers"},{"name": "DeMar DeRozan", "age": 32, "position": "Shooting Guard", "team": "Chicago Bulls"}]
new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)