# Define the base class player
class Player:
  def play(self):
    print("The player is Playing Cricket.")

# Define the derived class batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

# Define the derived class bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

# Create Object of Batsman and Bowler Classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()