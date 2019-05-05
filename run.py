#-----------------------------------------------------------------------------
# Get our components
# You may eventually wish to put these in their own directories and then load
from bottle import run
import routes, controller
# import populate_data # import to generate db

# It might be a good idea to move the following settings to a config file and then load them

# # development
host = 'localhost'
debug = True
reloader = True
# remember to change db path in helperMethods

# production
# host = '0.0.0.0' # IP address or 0.0.0.0
# debug = False
# reloader = False
# remember to change db path in helperMethods

port = 8080 # change to the appropriate port to host

#-----------------------------------------------------------------------------

#Run the server if using this file directly
if __name__ == '__main__':
    run(host=host, port=port, debug=debug, reloader=reloader)

# http://localhost:8080/
