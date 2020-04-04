from datetime import timedelta
from random import randint
import pytz

from django.core.management.base import BaseCommand

import faker

from user_activity.models import User, ActivityPeriod


class Command(BaseCommand):
    help = 'Generates some random fake data.'
    faker.Faker.seed(0)
    fake = faker.Faker()

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def create_user(self):
        profile = self.fake.simple_profile()
        return User.objects.create_user(
            id=self.fake.bothify(text='??#?##?##'),
            username=profile["username"],
            password="123",
            email=profile["mail"],
            is_active=True,
            timezone=self.fake.timezone(),
            real_name=profile["name"]
        )

    def create_max_of_10_activity_periods(self, user):
        for _ in range(0, randint(0, 10)):
            self.create_activity_period(user)

    def create_activity_period(self, user):
        start_time = self.fake.date_time(
            tzinfo=pytz.timezone(self.fake.timezone()))
        end_time = start_time + timedelta(minutes=30)
        activity_period = ActivityPeriod.objects.create(
            start_time=start_time,
            end_time=end_time,
            user=user
        )
        activity_period.save()

    def handle(self, *args, **options):
        for i in range(0, options['count']):
            print('Created bummy %d users data out of %d...' %
                  (i+1, options["count"]))
            user = self.create_user()
            self.create_max_of_10_activity_periods(user)
