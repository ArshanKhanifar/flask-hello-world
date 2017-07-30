# flask hello world


# import the Flask class form the flask package

from flask import Flask

# create the application object 

app = Flask(__name__)


# use decorators to link the function to a url 

@app.route("/")

def something():
	return "this is the root" 

@app.route("/hello")


#define the view using a fucntion, which returns a string

def hello_world():
	return "this is the hello" 


# start the development server using the run() method

if __name__ == "__main__":
	app.run()







