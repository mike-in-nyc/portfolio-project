from django.db import models

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=50)

    
    def __str__(self):
        return self.name

class ContestType(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class GameTime(models.Model):
    gameTime = models.ForeignKey
    
    def __str__(self):
        return self.gameTime

class Contest(models.Model):
    contestType = models.ForeignKey(ContestType, on_delete = CASCADE)
    gameTime = models.ForeignKey(GameTime, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField

    def __str__(self):
        return self.name 

class Position(models.Model):
    positionName = models.CharField(max_length=25)

    def __str__(self):
        return self.positionName

class Team(models.Model):
    name = models.CharField(max_length=100)
    location  = models.CharField(max_length=150)
    stadium = models.CharField(max_length = 150)
    abbreviation = models.CharField(max_length = 10)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return self.abbreviation


class Player(models.Model):
    name_dk = models.CharField(max_length=150)
    name_rg = models.CharField(max_length=150)

    def __str__(self):
        return self.name_dk
    
class Matchup(models.Model):
    gameDate = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    opponent = models.ForeignKey(Team, on_delete = models.CASCADE)
    gameTime = models.ForeignKey(GameTime, on_delete=models.CASCADE)
    hitterType = models.CharField(max_length=25)
    pitcherType = models.CharField(max_length=25)  
    # above two will likely be replaced by foreign keys when likely values are known

class PlayerMatchup(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    matchup = models.ForeignKey(Matchup, on_delete=models.CASCADE)
    salary = models.IntegerField
    projectedScore = models.DecimalField(decimal_places=3)
    actualScore = models.DecimalField(decimal_places=3)
    positionName = models.ForeignKey(Position, on_delete=models.CASCADE)

    #ideal return value: player name + date

class Lineup(models.Model):
    projectedScore = models.DecimalField(decimal_places=3)
    actualScore = models.DecimalField(decimal_places=3)
    cost = models.IntegerField
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    PlayerMatchup = models.ForeignKey(PlayerMatchup, on_delete=models.CASCADE)
