from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Eliminar datos previos
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        users = [
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='1234'),
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='1234'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='1234'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='1234'),
        ]

        # Crear actividades
        Activity.objects.create(name='Correr', user='spiderman', team='Marvel', points=10)
        Activity.objects.create(name='Nadar', user='ironman', team='Marvel', points=15)
        Activity.objects.create(name='Escalar', user='batman', team='DC', points=12)
        Activity.objects.create(name='Volar', user='wonderwoman', team='DC', points=20)

        # Crear leaderboard
        Leaderboard.objects.create(team='Marvel', points=25)
        Leaderboard.objects.create(team='DC', points=32)

        # Crear workouts
        Workout.objects.create(name='Entrenamiento Marvel', description='Rutina para héroes Marvel', suggested_for='Marvel')
        Workout.objects.create(name='Entrenamiento DC', description='Rutina para héroes DC', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('Base de datos poblada con datos de prueba.'))
