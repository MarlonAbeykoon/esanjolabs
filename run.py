import sys
from app.app import create_app

environments = {
    'test': 'App.instance.config.TestingConfig'
}

try:
    if sys.argv[1] in environments.keys():
        app = create_app(environments.get(sys.argv[1]))
        # Run the app
        app.run()
    else:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print ('Usage: python run.py <environment>')

except IndexError:
    # Handle missing arguments or more unfriendly options than required
    print ("Missing options: use [python run.py -h]")
exit()