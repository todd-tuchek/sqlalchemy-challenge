
#Import Dependencies 
#-------------------
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#-------------------
# CREATE DATABASE
#-------------------

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model...use 'automap_base()' to reflect the tables into classes
Base = automap_base()

# reflect the tables...Base.prepare method
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#-------------------
# FLASK SETUP
#-------------------

app = Flask(__name__)

#-------------------
# FLASK ROUTES
#-------------------

@app.route("/")
def welcome(): 
   """List the available API routes:"""
    return(
     f"Available Routes:<br>"
     f"/api/v1.0/precipitation<br/>"
     f"/api/v1.0/stations<br/>"
     f"/api/v1.0/tobs<br/>"
     f"/api/v1.0/<start><br/>"
     f"/api/v1.0/<start>/<end>"
    )

# Create a route to percipitation
@app.route("/api/v1.0/precipitation")
def precipitation(): 
    # Create session (link) from python to the DataBase
    session = Session(engine)

    """Return a list of dates and precipitations"""
    # Query Precipitatiion 
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    #Convert list of tuples into normal list
    prcp_all = []
    for date, precip in results:
        date_dict = {}
        date_dict[date] = precip
        prcp_all.append(date_dict)
    return jsonify(prcp_all)

# Create route to Stations
@app.route("/api/v1.0/precipitation")
def stations(): 
    # Create our session (link) from Python to the Database
    session = Session(engine)

    """Return a list of all the stations in the Database"""
    # Query all stations from DB
    results = session.query(Station.station).all()

    session.close()

    #Convert the list of station tuples into a normal list "Use .ravel"
    all_stations = list(np
    
    return jsonify(all_stations)

# Create route to TOBS
@app.route("/api/v1.0/tobs")
def tobs(): 
    # Create session link from Python to Database
    session = Session(engine)

    """Retuen a list of tobs (temp observation) for the LAST YEAR of data in the table"""
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).\
        filter(Measurement.date >= query_date).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)

# Create route to START ... When given the START only...
@app.route("/api/v1.0/<start>")
def start(start):
    #Create path to link from Python to Database
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs),\
                            func.avg(Measurement.tobs),\
                            func.max(Measurement.tobs)).\
                            filter(Measurement.date >= startDate.first()
    session.close()

    #Convert list of tuples into normal list
    start_result = list(np.ravel(results))
    return jsonify(start_result)

# When given the start and the end date,
# calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>/<end>")
def startend(startDate, endDate):
    # Create session from Python to Database
    seassion = Session(engine)
    results = session.query(func.min(Measurement.tobs),\
                            func.avg(Measurement.tobs),\
                            func.max(Measurement.tobs)).\
                            filter(Measurement.date >= startDate).\
                            filter(Measurement.date <= endDate).first()]
    session.close()

    # Convert list of tuples into normal list
    startend_result = list(np.ravel(results))
    return jsonify(startend_result)

if __name__ == '__main__':
    app.run(debug=True)


                                



    