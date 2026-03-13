
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create users (super heroes)
        users = [
            {
                'username': 'ironman',
                'email': 'ironman@marvel.com',
                'first_name': 'Tony',
                'last_name': 'Stark',
                'age': 45,
                'bio': 'Genius, billionaire, playboy, philanthropist.'
            },
            {
                'username': 'captainamerica',
                'email': 'cap@marvel.com',
                'first_name': 'Steve',
                'last_name': 'Rogers',
                'age': 100,
                'bio': 'The first Avenger.'
            },
            {
                'username': 'batman',
                'email': 'batman@dc.com',
                'first_name': 'Bruce',
                'last_name': 'Wayne',
                'age': 40,
                'bio': 'The Dark Knight.'
            },
            {
                'username': 'wonderwoman',
                'email': 'wonderwoman@dc.com',
                'first_name': 'Diana',
                'last_name': 'Prince',
                'age': 3000,
                'bio': 'Amazonian warrior princess.'
            },
        ]
        user_ids = db.users.insert_many(users).inserted_ids

        # Create teams
        marvel = {
            'name': 'Team Marvel',
            'members': [user_ids[0], user_ids[1]],
            'created_at': datetime.utcnow()
        }
        dc = {
            'name': 'Team DC',
            'members': [user_ids[2], user_ids[3]],
            'created_at': datetime.utcnow()
        }
        team_ids = db.teams.insert_many([marvel, dc]).inserted_ids

        # Create activities
        db.activities.insert_many([
            {
                'user_id': user_ids[0],
                'activity_type': 'Running',
                'duration_minutes': 30,
                'calories_burned': 300,
                'date': datetime.utcnow().date().isoformat()
            },
            {
                'user_id': user_ids[2],
                'activity_type': 'Cycling',
                'duration_minutes': 45,
                'calories_burned': 400,
                'date': datetime.utcnow().date().isoformat()
            }
        ])

        # Create leaderboard entries
        db.leaderboard.insert_many([
            {
                'user_id': user_ids[0],
                'score': 1000,
                'rank': 1
            },
            {
                'user_id': user_ids[2],
                'score': 950,
                'rank': 2
            }
        ])

        # Create workout suggestions
        db.workouts.insert_many([
            {
                'user_id': user_ids[1],
                'suggestion': 'Try HIIT for 20 minutes.',
                'created_at': datetime.utcnow()
            },
            {
                'user_id': user_ids[3],
                'suggestion': 'Yoga and meditation.',
                'created_at': datetime.utcnow()
            }
        ])

        # Ensure unique index on email
        db.users.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully using pymongo.'))
