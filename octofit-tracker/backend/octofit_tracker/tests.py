from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com', first_name='Test', last_name='User')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username='member', email='member@example.com', first_name='Member', last_name='User')
        team = Team.objects.create(name='Test Team', description='A team for testing')
        team.members.append(user)
        team.save()
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='active', email='active@example.com', first_name='Active', last_name='User')
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, calories=300, date='2026-02-18')
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Leaderboard Team', description='Leaderboard test')
        leaderboard = Leaderboard.objects.create(team=team, points=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(username='workout', email='workout@example.com', first_name='Workout', last_name='User')
        workout = Workout.objects.create(user=user, workout_type='Yoga', suggested=True, date='2026-02-18')
        self.assertTrue(workout.suggested)
