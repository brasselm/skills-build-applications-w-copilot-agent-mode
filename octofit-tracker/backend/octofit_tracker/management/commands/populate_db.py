from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Daten löschen
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User(username='ironman', email='ironman@marvel.com', first_name='Tony', last_name='Stark'),
            User(username='spiderman', email='spiderman@marvel.com', first_name='Peter', last_name='Parker'),
            User(username='batman', email='batman@dc.com', first_name='Bruce', last_name='Wayne'),
            User(username='wonderwoman', email='wonderwoman@dc.com', first_name='Diana', last_name='Prince'),
        ]
        for user in users:
            user.save()

        # Team-Mitglieder
        marvel.members.extend([users[0], users[1]])
        marvel.save()
        dc.members.extend([users[2], users[3]])
        dc.save()

        # Activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, calories=300, date='2026-02-18')
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, calories=400, date='2026-02-18')
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, calories=500, date='2026-02-18')
        Activity.objects.create(user=users[3], activity_type='Yoga', duration=40, calories=200, date='2026-02-18')

        # Workouts
        Workout.objects.create(user=users[0], workout_type='HIIT', suggested=True, date='2026-02-18')
        Workout.objects.create(user=users[1], workout_type='Strength', suggested=False, date='2026-02-18')
        Workout.objects.create(user=users[2], workout_type='Cardio', suggested=True, date='2026-02-18')
        Workout.objects.create(user=users[3], workout_type='Pilates', suggested=False, date='2026-02-18')

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=700, rank=1)
        Leaderboard.objects.create(team=dc, points=600, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db erfolgreich mit Testdaten befüllt!'))
