from djongo import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)  # Lista de usernames
    created_at = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    user = models.CharField(max_length=150)  # username
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutos
    calories = models.IntegerField()
    date = models.DateTimeField()

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)  # team name
    points = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)

