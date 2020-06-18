###1)create main file.
###2)create database file.
###3)create index file in templates.
###4)

from flask import Flask, render_template, request, redirect, url_for
from database import Base, Restaurant
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engine = create_engine("sqlite:///restaurantmenu.db")   ###this will create a database
Base.metadata.bind = engine

@app.route("/")
def rootPage():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurants = session.query(Restaurant).all()
    return render_template("index.html", restaurants=restaurants)

@app.route("/restaurants/new", methods=['GET', 'POST'])
def addNewRestaurant():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == 'POST':
        newRestaurant = Restaurant(
            name=request.form['name'],
            address = request.form['address']
        )
        session.add(newRestaurant)
        session.commit()
        return redirect(url_for('rootPage'))
    else:
        return render_template('newRestaurant.html')

@app.route('/restaurants/<int:restaurant_id>/details')
def viewRestaurant(restaurant_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    return render_template('restaurantDetails.html', restaurant=restaurant)

if __name__ == "__main__":
    app.run()