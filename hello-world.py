from flask import Flask 


#This line imports the Flask class from the flask module, which is necessary to create a Flask application.
app = Flask(__name__) 


#This line initializes a new Flask application instance. The __name__ variable is passed to the Flask constructor,
#which helps Flask determine the root path of the application.


@app.route('/') 


#This line is a decorator that defines a route for the application.
# The '/' route is the root URL of the application, and when a user accesses this URL, the function immediately following this decorator will be executed.
def hello_world(): # A function named hello_world is defined, which will be called when the root URL is accessed.
    return 'Hello, World!'  

    
if __name__ == '__main__': # This line checks if the script is being run directly (as the main program) rather than imported as a module in another script.
    app.run()