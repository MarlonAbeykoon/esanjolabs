#!/usr/bin/env python
from flask_script import Manager
from app.models import db, HotelDetails
from app.app import create_app


manager = Manager(create_app)


@manager.command
def createdb(testdata=True):
    """Initializes the database """
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        if testdata:
            for i in range(1,50):
                hotel_details = HotelDetails(name='The Apartments Dubai World Trade Centre', address='United Arab Emirates',
                                             badge='Clean Rooms', coordinate='25.224747', cost=590,
                                             image='https://res.cloudinary.com/esanjolabs/image/upload/hotels/3e4564321d5bbc209fcf215f25404de4.jpg',
                                             neighbourhood='Palm Jumeirah',rating=9, star_rating=5,type='hotel',id=i,
                                             date_created='2018-07-03 00:00:00', date_modified='2018-07-03 00:00:00')
                db.session.add(hotel_details)
                db.session.commit()

if __name__ == '__main__':
    manager.run()