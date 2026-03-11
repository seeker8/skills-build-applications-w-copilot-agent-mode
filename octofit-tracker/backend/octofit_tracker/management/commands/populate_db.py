
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Eliminar datos previos
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Crear usuarios
        spiderman = User.objects.create(username='spiderman', email='spiderman@marvel.com', first_name='Peter', last_name='Parker')
        ironman = User.objects.create(username='ironman', email='ironman@marvel.com', first_name='Tony', last_name='Stark')
        batman = User.objects.create(username='batman', email='batman@dc.com', first_name='Bruce', last_name='Wayne')
        wonderwoman = User.objects.create(username='wonderwoman', email='wonderwoman@dc.com', first_name='Diana', last_name='Prince')

        # Crear equipos y asignar miembros
        marvel = Team.objects.create(name='Marvel', members=['spiderman', 'ironman'])
        dc = Team.objects.create(name='DC', members=['batman', 'wonderwoman'])

        # Crear actividades
        Activity.objects.create(user='spiderman', type='Correr', duration=30, calories=300, date=timezone.now())
        Activity.objects.create(user='ironman', type='Nadar', duration=45, calories=400, date=timezone.now())
        Activity.objects.create(user='batman', type='Escalar', duration=25, calories=250, date=timezone.now())
        Activity.objects.create(user='wonderwoman', type='Volar', duration=60, calories=500, date=timezone.now())

        # Crear leaderboard
        Leaderboard.objects.create(team='Marvel', points=700)
        Leaderboard.objects.create(team='DC', points=750)

        # Crear workouts
        Workout.objects.create(name='Entrenamiento Marvel', description='Rutina para héroes Marvel', suggested_for='Marvel')
        Workout.objects.create(name='Entrenamiento DC', description='Rutina para héroes DC', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('Base de datos poblada con datos de prueba.'))
