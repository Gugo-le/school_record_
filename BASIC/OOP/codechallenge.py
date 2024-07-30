class Player:
    
  def __init__(self, name, xp, team):
    self.name = name
    self.xp = xp
    self.team = team

  def introduce(self):
    print(f"Hello! I'm {self.name} and I'm on {self.team}")

  def show_xp(self):
    print(f"This player has {self.xp} XP")


class Team:

  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []

  def show_players(self):
    for player in self.players:
      player.introduce()

  def add_player(self, name, xp):
    new_player = Player(name, xp, self.team_name)
    self.players.append(new_player)

  def remove_player(self, name):
    for player in self.players:
      if player.name == name:
        self.players.remove(player)
        return

  def total_xp(self):
    total = sum(player.xp for player in self.players)
    print(f"Total XP for {self.team_name}: {total}")


# Create instances and test the code
lynn = Player(name='Lynn', xp=100, team="Team Blue")

team_x = Team("Team X")

team_blue = Team("Team Blue")
team_blue.add_player("Lynn", 100)
team_blue.add_player("Kevin", 300)

team_blue.show_players()

# Calculate and show the total XP
team_blue.total_xp()
