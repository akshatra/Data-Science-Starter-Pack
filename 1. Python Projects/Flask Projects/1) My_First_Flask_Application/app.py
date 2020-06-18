from flask import Flask  ##we are importing Flask class.


##__name__ represents the name of the currently working module.
app=Flask(__name__) ##setting the app variable to an instance of the flask class.

##Decorators allows us to add extra features to some existing functions from same or different module.
@app.route("/") ##This is a decorator.
def home():
    return '<h1>You are in the root !<h1>'


if __name__=="__main__":  ##only true if we run this module.
    app.run(bebug=True)
