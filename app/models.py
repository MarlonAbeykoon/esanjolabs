from flask_sqlalchemy import sqlalchemy,SQLAlchemy

db = SQLAlchemy()
class_mapper = sqlalchemy.orm.class_mapper
# migrate = Migrate(app, db)


class Base(db.Model):
    """ Base model from which other models will inherit from """
    __abstract__ = True

    # primary keys, created_date, modified_date etc can be set here to use in updates and inserts
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    # save, delete methods can be written here

    def to_json(self):
        """ Serializes objects to json """
        json_dict = dict()
        result_list = []
        for property in class_mapper(self.__class__).iterate_properties:
            if property.key == 'user':
                continue
            if property.key == 'items':
                items = getattr(self, property.key)
                # serialize objects to json format
                for item in items:
                    if callable(getattr(item, 'to_json')):
                        result = item.to_json()
                        result_list.append(result)
                json_dict[property.key] = result_list
                continue

            json_dict[property.key] = getattr(self, property.key)

        return json_dict

class HotelDetails(Base):
    """Maps to the hoteldetails table """
    __tablename__ = 'hoteldetails'
    name = db.Column(db.String(256))
    address = db.Column(db.String(256))
    badge = db.Column(db.String(256))
    coordinate = db.Column(db.String(256))
    cost = db.Column(db.FLOAT)
    image = db.Column(db.String(256))
    neighbourhood = db.Column(db.String(256))
    rating = db.Column(db.Integer)
    star_rating = db.Column(db.Integer)
    type = db.Column(db.String(256))


    @staticmethod
    def get_all():
        """Returns all data """
        return HotelDetails.query.filter_by()