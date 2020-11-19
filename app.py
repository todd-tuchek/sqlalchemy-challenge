
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

