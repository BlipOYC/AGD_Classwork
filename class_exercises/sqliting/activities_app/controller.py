import sqlalchemy as sa
import sqlalchemy.orm as so

from models import Person, Activity


class Controller:
    def __init__(self, db_location = 'sqlite:///activities.sqlite'):
        self.engine = sa.create_engine(db_location)

    def get_person_activities(self, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person).where(Person.first_name == first_name and Person.last_name == last_name)
            user = session.scalar(stmt)
            activities = user.activities
            activity_names = [activity.name for activity in activities]
        return activity_names

    def get_all_people(self):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person).order_by(Person.first_name, Person.last_name)
            all_people = session.scalars(stmt)
            all_people_return = all_people.all()
        return all_people_return

    def get_all_activities(self):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Activity).order_by(Activity.name)
            all_activities = session.scalars(stmt)
            all_activities_return = all_activities.all()
        return all_activities_return

    def add_person(self, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.insert(Person).values(first_name=first_name, last_name=last_name)
            session.execute(stmt)
            session.commit()

    def add_activity(self, name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.insert(Activity).values(name=name)
            session.execute(stmt)
            session.commit()



if __name__ == '__main__':
    controller = Controller()