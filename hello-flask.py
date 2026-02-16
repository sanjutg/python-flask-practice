from flask import Flask
app : Flask = Flask(import_name = __name__) #Creates a Flask application instance and sets the project’s root using __name__.
@app.route(rule='/') #Defines a route for the root URL ('/'). When a user accesses this URL, the function immediately following this decorator will be executed.
def index() -> Literal['<h1> Hello, Flask! </h1>']:  #Defines a function named index that will be called when the root URL is accessed. The function returns an HTML string that will be displayed in the user's browser. In this case, it returns a heading with the text "Hello, Flask!".
    return '<h1> Hello, Flask! </h1>'  #The return statement sends the HTML string back to the client (the user's browser) as the response to the HTTP request made to the root URL.
@app.route(rule='/hello')
def hello() -> Literal['<h1> Hello, World! </h1>']:  #Defines another route for the URL '/hello'. When a user accesses this URL, the hello function will be executed, which returns an HTML string that says "Hello, World!".
    return '<h1> Hello, World! </h1>' 
@app.route(rule='/hello/<name>')
def hello_name(name: str) -> str: #Defines a dynamic route that includes a variable part <name>. When a user accesses a URL like '/hello/John', the hello_name function will be executed, and the value 'John' will be passed as an argument to the function. The function then returns an HTML string that greets the user by name.
    return f'<h1> Hello, {name}! </h1>' #The return statement uses an f-string to format the HTML string with the value of the name variable, allowing for personalized greetings based on the URL accessed by the user.
if __name__ == '__main__':
    app.run()


    #     Using Literal here is over-specific and not commonly done in basic Flask apps.

    # 💡 Simple Difference Summary
    # Part	Purpose	Affects Runtime?
    # return '...'	Sends data back	✅ Yes
    # -> Literal[...]	Type hint	❌ No

    # So if you remove Literal completely:

    # Your app will still work perfectly. The type hints are just for developers and tools, and they don't change how the code runs.