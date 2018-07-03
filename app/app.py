from flask import request
from app.models import db, HotelDetails
from flask_api import FlaskAPI
from app.jwthandler import auth_required


def create_app(module='app.instance.config.TestingConfig'):
    """This exportable method wraps the routes """
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(module)
    app.debug = True
    db.init_app(app)

    @app.route('/hotels/v1/list')
    @auth_required
    def hotel_list():
        """ Return a JSON response """
        # user_id = auth.get_current_user()
        if request.method == 'GET':
            # pagination limit
            results = HotelDetails.get_all()
            limit = int(request.args.get('record', 5))
            page = int(request.args.get('page', 1))

            if results.all():
                results_data = results
                limit = 100 if int(limit) > 100 else limit
                # serialize result objects to json
                result_list = []
                paginated_data = results_data.paginate(page, int(limit), False).items
                for item in paginated_data:
                    if callable(getattr(item, 'to_json')):
                        result = item.to_json()
                        result_list.append(result)
                return {'message': result_list}

    return app

