# from sys import excelsption
from types import NoneType
from unittest import result
from xxlimited import Str
from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, func
from sqlalchemy.dialects.postgresql import JSON
# from flask_wtf.csrf import CSRFProtect
# from flask_wtf import csrf
import requests
from werkzeug.security import generate_password_hash, check_password_hash
import json
import time
from datetime import datetime, timezone, timedelta
import math
import random


app = Flask(__name__)

# http://192.168.225.48:8080
cors = CORS(app, resources={r'/*': {"origins": "http://betatestrivalofstate.rf.gd"}})
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

# postgresql://postgres:G1234567@localhost:5432/rival_base
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:G1234567@localhost:5432/rival_base'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://super:G1234567@Tato1999-3591.postgres.pythonanywhere-services.com:13591/rival_base'
# postgres://test_db_pciz_user:zDzvlEL6DYjCzmi1VH3zwdW4AQAnsrdj@dpg-ckdu0tljhfbs73agl9f0-a.oregon-postgres.render.com/test_db_pciz
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://[DB_USER]:[DB_PASSWORD]@[DB_IP]/[DB_NAME]?unix_socket=/cloudsql/[CONNECTION_NAME]"'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # Session(app)
# csrf = CSRFProtect(app)
# csrf.init_app(app)
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    permission = db.Column(db.Integer)
    name = db.Column(db.String(100), nullable = False)
    second_name = db.Column(db.String(100), nullable = False)
    energy = db.Column(db.Integer, nullable = False)
    money = db.Column(db.BigInteger, nullable = False)
    res_region = db.Column(db.String(200), nullable = False)
    res_state = db.Column(db.String(200), nullable = False)
    level = db.Column(db.Integer, nullable = False)
    experience = db.Column(db.Integer, nullable = False)
    strenght = db.Column(db.Integer, nullable = False)
    education = db.Column(db.Integer, nullable = False)
    endurance = db.Column(db.Integer, nullable = False)
    premium = db.Column(db.Integer, nullable = False)
    friends_count = db.Column(db.Integer, nullable = False)
    damage = db.Column(db.Integer, nullable = False)
    working_experience = db.Column(db.Integer, nullable = False)
    max_experience = db.Column(db.Integer, nullable = False)
    mail = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(100))
    living_region = db.Column(db.String)
    current_factory = db.Column(db.Integer)
    last_fill = db.Column(db.Integer)
    last_fill_hour = db.Column(db.Integer)
    last_fill_day = db.Column(db.Integer)
    refilClickTime = db.Column(db.Integer)
    last_fill_manual = db.Column(db.Integer)
    last_fill_hour_manual = db.Column(db.Integer)
    last_fill_day_manual = db.Column(db.Integer)
    manualFilling = db.Column(db.Integer)
    autoWork = db.Column(db.Integer)
    lastFillDate = db.Column(db.TIMESTAMP)
    autoWorkStart = db.Column(db.TIMESTAMP)
    autoRefill = db.Column(db.TIMESTAMP)
    Gold_Factory = db.Column(db.Integer)
    Oil_Factory = db.Column(db.Integer)
    Silver_Factory = db.Column(db.Integer)
    Iron_Factory = db.Column(db.Integer)
    Coal_Factory = db.Column(db.Integer)
    tiger_1 = db.Column(db.Integer)
    tiger_2 = db.Column(db.Integer)
    t_90 = db.Column(db.Integer)
    drone = db.Column(db.Integer)
    haimars = db.Column(db.Integer)
    wolfram = db.Column(db.Integer)
    oxygen = db.Column(db.Integer)
    fly = db.Column(JSON)
    factorys = relationship('Factory', backref='aut')
    party = db.Column(db.Integer)

    # def __repr__(self):
    #     return f'{self.id}'
app.app_context().push()
db.create_all()

class Region(UserMixin, db.Model):
    __tablename__ = 'region'
    id = db.Column(db.String(), primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    defColor = db.Column(db.String(150), nullable = False)
    color = db.Column(db.String(150), nullable = False)
    educationIndex = db.Column(db.Integer(), nullable = False)
    medicinIndex = db.Column(db.Integer(), nullable = False)
    militaryIndex = db.Column(db.Integer(), nullable = False)
    developmentIndex = db.Column(db.Integer(), nullable = False)
    teachersCount = db.Column(db.Integer(), nullable = False)
    doctorsCount = db.Column(db.Integer(), nullable = False)
    hesCount = db.Column(db.Integer(), nullable = False)
    clinicsCount = db.Column(db.Integer(), nullable = False)
    schoolsCount = db.Column(db.Integer(), nullable = False)
    militaryBases = db.Column(db.Integer(), nullable = False)
    generalCount = db.Column(db.Integer(), nullable = False)
    residendalCount = db.Column(db.Integer(), nullable = False)
    liverCount = db.Column(db.Integer(), nullable = False)
    country = db.Column(db.String(), nullable = False)
    gerb = db.Column(db.String(), nullable = False)
    factory = db.Column(db.Integer(), nullable = False)
    party = db.Column(db.Integer(), nullable = False)
    house = db.Column(db.Integer(), nullable = False)
    defenceSystems = db.Column(db.Integer(), nullable = False)
    rect = db.Column(JSON)
    # max_experience = db.Column(db.Integer, nullable = False)
    # mail = db.Column(db.String(100), nullable = False, unique = True)
    # password = db.Column(db.String(100))

    # def __repr__(self):
    #     return f'{self.id}'
app.app_context().push()
db.create_all()

class State(UserMixin, db.Model):
    __tablename__ = 'state'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=True)
    defColor = db.Column(db.String(150))
    color = db.Column(db.String(150))
    teachersCount = db.Column(db.Integer(), nullable=True)
    doctorsCount = db.Column(db.Integer(), nullable=True)
    hesCount = db.Column(db.Integer(), nullable=True)
    clinicsCount = db.Column(db.Integer(), nullable=True)
    schoolsCount = db.Column(db.Integer(), nullable=True)
    militaryBases = db.Column(db.Integer(), nullable=True)
    generalCount = db.Column(db.Integer(), nullable=True)
    residendalCount = db.Column(db.Integer(), nullable=True)
    liverCount = db.Column(db.Integer(), nullable=True)
    country = db.Column(db.String())
    gerb = db.Column(db.String(), nullable=True)
    factory = db.Column(db.Integer(), nullable=True)
    party = db.Column(db.Integer(), nullable=True)
    house = db.Column(db.Integer(), nullable=True)
    defenceSystems = db.Column(db.Integer(), nullable=True)
    election = db.Column(JSON)
    parlament = db.Column(JSON)
    regions = db.Column(JSON)
    laws = db.Column(JSON)

app.app_context().push()
db.create_all()

class Election(UserMixin, db.Model):
    __tablename__ = 'election'
    id = db.Column(db.Integer, primary_key = True)
    party = db.Column(JSON)
    state = db.Column(db.String)
    voter = db.Column(JSON)

app.app_context().push()
db.create_all()

class Factory(UserMixin, db.Model):
    __tablename__ = 'Factory'
    id = db.Column(db.Integer, primary_key = True)
    owner = db.Column(db.Integer, ForeignKey('user.id'))
    region = db.Column(db.String, ForeignKey('region.id'))
    level = db.Column(db.Integer, nullable = False)
    organization = db.Column(db.String(100), nullable = False)
    type = db.Column(db.String(100), nullable = False)
    wage_type = db.Column(db.Integer, nullable = False)
    potentional_wage = db.Column(db.BigInteger, nullable = False)
    real_wage = db.Column(db.String(200), nullable = False)
    workers_amount = db.Column(db.Integer, nullable = False)
    workers_count = db.Column(db.Integer, nullable = False)
    experience = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String, nullable = False)
    factory_icon = db.Column(db.String, nullable = False)

    factorys_owner = relationship('User', backref='aut')
    factorys_region = relationship('Region', backref='aut_region')
    # def __repr__(self):
    #     return f'{self.id}'
app.app_context().push()
db.create_all()

class WeaponPrice(db.Model,UserMixin):
    # __tablename__='weapon_price'
    id = db.Column(db.Integer, primary_key = True)
    taiger_1=db.Column(db.String)
    taiger_2=db.Column(db.String)
    t_90=db.Column(db.String)
    haimars=db.Column(db.String)
    drone=db.Column(db.String)
    wolfram=db.Column(db.String)

app.app_context().push()
db.create_all()

class Market(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    oil = db.Column(JSON)
    coal = db.Column(JSON)
    iron = db.Column(JSON)
    silver = db.Column(JSON)
    oxygen_market = db.Column(JSON)
    taiger_1_market = db.Column(JSON)
    taiger_2_market = db.Column(JSON)
    t_90_market = db.Column(JSON)
    haimars_market = db.Column(JSON)
    drone_market = db.Column(JSON)
    wolfram_market = db.Column(JSON)

app.app_context().push()
db.create_all()


class Party(UserMixin, db.Model):
    __tablename__ = 'party'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150))
    region = db.Column(db.String())
    state = db.Column(db.String())
    # salary = db.Column(db.Integer())
    gold = db.Column(db.Integer())
    budget = db.Column(db.Integer())
    members = db.Column(JSON)
    waiter = db.Column(JSON)

app.app_context().push()
db.create_all()


def create_weapon_price_base():
    WeaponPrice_info=WeaponPrice(
        taiger_1='28800,3456,2304,2016',
        taiger_2='28800,3456,2304,1814',
        t_90='28800,3456,2304,1.612',
        wolfram='576,2304,2304,2304,2304,604',
        drone='5760,1,604',
        haimars='5760,1,604'
    )
    db.session.add(WeaponPrice_info)
    db.session.commit()
# create_weapon_price_base()


#Add Market Resource ln 202 - ln 864


@app.route('/add_market_oil_json', methods=["GET","POST"])
def addMarketJson():
    result = request.get_json()
    print(result)
    user_info = db.session.query(User).get(result["id"])
    # print(market_info.oil['oil']['amount'])
    try:
        market_info = db.session.query(Market).get(result['id'])
        if (int(result['oil'])) <= int(user_info.Oil_Factory):
            market_info.oil = {
                    'id': user_info.id,
                    'name': user_info.name,
                    'oil': {
                        'amount': int(market_info.oil['oil']['amount']) + int(result['oil']),
                        'price': result['price']
                    }
                }
            user_info.Oil_Factory = user_info.Oil_Factory - int(result['oil'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], oil = {
        
            'id': user_info.id,
            'name': user_info.name,
            'oil': {
                'amount': int(result['oil']),
                'price': result['price']
            }
        },
        coal = {'id': user_info.id,'name': user_info.name,'coal': {'amount': 0,'price': 0}},
        iron = {'id': user_info.id,'name': user_info.name,'iron': {'amount': 0,'price': 0}},
        silver = {'id': user_info.id,'name': user_info.name,'silver': {'amount': 0,'price': 0}},
        oxygen_market = {'id': user_info.id,'name': user_info.name,'oxygen': {'amount': 0,'price': 0}},
        taiger_1_market = {'id': user_info.id,'name': user_info.name,'taiger_1': {'amount': 0,'price': 0}},
        taiger_2_market = {'id': user_info.id,'name': user_info.name,'taiger_2': {'amount': 0,'price': 0}},
        t_90_market = {'id': user_info.id,'name': user_info.name,'t_90': {'amount': 0,'price': 0}},
        haimars_market = {'id': user_info.id,'name': user_info.name,'haimars': {'amount': 0,'price': 0}},
        drone_market = {'id': user_info.id,'name': user_info.name,'drone': {'amount': 0,'price': 0}},
        wolfram_market = {'id': user_info.id,'name': user_info.name,'wolfram': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.Oil_Factory = user_info.Oil_Factory - int(result['oil'])
        db.session.commit()
        return{"Respone": "add Succes"}

    return {'test':"DONE"}

@app.route('/add_market_coal_json', methods=["GET","POST"])
def addCoalMarketJson():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    print("TEsaadasdasdsa")
    
    try:
        market_info = db.session.query(Market).get(result['id'])
        if (int(result['coal'])) <= int(user_info.Coal_Factory):
            market_info.coal = {
                    'id': user_info.id,
                    'name': user_info.name,
                    'coal': {
                        'amount': int(market_info.coal['coal']['amount']) + int(result['coal']),
                        'price': result['price']
                    }
                }
            user_info.Coal_Factory = user_info.Coall_Factory - int(result['coal'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], coal = {
        
            'id': user_info.id,
            'name': user_info.name,
            'coal': {
                'amount': int(result['coal']),
                'price': result['price']
            }
        },
        oil = {'id': user_info.id,'name': user_info.name,'oil': {'amount': 0,'price': 0}},
        iron = {'id': user_info.id,'name': user_info.name,'iron': {'amount': 0,'price': 0}},
        silver = {'id': user_info.id,'name': user_info.name,'silver': {'amount': 0,'price': 0}},
        oxygen_market = {'id': user_info.id,'name': user_info.name,'oxygen': {'amount': 0,'price': 0}},
        taiger_1_market = {'id': user_info.id,'name': user_info.name,'taiger_1': {'amount': 0,'price': 0}},
        taiger_2_market = {'id': user_info.id,'name': user_info.name,'taiger_2': {'amount': 0,'price': 0}},
        t_90_market = {'id': user_info.id,'name': user_info.name,'t_90': {'amount': 0,'price': 0}},
        haimars_market = {'id': user_info.id,'name': user_info.name,'haimars': {'amount': 0,'price': 0}},
        drone_market = {'id': user_info.id,'name': user_info.name,'drone': {'amount': 0,'price': 0}},
        wolfram_market = {'id': user_info.id,'name': user_info.name,'wolfram': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.Coal_Factory = user_info.Coal_Factory - int(result['coal'])
        db.session.commit()
        return{"Respone": "add Succes"}

@app.route('/add_market_iron_json', methods=["GET","POST"])
def addIronMarketJson():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    
    try:

        market_info = db.session.query(Market).get(result['id'])
        if (int(result['iron'])) <= int(user_info.Iron_Factory):
            market_info.iron = {
                    'id': user_info.id,
                    'name': user_info.name,
                    'iron': {
                        'amount': int(market_info.iron['iron']['amount']) + int(result['iron']),
                        'price': result['price']
                    }
                }
            user_info.Iron_Factory = user_info.Iron_Factory - int(result['iron'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], iron = {
        
            'id': user_info.id,
            'name': user_info.name,
            'iron': {
                'amount': result['iron'],
                'price': result['price']
            }
        },
        oil = {'id': user_info.id,'name': user_info.name,'oil': {'amount': 0,'price': 0}},
        coal = {'id': user_info.id,'name': user_info.name,'coal': {'amount': 0,'price': 0}},
        silver = {'id': user_info.id,'name': user_info.name,'silver': {'amount': 0,'price': 0}},
        oxygen_market = {'id': user_info.id,'name': user_info.name,'oxygen': {'amount': 0,'price': 0}},
        taiger_1_market = {'id': user_info.id,'name': user_info.name,'taiger_1': {'amount': 0,'price': 0}},
        taiger_2_market = {'id': user_info.id,'name': user_info.name,'taiger_2': {'amount': 0,'price': 0}},
        t_90_market = {'id': user_info.id,'name': user_info.name,'t_90': {'amount': 0,'price': 0}},
        haimars_market = {'id': user_info.id,'name': user_info.name,'haimars': {'amount': 0,'price': 0}},
        drone_market = {'id': user_info.id,'name': user_info.name,'drone': {'amount': 0,'price': 0}},
        wolfram_market = {'id': user_info.id,'name': user_info.name,'wolfram': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.Iron_Factory = user_info.Iron_Factory - int(result['iron'])
        db.session.commit()
        return{"Respone": "add Succes"}

@app.route('/add_market_silver_json', methods=["GET","POST"])
def addSilverMarketJson():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    
    try:

        market_info = db.session.query(Market).get(result['id'])
        if int(result['silver']) <= int(user_info.Silver_Factory):
            market_info.silver = {
                    'id': user_info.id,
                    'name': user_info.name,
                    'silver': {
                        'amount': int(market_info.silver['silver']['amount']) + int(result['silver']),
                        'price': result['price']
                    }
                }
            user_info.Silver_Factory = user_info.Silver_Factory - int(result['silver'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], silver = {
        
            'id': user_info.id,
            'name': user_info.name,
            'silver': {
                'amount': result['silver'],
                'price': result['price']
            }
        },
        oil = {'id': user_info.id,'name': user_info.name,'oil': {'amount': 0,'price': 0}},
        coal = {'id': user_info.id,'name': user_info.name,'coal': {'amount': 0,'price': 0}},
        iron = {'id': user_info.id,'name': user_info.name,'iron': {'amount': 0,'price': 0}},
        oxygen_market = {'id': user_info.id,'name': user_info.name,'oxygen': {'amount': 0,'price': 0}},
        taiger_1_market = {'id': user_info.id,'name': user_info.name,'taiger_1': {'amount': 0,'price': 0}},
        taiger_2_market = {'id': user_info.id,'name': user_info.name,'taiger_2': {'amount': 0,'price': 0}},
        t_90_market = {'id': user_info.id,'name': user_info.name,'t_90': {'amount': 0,'price': 0}},
        haimars_market = {'id': user_info.id,'name': user_info.name,'haimars': {'amount': 0,'price': 0}},
        drone_market = {'id': user_info.id,'name': user_info.name,'drone': {'amount': 0,'price': 0}},
        wolfram_market = {'id': user_info.id,'name': user_info.name,'wolfram': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.Silver_Factory = user_info.Silver_Factory - int(result['silver'])
        db.session.commit()
        return{"Respone": "add Succes"}

@app.route('/add_market_oxygen_json', methods=["GET","POST"])
def addOxygenMarketJson():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    
    try:

        market_info = db.session.query(Market).get(result['id'])
        if int(result['oxygen']) <= int(user_info.oxygen):
            market_info.oxygen_market = {
                    'id': user_info.id,
                    'name': user_info.name,
                    'oxygen': {
                        'amount': int(market_info.oxygen_market['oxygen']['amount']) + int(result['oxygen']),
                        'price': result['price']
                    }
                }
            user_info.oxygen = user_info.oxygen - int(result['oxygen'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], oxygen_market = {
        
            'id': user_info.id,
            'name': user_info.name,
            'oxygen': {
                'amount': result['oxygen'],
                'price': result['price']
            }
        },
        oil = {'id': user_info.id,'name': user_info.name,'oil': {'amount': 0,'price': 0}},
        coal = {'id': user_info.id,'name': user_info.name,'coal': {'amount': 0,'price': 0}},
        iron = {'id': user_info.id,'name': user_info.name,'iron': {'amount': 0,'price': 0}},
        silver = {'id': user_info.id,'name': user_info.name,'silver': {'amount': 0,'price': 0}},
        taiger_1_market = {'id': user_info.id,'name': user_info.name,'taiger_1': {'amount': 0,'price': 0}},
        taiger_2_market = {'id': user_info.id,'name': user_info.name,'taiger_2': {'amount': 0,'price': 0}},
        t_90_market = {'id': user_info.id,'name': user_info.name,'t_90': {'amount': 0,'price': 0}},
        haimars_market = {'id': user_info.id,'name': user_info.name,'haimars': {'amount': 0,'price': 0}},
        drone_market = {'id': user_info.id,'name': user_info.name,'drone': {'amount': 0,'price': 0}},
        wolfram_market = {'id': user_info.id,'name': user_info.name,'wolfram': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.oxygen = user_info.oxygen - int(result['oxygen'])
        db.session.commit()
        return{"Respone": "add Succes"}

@app.route('/add_market_taiger_1_json', methods=["GET","POST"])
def addTaiger1MarketJson():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    
    try:
        market_info = db.session.query(Market).get(result['id'])
        if int(result['taiger_1']) <= int(user_info.tiger_1):
            market_info.taiger_1_market = {
                    'id': user_info.id,
                    'name': user_info.name,
                    'taiger_1': {
                        'amount': int(market_info.taiger_1_market['taiger_1']['amount']) + int(result['taiger_1']),
                        'price': result['price']
                    }
                }
            user_info.tiger_1 = user_info.tiger_1 - int(result['taiger_1'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], taiger_1_market = {
        
            'id': user_info.id,
            'name': user_info.name,
            'taiger_1': {
                'amount': result['taiger_1'],
                'price': result['price']
            }
        },
        oil = {'id': user_info.id,'name': user_info.name,'oil': {'amount': 0,'price': 0}},
        coal = {'id': user_info.id,'name': user_info.name,'coal': {'amount': 0,'price': 0}},
        iron = {'id': user_info.id,'name': user_info.name,'iron': {'amount': 0,'price': 0}},
        silver = {'id': user_info.id,'name': user_info.name,'silver': {'amount': 0,'price': 0}},
        oxygen_market = {'id': user_info.id,'name': user_info.name,'oxygen': {'amount': 0,'price': 0}},
        taiger_2_market = {'id': user_info.id,'name': user_info.name,'taiger_2': {'amount': 0,'price': 0}},
        t_90_market = {'id': user_info.id,'name': user_info.name,'t_90': {'amount': 0,'price': 0}},
        haimars_market = {'id': user_info.id,'name': user_info.name,'haimars': {'amount': 0,'price': 0}},
        drone_market = {'id': user_info.id,'name': user_info.name,'drone': {'amount': 0,'price': 0}},
        wolfram_market = {'id': user_info.id,'name': user_info.name,'wolfram': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.tiger_1 = user_info.tiger_1 - int(result['taiger_1'])
        db.session.commit()
        return{"Respone": "add Succes"}

@app.route('/add_market_taiger_2_json', methods=["GET","POST"])
def addTaiger2MarketJson():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    
    try:
        market_info = db.session.query(Market).get(result['id'])
        if (int(result['taiger_2'])) <= int(user_info.tiger_2):
            market_info.taiger_2_market = {
                    'id': user_info.id,
                    'name': user_info.name,
                    'taiger_2': {
                        'amount': int(market_info.taiger_2_market['taiger_2']['amount']) + int(result['taiger_2']),
                        'price': result['price']
                    }
                }
            user_info.tiger_2 = user_info.tiger_2 - int(result['taiger_2'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], taiger_2_market = {
        
            'id': user_info.id,
            'name': user_info.name,
            'taiger_2': {
                'amount': result['taiger_2'],
                'price': result['price']
            }
        },
        oil = {'id': user_info.id,'name': user_info.name,'oil': {'amount': 0,'price': 0}},
        coal = {'id': user_info.id,'name': user_info.name,'coal': {'amount': 0,'price': 0}},
        iron = {'id': user_info.id,'name': user_info.name,'iron': {'amount': 0,'price': 0}},
        silver = {'id': user_info.id,'name': user_info.name,'silver': {'amount': 0,'price': 0}},
        oxygen_market = {'id': user_info.id,'name': user_info.name,'oxygen': {'amount': 0,'price': 0}},
        taiger_1_market = {'id': user_info.id,'name': user_info.name,'taiger_1': {'amount': 0,'price': 0}},
        t_90_market = {'id': user_info.id,'name': user_info.name,'t_90': {'amount': 0,'price': 0}},
        haimars_market = {'id': user_info.id,'name': user_info.name,'haimars': {'amount': 0,'price': 0}},
        drone_market = {'id': user_info.id,'name': user_info.name,'drone': {'amount': 0,'price': 0}},
        wolfram_market = {'id': user_info.id,'name': user_info.name,'wolfram': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.tiger_2 = user_info.tiger_2 - int(result['taiger_2'])
        db.session.commit()
        return{"Respone": "add Succes"}

@app.route('/add_market_t_90_json', methods=["GET","POST"])
def addT90MarketJson():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    
    try:
        market_info = db.session.query(Market).get(result['id'])
        if (int(result['t_90'])) <= int(user_info.t_90):
            market_info.t_90_market = {
                    'id': user_info.id,
                    'name': user_info.name,
                    't_90': {
                        'amount': int(market_info.t_90_market['t_90']['amount']) + int(result['t_90']),
                        'price': result['price']
                    }
                }
            user_info.t_90 = user_info.t_90 - int(result['t_90'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], t_90_market = {
        
            'id': user_info.id,
            'name': user_info.name,
            't_90': {
                'amount': result['t_90'],
                'price': result['price']
            }
        },
        oil = {'id': user_info.id,'name': user_info.name,'oil': {'amount': 0,'price': 0}},
        coal = {'id': user_info.id,'name': user_info.name,'coal': {'amount': 0,'price': 0}},
        iron = {'id': user_info.id,'name': user_info.name,'iron': {'amount': 0,'price': 0}},
        silver = {'id': user_info.id,'name': user_info.name,'silver': {'amount': 0,'price': 0}},
        oxygen_market = {'id': user_info.id,'name': user_info.name,'oxygen': {'amount': 0,'price': 0}},
        taiger_1_market = {'id': user_info.id,'name': user_info.name,'taiger_1': {'amount': 0,'price': 0}},
        taiger_2_market = {'id': user_info.id,'name': user_info.name,'taiger_2': {'amount': 0,'price': 0}},
        haimars_market = {'id': user_info.id,'name': user_info.name,'haimars': {'amount': 0,'price': 0}},
        drone_market = {'id': user_info.id,'name': user_info.name,'drone': {'amount': 0,'price': 0}},
        wolfram_market = {'id': user_info.id,'name': user_info.name,'wolfram': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.t_90 = user_info.t_90 - int(result['t_90'])
        db.session.commit()
        return{"Respone": "add Succes"}

@app.route('/add_market_haimars_json', methods=["GET","POST"])
def addHaimarsMarketJson():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    
    try:
        market_info = db.session.query(Market).get(result['id'])
        if (int(result['haimars'])) <= int(user_info.haimars):
            market_info.haimars_market = {
                    'id': user_info.id,
                    'name': user_info.name,
                    'haimars': {
                        'amount': int(market_info.haimars_market['haimars']['amount']) + int(result['haimars']),
                        'price': result['price']
                    }
                }
            user_info.haimars = user_info.haimars - int(result['haimars'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], haimars_market = {
        
            'id': user_info.id,
            'name': user_info.name,
            'haimars': {
                'amount': result['haimars'],
                'price': result['price']
            }
        },
        oil = {'id': user_info.id,'name': user_info.name,'oil': {'amount': 0,'price': 0}},
        coal = {'id': user_info.id,'name': user_info.name,'coal': {'amount': 0,'price': 0}},
        iron = {'id': user_info.id,'name': user_info.name,'iron': {'amount': 0,'price': 0}},
        silver = {'id': user_info.id,'name': user_info.name,'silver': {'amount': 0,'price': 0}},
        oxygen_market = {'id': user_info.id,'name': user_info.name,'oxygen': {'amount': 0,'price': 0}},
        taiger_1_market = {'id': user_info.id,'name': user_info.name,'taiger_1': {'amount': 0,'price': 0}},
        taiger_2_market = {'id': user_info.id,'name': user_info.name,'taiger_2': {'amount': 0,'price': 0}},
        t_90_market = {'id': user_info.id,'name': user_info.name,'t_90': {'amount': 0,'price': 0}},
        drone_market = {'id': user_info.id,'name': user_info.name,'drone': {'amount': 0,'price': 0}},
        wolfram_market = {'id': user_info.id,'name': user_info.name,'wolfram': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.haimars = user_info.haimars - int(result['haimars'])
        db.session.commit()
        return{"Respone": "add Succes"}

@app.route('/add_market_drone_json', methods=["GET","POST"])
def addDroneMarketJson():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    
    try:
        market_info = db.session.query(Market).get(result['id'])
        if (int(result['drone'])) <= int(user_info.drone):
            market_info.drone_market = {
                    'id': user_info.id,
                    'name': user_info.name,
                    'drone': {
                        'amount': int(market_info.drone_market['drone']['amount']) + int(result['drone']),
                        'price': result['price']
                    }
                }
            user_info.drone = user_info.drone - int(result['drone'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], drone_market = {
            'id': user_info.id,
            'name': user_info.name,
            'drone': {
                'amount': result['drone'],
                'price': result['price']
            }
        },
        oil = {'id': user_info.id,'name': user_info.name,'oil': {'amount': 0,'price': 0}},
        coal = {'id': user_info.id,'name': user_info.name,'coal': {'amount': 0,'price': 0}},
        iron = {'id': user_info.id,'name': user_info.name,'iron': {'amount': 0,'price': 0}},
        silver = {'id': user_info.id,'name': user_info.name,'silver': {'amount': 0,'price': 0}},
        oxygen_market = {'id': user_info.id,'name': user_info.name,'oxygen': {'amount': 0,'price': 0}},
        taiger_1_market = {'id': user_info.id,'name': user_info.name,'taiger_1': {'amount': 0,'price': 0}},
        taiger_2_market = {'id': user_info.id,'name': user_info.name,'taiger_2': {'amount': 0,'price': 0}},
        haimars_market = {'id': user_info.id,'name': user_info.name,'haimars': {'amount': 0,'price': 0}},
        t_90_market = {'id': user_info.id,'name': user_info.name,'t_90': {'amount': 0,'price': 0}},
        wolfram_market = {'id': user_info.id,'name': user_info.name,'wolfram': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.drone = user_info.drone - int(result['drone'])
        db.session.commit()
        return{"Respone": "add Succes"}

@app.route('/add_market_wolfram_json', methods=["GET","POST"])
def addWolframMarketJson():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    
    try:
        market_info = db.session.query(Market).get(result['id'])
        if (int(result['wolfram'])) <= int(user_info.wolfram):
            market_info.wolfram_market = {
                    'id': user_info.id,
                    'name': user_info.name,
                    'wolfram': {
                        'amount': int(market_info.wolfram_market['wolfram']['amount']) + int(result['wolfram']),
                        'price': result['price']
                    }
                }
            user_info.wolfram = user_info.wolfram - int(result['wolfram'])
            db.session.commit()
            return{"Respone": "Update Succes"}
        else: 
            return{'Respone': "Not Enough Resource"}
        
    except:
        addInfo = Market(id = result['id'], wolfram_market = {
            'id': user_info.id,
            'name': user_info.name,
            'wolfram': {
                'amount': result['wolfram'],
                'price': result['price']
            }
        },
        oil = {'id': user_info.id,'name': user_info.name,'oil': {'amount': 0,'price': 0}},
        coal = {'id': user_info.id,'name': user_info.name,'coal': {'amount': 0,'price': 0}},
        iron = {'id': user_info.id,'name': user_info.name,'iron': {'amount': 0,'price': 0}},
        silver = {'id': user_info.id,'name': user_info.name,'silver': {'amount': 0,'price': 0}},
        oxygen_market = {'id': user_info.id,'name': user_info.name,'oxygen': {'amount': 0,'price': 0}},
        taiger_1_market = {'id': user_info.id,'name': user_info.name,'taiger_1': {'amount': 0,'price': 0}},
        taiger_2_market = {'id': user_info.id,'name': user_info.name,'taiger_2': {'amount': 0,'price': 0}},
        haimars_market = {'id': user_info.id,'name': user_info.name,'haimars': {'amount': 0,'price': 0}},
        drone_market = {'id': user_info.id,'name': user_info.name,'drone': {'amount': 0,'price': 0}},
        t_90_market = {'id': user_info.id,'name': user_info.name,'t_90': {'amount': 0,'price': 0}},
        )
        db.session.add(addInfo)
        user_info.wolfram = user_info.wolfram - int(result['wolfram'])
        db.session.commit()
        return{"Respone": "add Succes"}

def get_market(market_type,resource):
    market_info = db.session.query(getattr(Market, market_type)).all()

    # Convert the market_info to a list of dictionaries
    market_info_dicts = [i[0] for i in market_info]

    # Sort the list based on 'price' values (assuming 'price' is a string)
    sorted_market_info = sorted(market_info_dicts, key=lambda x: int(x[resource]['price']))

    # Create a dictionary with 'price' as key and a list of dictionaries as value
    json_data = {}
    for i in sorted_market_info:
        price_key = str(i[resource]['price'])
        if int(price_key) != 0:
        # Check if price_key is in json_data, if not, initialize it as an empty list
            if price_key not in json_data:
                json_data[price_key] = []

            # Append the dictionary to the list associated with price_key
            json_data[price_key].append(i)

    # Print the resulting JSON data
    print(json_data)

    return jsonify(json_data)

@app.route('/get_market_oil', methods=["GET", "POST"])
def getOilMarket():
    return get_market('oil','oil')

@app.route('/get_market_coal', methods=["GET", "POST"])
def getCoalMarket():
    return get_market('coal','coal')

@app.route('/get_market_iron', methods=["GET", "POST"])
def getIronMarket():
    return get_market('iron','iron')

def getIronMarket():
    return get_market('iron')

@app.route('/get_market_silver', methods=["GET", "POST"])
def getSilverMarket():
    return get_market('silver','silver')

@app.route('/get_market_oxygen', methods=["GET", "POST"])
def getOxygenMarket():
    return get_market('oxygen_market','oxygen')

@app.route('/get_market_taiger_1', methods=["GET", "POST"])
def getTaiger1Market():
    return get_market('taiger_1_market','taiger_1')

@app.route('/get_market_taiger_2', methods=["GET", "POST"])
def getTaiger2Market():
    return get_market('taiger_2_market','taiger_2')

@app.route('/get_market_t_90', methods=["GET", "POST"])
def getT90Market():
    return get_market('t_90_market','t_90')

@app.route('/get_market_haimars', methods=["GET", "POST"])
def getHaimarsMarket():
    return get_market('haimars_market','haimars')

@app.route('/get_market_drone', methods=["GET", "POST"])
def getDroneMarket():
    return get_market('drone_market','drone')

@app.route('/get_market_wolfram', methods=["GET", "POST"])
def getWolframMarket():
    return get_market('wolfram_market','wolfram')

@app.route('/buy_oil', methods=["GET","POST"])
def buyOil():
    result = request.get_json()
    print(result)
    my_user_info = db.session.query(User).get(result['myId'])
    owner_user_info = db.session.query(User).get(result['ownerId'])
    current_seller_info = db.session.query(Market).get(result['ownerId'])

    buying_amount_price = int(result['amount']) * int(getattr(current_seller_info, result['sellerResourceType'])[result['sellerResourceTypeInside']]['price'])

    if int(my_user_info.money) >= int(buying_amount_price):
        overalAmount = getattr(my_user_info, result['buyerResource']) + int(result['amount'])
        setattr(my_user_info, result['buyerResource'], overalAmount)
        my_user_info.money = my_user_info.money - buying_amount_price
        owner_user_info.money = owner_user_info.money + buying_amount_price
        if (int(getattr(current_seller_info, result['sellerResourceType'])[result['sellerResourceTypeInside']]['amount']) - int(result['amount']) <= 0):
            newMarket = {
                'id': getattr(current_seller_info, result['sellerResourceType'])['id'],
                'name': getattr(current_seller_info, result['sellerResourceType'])['name'],
                result['sellerResourceTypeInside']: {
                    'amount': 0,
                    'price': 0
                }
            }
            setattr(current_seller_info, result['sellerResourceType'], newMarket)
            db.session.commit()
        else:
            newMarket = {
                'id': getattr(current_seller_info, result['sellerResourceType'])['id'],
                'name': getattr(current_seller_info, result['sellerResourceType'])['name'],
                result['sellerResourceTypeInside']: {
                    'amount': getattr(current_seller_info, result['sellerResourceType'])[result['sellerResourceTypeInside']]['amount'] - int(result['amount']),
                    'price': getattr(current_seller_info, result['sellerResourceType'])[result['sellerResourceTypeInside']]['price']
                }
            }
            setattr(current_seller_info, result['sellerResourceType'], newMarket)
            db.session.commit()

        db.session.commit()
        # print(buying_amount_price)
        return {'test':'Done'}
    else:
        return {'test':'You Dont Have Enough Money'}
    

#travel and residency System ln865 - onGoing

@app.route('/get_Living_region', methods=["GET","POST"])
def getLIvingRegion():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    
    return {"region":user_info.living_region}

@app.route('/get_Living_region_rect', methods=["GET","POST"])
def getLivingRegionRect():
    result = request.get_json()
    region = db.session.query(Region).get(result['region'])
    return {"rect":region.rect}

@app.route('/get_next_region_rect',methods=["GET","POST"])
def getNextRegionRect():
    result = request.get_json()
    region = db.session.query(Region).get(result['region'])
    return {"rect":region.rect}

@app.route('/sent_fly_info', methods=['GET',"POST"])
def sendFly():
    result = request.get_json()
    print(result)
    user_info = db.session.query(User).get(result['id'])
    print(user_info.fly)
    if user_info.fly == None:
        user_info.fly = result['flyJson']
        db.session.commit()
        return {'response':int(result['flyJson']['time'])}
    else: 
        return {'response':'First Cancel Travel'}

@app.route('/check_fly',methods=["GET","POST"])
def checkFly():
    result = request.get_json()

    user_info = db.session.query(User).get(result['id'])
    if user_info.fly != None:
        try:
            start_time = user_info.fly['startTime']
            print(start_time)
            prev = datetime.fromisoformat(str(start_time)).astimezone(timezone.utc)
            new = datetime.fromisoformat(str(result['date'])).astimezone(timezone.utc)
            difference_time = new-prev
            if (int(difference_time.total_seconds())/60)>=int(user_info.fly['time']):
                user_info.living_region = user_info.fly['destination']
                user_info.fly = None
                db.session.commit()
                return{'res':'Done'}
            else:
                return{'res':'you need To fly more','time':(int(user_info.fly['time'])*60)-int(difference_time.total_seconds()),'from':user_info.living_region,'to':user_info.fly['destination']}
        except:
            print("Here is No travel Request")
            return{'res':'1No Travel Request'}
    else:
        return{'res':'2No Travel Request'}

@app.route('/start_fly', methods=["GET","POST"])
def starFly():
    time.sleep(60)
    result = request.get_json()
    user_info = db.session.query(User).get(result['myId'])
    second_region = db.session.query(Region).get(user_info.living_region)
    second_region.liverCount = second_region.liverCount - 1
    user_info.living_region = result['region']
    region_info = db.session.query(Region).get(result['region'])
    region_info.liverCount =  region_info.liverCount + 1
    db.session.commit()
    return {"Region Change":user_info.living_region, "citizen": region_info.liverCount }

@app.route('/send_residancy',methods=["GET","POST"])
def sendResidancy():
    result = request.get_json()
    region_info = db.session.query(Region).get(result['region'])
    user_info = db.session.query(User).get(result['myId'])
    #if state_info.residency = free:
    second_region = db.session.query(Region).filter(Region.name == user_info.res_region.title()).first()
    second_region.residendalCount = second_region.residendalCount - 1
    region_info.residendalCount = region_info.residendalCount + 1
    user_info.res_region = region_info.name
    db.session.commit()
    return{"Response":"Done", "residental": region_info.residendalCount}


@app.route('/home')
def home():
    return "Hello World"

@app.route('/get_last_fill', methods=["GET","POST"])
def get_last_fill():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    return {'lastFillTime': user_info.lastFillDate}

@app.route('/login', methods=["POST","GET"])
@cross_origin(origin='*',headers=['Content-Type'])
def login():
    result = request.get_json()
    print(f"test {result['password']}")
    user_mail = db.session.query(User).filter(User.mail == result['email']).first()
    print(check_password_hash(pwhash=user_mail.password, password=result['password']))
    if request.method == "POST":
        if user_mail:
            if user_mail.password and check_password_hash(pwhash=user_mail.password, password=result['password']):
                print('yep')
                return jsonify({'id':user_mail.id})
            else:
                print('Password Err')
        else:
            print('mail Err')

    return jsonify(result)

@app.route('/register', methods=["GET","POST"])
# @cross_origin(origin='*',headers=['content-type'])
# @cross_origin(origin='*',headers=['Content-Type'])
def register():
    result = request.get_json()
    print(result)
    if request.method == "POST":
        gen_hash = generate_password_hash(result['password'], salt_length=8, method="pbkdf2:sha256")
        user_info = User(permission = 2, name = result['name'], second_name = 'None',
                            mail = result["email"],
                            password = gen_hash, energy = 200, money = 1000000000,
                            res_region = "georgia", res_state = "Georgia", level = 1,
                            experience = 0, strenght = 1, education = 1, endurance = 1,
                            premium = 0, friends_count = 0, damage = 0, working_experience = 0,
                            max_experience = 0,lastFillDate = datetime.now(), autoWorkStart = datetime.now(), autoRefill = datetime.now(),
                            Gold_Factory = 0, Oil_Factory = 0, Silver_Factory = 0, Coal_Factory = 0,
                            Iron_Factory = 0, tiger_1 = 0, t_90 = 0, oxygen = 0, drone = 0, haimars = 0, wolfram = 0,
                            tiger_2 = 0, current_factory = 2, living_region = "GE" ) 
        user_mail = result["email"]
        base_mail = db.session.query(User).filter(User.mail == result['email']).first()
        print(base_mail)
        if base_mail and str(base_mail.mail) == str(result["email"]):
            print('error')
        else:
            db.session.add(user_info)
            db.session.commit()
            print('succesfully')
    return jsonify(result)


@app.route('/profile', methods=["GET","POST"])
# @cross_origin(origin='*',headers=['Content-Type'])
# @cross_origin(origin='http://localhost:8080')
def get_profile():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    try:
        partyName = db.session.query(Party).get(user_info.party).name,
        partyRegion = db.session.query(Party).get(user_info.party).region,
        # partyId = db.session.query(Party).get(user_info.party).id,
    except:
        partyName = "None"
        partyRegion = "None"
        # partyId = 0
    print(result)
    user = {
        'id':user_info.id,
        'name': user_info.name,
        "energy":user_info.energy,
        "money":user_info.money,
        "level":user_info.level,
        "res_region":user_info.res_region,
        "res_state":db.session.query(Region).filter(Region.name == user_info.res_region.capitalize()).first().country,
        "experience":user_info.experience,
        "strenght":user_info.strenght,
        "education":user_info.education,
        "endurance":user_info.endurance,
        "premium":user_info.premium,
        "friends_count":user_info.friends_count,
        "damage":user_info.damage,
        "working_experience":user_info.working_experience,
        "max_experience":user_info.max_experience,
        "living_region":user_info.living_region,
        'current_factory':user_info.current_factory,
        'last_fill':user_info.last_fill,
        'last_fill_hour':user_info.last_fill_hour,
        'last_fiil_day':user_info.last_fill_day,
        'refilClickTime': user_info.refilClickTime,
        'manualFilling': user_info.manualFilling,
        'gold': user_info.Gold_Factory,
        'oil': user_info.Oil_Factory,
        'silver': user_info.Silver_Factory,
        'iron': user_info.Iron_Factory,
        'coal': user_info.Coal_Factory,
        'living_region_name': db.session.query(Region).get(user_info.living_region).name,
        'living_region_country': db.session.query(Region).get(user_info.living_region).country,
        'party_name': partyName[0],
        'party_region': partyRegion[0],
        'party_id': user_info.party
    }
    
    return jsonify(user)



@app.route('/send_factory_type', methods=["GET","POST"])
def send_factory():
    result = request.get_json()
    print(result)
    return {'test':'factory Done'}

#send storage info
@app.route('/send_storage_info', methods=["GET","POST"])
# @cross_origin(origin='*',headers=['Content-Type'])
# @cross_origin(origin='http://localhost:8080')
def get_storage_profile():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    print(result)
    user = {
        'id':user_info.id,
        'name': user_info.name,
        "energy":user_info.energy,
        "money":user_info.money,
        "level":user_info.level,
        "res_region":user_info.res_region,
        "res_state":user_info.res_state,
        "experience":user_info.experience,
        "strenght":user_info.strenght,
        "education":user_info.education,
        "endurance":user_info.endurance,
        "premium":user_info.premium,
        "friends_count":user_info.friends_count,
        "damage":user_info.damage,
        "working_experience":user_info.working_experience,
        "max_experience":user_info.max_experience,
        "living_region":user_info.living_region,
        'current_factory':user_info.current_factory,
        'last_fill':user_info.last_fill,
        'last_fill_hour':user_info.last_fill_hour,
        'last_fiil_day':user_info.last_fill_day,
        'refilClickTime': user_info.refilClickTime,
        'manualFilling': user_info.manualFilling,
        'gold': user_info.Gold_Factory,
        'oil': user_info.Oil_Factory,
        'silver': user_info.Silver_Factory,
        'iron': user_info.Iron_Factory,
        'coal': user_info.Coal_Factory,
        'tiger_1':user_info.tiger_1,
        'tiger_2':user_info.tiger_2,
        't_90':user_info.t_90,
        'drone':user_info.drone,
        'haimars':user_info.haimars,
        'wolfram':user_info.wolfram,
        'oxygen':user_info.oxygen
    }
    
    return jsonify(user)

#gold convert
@app.route('/send_storage_info_base', methods=['GET','POST'])
def get_gold_convert():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    user_info.Gold_Factory = result['gold']
    user_info.money = result['money']
    db.session.commit()
    print(result)
    return{'money':user_info.money, 'gold':user_info.Gold_Factory}

#send weapon craft info
@app.route('/get_weapon_craft', methods=["POST","GET"])
def send_info():
    result = request.get_json()
    info = db.session.query(WeaponPrice).get(result['id'])
    print(type(info.t_90.split(',')[0]))
    data = {
        'tiger_1':{
            'money':round((int(info.taiger_1.split(',')[0])/2016),3),
            'iron':round((int(info.taiger_1.split(',')[1])/2016),3),
            'oil':round((int(info.taiger_1.split(',')[2])/2016),3),
            'crafted':round((int(info.taiger_1.split(',')[3])/2016),3),
        },
        'tiger_2':{
            'money':round((int(info.taiger_2.split(',')[0])/1814),3),
            'iron':round((int(info.taiger_2.split(',')[1])/1814),3),
            'oil':round((int(info.taiger_2.split(',')[2])/1814),3),
            'crafted':round((int(info.taiger_2.split(',')[3])/1814),3),
        },
        't_90':{
            'money':round((int(info.t_90.split(',')[0])/1612),3),
            'iron':round((int(info.t_90.split(',')[1])/1612),3),
            'coal':round((int(info.t_90.split(',')[2])/1612),3),
            'crafted':round((int(info.t_90.split(',')[3])/1612),3),
        },
        'wolfram':{
            'gold':round((int(info.wolfram.split(',')[0])/604),3),
            'iron':round((int(info.wolfram.split(',')[1])/604),3),
            'oil':round((int(info.wolfram.split(',')[1])/604),3),
            'coal':round((int(info.wolfram.split(',')[1])/604),3),
            'silver':round((int(info.wolfram.split(',')[1])/604),3),
            'crafted':round((int(info.wolfram.split(',')[2])/604),3),
        },
        'haimars':{
            'money':round((int(info.haimars.split(',')[0])/604),3),
            'wolfram':round((int(info.haimars.split(',')[1])/604),3)
        },
        'drone':{
            'money':round((int(info.drone.split(',')[0])/604),3),
            'wolfram':round((int(info.drone.split(',')[1])/604),3)
        }

    }
    return data

#when lost regions db and need recovery factory value need uncomment map.vue postData script
@app.route('/get_map_info', methods=["GET","POST"])
def get_map_data():
    result = request.get_json()
    test = [['Oil Factory','oilFactory.webp'],['Coal Factory','coalFactory.png'],['Iron Factory','ironFactory.jpg'],['Silver Factory','silverFactory.png'],['Gold Factory','goldFactory.png']]
    for i in result['regions']:
        print(i[0])
        region_info = Region(id = i[0], name = i[1], defColor = 'white', color = 'green',
                             educationIndex = 1, medicinIndex = 1, militaryIndex = 1,
                             developmentIndex = 1, teachersCount = 1, doctorsCount = 1,
                             hesCount = 1, clinicsCount = 1, schoolsCount = 1,
                             militaryBases = 1, generalCount = 1, liverCount = 0,
                             residendalCount = 0, country = 'None', gerb = 'none', defenceSystems = 1,
                             factory = 1, party = 1, house = 10, rect = i[2])
        for j in test:
            factory_info = Factory(owner = 1, region = i[0],
                            organization = 'Rival Of State', type = j[0],
                            wage_type = 0, potentional_wage = '15000000000',
                            real_wage = '13000000000', workers_amount = 10,
                            workers_count = 0, experience = 0, level = 1, name = 'Test', factory_icon = j[1])
        # db.session.add(region_info)
            db.session.add(factory_info)
        db.session.commit()
    return 'Done'

#get map info
@app.route('/post_map_data', methods = ['GET','POST'])
def post_map_data():
    firstFilter = []
    secondFilter = []
    thirdFilter = []
    dict = {}
    region_info = db.session.query(Region).all()
    for i in region_info:
        firstFilter = [i.id, i.defColor, i.color]
        secondFilter = [firstFilter]
        thirdFilter.extend(secondFilter)
        secondFilter = []
        # fourthFilter.extend[thirdFilter]
        # thirdFilter = []
    dict = {
        "info":thirdFilter
    }
    # print(thirdFilter)
    return jsonify(dict)

#ger region info
@app.route('/get_region_info', methods=["POST","GET"])
def get_region():
    result = request.get_json()
    # time.sleep(10)
    # print(f'gasvdgavdgasvdhgasvdhgasvdhgasvdhgasvdhg /asvdhagsdvash{result["id"]}')
    try:
        user_info = db.session.query(User).get(result["id"])
        region_info = db.session.query(Region).get(user_info.living_region)
    except:
        user_info = db.session.query(User).get(result["id"])
        region_info = db.session.query(Region).get(user_info.living_region)
    # print(f"asdasdas{region_info}")
    finally:
        try:
            region = {
                'id':region_info.id,
                'name': region_info.name,
                "educationIndex":region_info.educationIndex,
                "medicinIndex":region_info.medicinIndex,
                "militaryIndex":region_info.militaryIndex,
                "militaryIndex":region_info.militaryIndex,
                "developmentIndex":region_info.developmentIndex,
                "developmentIndex":region_info.developmentIndex,
                "teachersCount":region_info.teachersCount,
                "doctorsCount":region_info.doctorsCount,
                "hesCount":region_info.hesCount,
                "clinicsCount":region_info.clinicsCount,
                "schoolsCount":region_info.schoolsCount,
                "militaryBases":region_info.militaryBases,
                "generalCount":region_info.generalCount,
                "residendalCount":region_info.residendalCount,
                "liverCount":region_info.liverCount,
                "country":region_info.country,
                "gerb":region_info.gerb,
                "factory":region_info.factory,
                "party":region_info.party,
                "defenceSystems":region_info.defenceSystems,
                "house":region_info.house,
            }
        except:
            user_info = db.session.query(User).get(result["id"])
            region_info = db.session.query(Region).get(user_info.living_region)
            region = {
                'id':region_info.id,
                'name': region_info.name,
                "educationIndex":region_info.educationIndex,
                "medicinIndex":region_info.medicinIndex,
                "militaryIndex":region_info.militaryIndex,
                "militaryIndex":region_info.militaryIndex,
                "developmentIndex":region_info.developmentIndex,
                "developmentIndex":region_info.developmentIndex,
                "teachersCount":region_info.teachersCount,
                "doctorsCount":region_info.doctorsCount,
                "hesCount":region_info.hesCount,
                "clinicsCount":region_info.clinicsCount,
                "schoolsCount":region_info.schoolsCount,
                "militaryBases":region_info.militaryBases,
                "generalCount":region_info.generalCount,
                "residendalCount":region_info.residendalCount,
                "liverCount":region_info.liverCount,
                "country":region_info.country,
                "gerb":region_info.gerb,
                "factory":region_info.factory,
                "party":region_info.party,
                "defenceSystems":region_info.defenceSystems,
                "house":region_info.house,
            }
    return jsonify(region)

#get region info for region page
@app.route('/get_region_info_region', methods=["GET","POST"])
def getRegionInfoForRegion():
    result = request.get_json()
    region_info = db.session.query(Region).get(result['id'])
    region = {
        'id':region_info.id,
        'name': region_info.name,
        "educationIndex":region_info.educationIndex,
        "medicinIndex":region_info.medicinIndex,
        "militaryIndex":region_info.militaryIndex,
        "militaryIndex":region_info.militaryIndex,
        "developmentIndex":region_info.developmentIndex,
        "developmentIndex":region_info.developmentIndex,
        "teachersCount":region_info.teachersCount,
        "doctorsCount":region_info.doctorsCount,
        "hesCount":region_info.hesCount,
        "clinicsCount":region_info.clinicsCount,
        "schoolsCount":region_info.schoolsCount,
        "militaryBases":region_info.militaryBases,
        "generalCount":region_info.generalCount,
        "residendalCount":region_info.residendalCount,
        "liverCount":region_info.liverCount,
        "country":region_info.country,
        "gerb":region_info.gerb,
        "factory":region_info.factory,
        "party":region_info.party,
        "defenceSystems":region_info.defenceSystems,
        "house":region_info.house,
    }
    return jsonify(region)

#get storage info   
@app.route('/test_storage', methods=["GET",'POST'])
def get_info():
    result = request.get_json()
    print(result['id'])
    test = db.session.query(User).get(result['id'])
    print(test.experience)
    return {'t':test.experience}

#get craft info ln 1310-1471
@app.route('/craft_tiger_1', methods=["POST","GET"])
def craft_tiger_1():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    craft_price = db.session.query(WeaponPrice).get(1)
    data={
        'tiger_1':{
            'money':round((int(craft_price.taiger_1.split(',')[0])/2016),3),
            'iron':round((int(craft_price.taiger_1.split(',')[1])/2016),3),
            'oil':round((int(craft_price.taiger_1.split(',')[2])/2016),3),
            'crafted':round((int(craft_price.taiger_1.split(',')[3])/2016),3),
        }
    }
    money = data['tiger_1']['money']*int(result['amount'])
    iron = data['tiger_1']['iron']*int(result['amount'])
    oil = data['tiger_1']['oil']*int(result['amount'])
    print(iron)
    if user_info.money >= money and user_info.Iron_Factory >= iron and user_info.Oil_Factory >= oil:
        user_info.money = user_info.money - money
        user_info.Iron_Factory = user_info.Iron_Factory - iron
        user_info.Oil_Factory = user_info.Oil_Factory - oil
        user_info.tiger_1 = user_info.tiger_1 + result['amount']
        db.session.commit()
        return{'tiger_1': user_info.tiger_1, 'iron': user_info.Iron_Factory,
               'oil': user_info.Oil_Factory}
    else:
        return {'tiger_1':0}
       

@app.route('/craft_tiger_2', methods=["POST","GET"])
def craft_tiger_2():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    craft_price = db.session.query(WeaponPrice).get(1)
    data={
        'tiger_2':{
            'money':round((int(craft_price.taiger_2.split(',')[0])/2016),3),
            'iron':round((int(craft_price.taiger_2.split(',')[1])/2016),3),
            'oil':round((int(craft_price.taiger_2.split(',')[2])/2016),3),
            'crafted':round((int(craft_price.taiger_2.split(',')[3])/2016),3),
        }
    }
    money = data['tiger_2']['money']*int(result['amount'])
    iron = data['tiger_2']['iron']*int(result['amount'])
    oil = data['tiger_2']['oil']*int(result['amount'])
    print(iron)
    if user_info.money >= money and user_info.Iron_Factory >= iron and user_info.Oil_Factory >= oil:
        user_info.money = user_info.money - money
        user_info.Iron_Factory = user_info.Iron_Factory - iron
        user_info.Oil_Factory = user_info.Oil_Factory - oil
        user_info.tiger_2 = user_info.tiger_2 + result['amount']
        db.session.commit()
        return{'tiger_2': user_info.tiger_2, 'iron': user_info.Iron_Factory,
               'oil': user_info.Oil_Factory}
    else:
        return {'tiger_2':0}
            
@app.route('/craft_t_90', methods=["POST","GET"])
def t_90():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    craft_price = db.session.query(WeaponPrice).get(1)
    data={
        't_90':{
            'money':round((int(craft_price.t_90.split(',')[0])/2016),3),
            'iron':round((int(craft_price.t_90.split(',')[1])/2016),3),
            'coal':round((int(craft_price.t_90.split(',')[2])/2016),3),
            'crafted':round((int(craft_price.t_90.split(',')[3])/2016),3),
        }
    }
    money = data['t_90']['money']*int(result['amount'])
    iron = data['t_90']['iron']*int(result['amount'])
    coal = data['t_90']['coal']*int(result['amount'])
    print(iron)
    if user_info.money >= money and user_info.Iron_Factory >= iron and user_info.Coal_Factory >= coal:
        user_info.money = user_info.money - money
        user_info.Iron_Factory = user_info.Iron_Factory - iron
        user_info.Coal_Factory = user_info.Coal_Factory - coal
        user_info.t_90 = user_info.t_90 + result['amount']
        db.session.commit()
        return{'t_90': user_info.t_90, 'iron': user_info.Iron_Factory,
               'coal': user_info.Coal_Factory}
    else:
        return {'t_90':0}
            
@app.route('/craft_wolfram', methods=["POST","GET"])
def wolfram():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    craft_price = db.session.query(WeaponPrice).get(1)
    data={
        'wolfram':{
            'gold':round((int(craft_price.wolfram.split(',')[0])/604),3),
            'iron':round((int(craft_price.wolfram.split(',')[1])/604),3),
            'oil':round((int(craft_price.wolfram.split(',')[1])/604),3),
            'coal':round((int(craft_price.wolfram.split(',')[1])/604),3),
            'silver':round((int(craft_price.wolfram.split(',')[1])/604),3),
            'crafted':round((int(craft_price.wolfram.split(',')[2])/604),3),
        },
    }
    gold = data['wolfram']['gold']*int(result['amount'])
    iron = data['wolfram']['iron']*int(result['amount'])
    coal = data['wolfram']['coal']*int(result['amount'])
    oil = data['wolfram']['oil']*int(result['amount'])
    silver = data['wolfram']['silver']*int(result['amount'])
    print(iron)
    if user_info.Gold_Factory >= gold and user_info.Iron_Factory >= iron and user_info.Coal_Factory >= coal and user_info.Silver_Factory >= silver and user_info.Oil_Factory >= oil:
        user_info.Gold_Factory = user_info.Gold_Factory - gold
        user_info.Iron_Factory = user_info.Iron_Factory - iron
        user_info.Coal_Factory = user_info.Coal_Factory - coal
        user_info.Silver_Factory = user_info.Silver_Factory - silver
        user_info.wolfram = user_info.wolfram + result['amount']
        db.session.commit()
        return{'wolfram': user_info.wolfram, 'iron': user_info.Iron_Factory,
               'coal': user_info.Coal_Factory, 'oil': user_info.Oil_Factory,
               'gold': user_info.Gold_Factory, 'silver': user_info.Silver_Factory}
    else:
        return {'wolfram':0}

@app.route('/craft_haimars', methods=["POST","GET"])
def craft_haimars():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    craft_price = db.session.query(WeaponPrice).get(1)
    data={
        'haimars':{
            'money':round((int(craft_price.haimars.split(',')[0])/604),3),
            'wolfram':round((int(craft_price.haimars.split(',')[1])/604),3),
        },
    }
    money = data['haimars']['money']*int(result['amount'])
    wolfram = data['haimars']['wolfram']*int(result['amount'])
    if user_info.money >= money and user_info.wolfram >= wolfram:
        user_info.wolfram = user_info.wolfram - wolfram
        user_info.money = user_info.money - money
        user_info.haimars = user_info.haimars + result['amount']
        db.session.commit()
        return{'haimars': user_info.haimars, 'wolfram': user_info.wolfram}
    else:
        return {'haimars':0}
        
@app.route('/craft_drone', methods=["POST","GET"])
def drone():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    craft_price = db.session.query(WeaponPrice).get(1)
    data={
        'drone':{
            'money':round((int(craft_price.drone.split(',')[0])/604),3),
            'wolfram':round((int(craft_price.drone.split(',')[1])/604),3),
        },
    }
    money = data['drone']['money']*int(result['amount'])
    wolfram = data['drone']['wolfram']*int(result['amount'])
    if user_info.money >= money and user_info.wolfram >= wolfram:
        user_info.wolfram = user_info.wolfram - wolfram
        user_info.money = user_info.money - money
        user_info.drone = user_info.drone + result['amount']
        db.session.commit()
        return{'drone': user_info.drone, 'wolfram': user_info.wolfram}
    else:
        return {'drone':0}
        


@app.route('/send_manual_refill_info', methods=["GET","POST"])
def refil():
    result = request.get_json()
    print(result)
    user_info = db.session.query(User).get(result["id"])
    user_info.energy = result['energy']
    user_info.lastFillDate = result['lft']
    print(result)
    user = {
        'id':user_info.id,
        "energy":user_info.energy
    }
    db.session.commit()
    return jsonify(user)

@app.route('/send_work_info',methods=["GET","POST"])
def send_work_info():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    factoryType = result['factory'].replace(' ','_')
    print(result)
    money = getattr(user_info, f"{factoryType}")
    money = money + result['resource']
    setattr(user_info, f"{factoryType}", money)
    user_info.energy = result['energy']
    db.session.commit()
    print(result)
    return {'energy':user_info.energy}

@app.route('/check_auto_work', methods=["GET","POST"])
def check_auto_Work():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    return {'autoWorkTime': user_info.autoWorkStart}

@app.route('/get_auto_work_bool', methods=["GET","POST"])
def get_auto_Work_bool():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    return {'autoWorkbool': user_info.autoWork,'autoWorkStartTime':user_info.autoWorkStart}

@app.route('/send_auto_info', methods=['GET','POST'])
def send_autoWork_info():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    user_info.autoWorkStart = result['autoWorkTime']
    user_info.autoWork = result['autoWorkBoolian']
    db.session.commit()
    return {'autoWorkTime': user_info.autoWorkStart}

@app.route('/refill_auto',methods=['GET','POST'])
def refill_auto():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])

    return {'lastAutoFill':user_info.autoRefill}


@app.route('/auto_refill',methods=['GET',"POST"])
def auto_refill():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    # print(user_info.autoRefill)
    prev = datetime.fromisoformat(str(user_info.autoRefill)).astimezone(timezone.utc)
    new = datetime.fromisoformat(str(result['date'])).astimezone(timezone.utc)
    total = new - prev
    print(total)
    total_in_minute = (total.total_seconds()/60)
    if total_in_minute >= 5:
        if (user_info.energy + (5*(total_in_minute/5)))>200:
            user_info.energy = 200
            user_info.autoRefill = result['date']
            db.session.commit()
        else:
            user_info.energy = user_info.energy + (5*(total_in_minute/5))
            user_info.autoRefill = result['date']
            db.session.commit()
        return {'energy':user_info.energy,'timer':(300)}
    else:
        return {'energy':user_info.energy,'en':'err','timer':(300-total.total_seconds())}
   
    
    return{'test':1}

@app.route('/send_refill_auto',methods=['GET','POST'])
def send_refill_auto():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    user_info.energy = result['energy']
    user_info.autoRefill = result['time']
    db.session.commit()
    return {"Done":1}

@app.route('/create_factory', methods=["GET","POST"])
def create_factory():
    result = request.get_json()
    user_info = db.session.query(User).get(result["id"])
    user_region = user_info.living_region
    region_info = Factory(owner = user_info.id, region = user_region,
                          organization = 'None', type = 'Gold Factory',
                          wage_type = 0, potentional_wage = '15000000000',
                          real_wage = '13000000000', workers_amount = 10,
                          workers_count = 0, experience = 0, level = 1)
    print(region_info)
    db.session.add(region_info)
    db.session.commit()
    return {"test":"test"}

@app.route('/change_work_factory', methods=['GET','POST'])
def change_Work_factory():
    result = request.get_json()
    print(result['nextFactoryId']['id'])
    user_info = db.session.query(User).get(result["id"])
    user_info.current_factory = result['nextFactoryId']['id']
    db.session.commit()
    # print(user_info.current_factory)
    return {'Change Factory':'Done','nextFactory':user_info.current_factory}

@app.route('/auto_work_start_end',methods=["GET","POST"])
def startAutoWork():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    print(user_info.autoWorkStart)
    prev = datetime.fromisoformat(str(user_info.autoWorkStart)).astimezone(timezone.utc)
    new = datetime.fromisoformat(str(result['date'])).astimezone(timezone.utc)
    total = new - prev
    print(total)
    total_in_minute = (total.total_seconds()/60)

    print(f'qdadsadadad{(total_in_minute)}')
    if int(result['energy'])>=200:
        if total_in_minute>=5:
            if user_info.autoWork != 1:
                user_info.autoWork = 1
                user_info.autoWorkStart = result['date']
                db.session.commit()
                return {'minute':total_in_minute,'start':1}
            else:
                user_info.autoWork = 0
                db.session.commit()
                return {'minute':0,'start':0}
        else:
            user_info.autoWork = 0
            db.session.commit()
            return {'minute':total_in_minute,'start':0}
    else:
        user_info.autoWork = 0
        db.session.commit()
        return {'minute':total_in_minute,'start':0}
    return{'test':'done'}

@app.route('/send_auto_work_new_date', methods=["POST","GET"])
def sendAutoWorkNewDate():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    user_info.autoWorkStart = result['date']
    db.session.commit()
    return {'res':'Done'}

@app.route('/check_auto_work_start_end',methods=["POST","GET"])
def check_Auto_work_start():
    result = request.get_json()
    
    user_info = db.session.query(User).get(result['id'])
    region_info = db.session.query(Region).get(user_info.living_region)
    print(user_info.autoWorkStart)
    prev = datetime.fromisoformat(str(user_info.autoWorkStart)).astimezone(timezone.utc)
    new = datetime.fromisoformat(str(result['date'])).astimezone(timezone.utc)
    total = new - prev
    print(total)
    total_in_minute = (total.total_seconds()/60)
    total_in_hour = (total_in_minute/1440)
    print(f'qdadsadadad{(total_in_minute)}')
    if total_in_minute>=5:
        if total_in_hour>1:
            if user_info.autoWork == 1:
                user_info = db.session.query(User).get(result["id"])
                user_info = db.session.query(User).get(result["id"])
                factory = user_info.current_factory
                factoryType = db.session.query(Factory).get(factory)
                money = getattr(user_info, f"{factoryType.type.replace(' ','_')}")
                print(f'es ra xdeba{factoryType}')
                money = (money + ((200*((user_info.education*0.06)+(region_info.medicinIndex*0.04)))*(288)))
                print(money)
                setattr(user_info, f"{factoryType.type.replace(' ','_')}", money)
                user_info.autoWorkStart = result['date']
                user_info.autoWork = 0
                db.session.commit()
                return {'minute':total_in_minute,'start':0}
            else:
                return {'minute':0,'start':0}
        else:
            if user_info.autoWork == 1:
                user_info.autoWork = 1
                user_info = db.session.query(User).get(result["id"])
                factory = user_info.current_factory
                factoryType = db.session.query(Factory).get(factory)
                money = getattr(user_info, f"{factoryType.type.replace(' ','_')}")
                print(f"asgfdytasFDASVDGACDTSADA{factoryType}")
                print(f'y4wfgy6gr63qy812y4y128u34128y471{money}')
                money = (money + ((200*((user_info.education*0.06)+(region_info.medicinIndex*0.04)))*(math.floor(total_in_minute/5))))
                setattr(user_info, f"{factoryType.type.replace(' ','_')}", money)
                user_info.autoWorkStart = result['date']
                db.session.commit()
                prev = datetime.fromisoformat(str(user_info.autoWorkStart)).astimezone(timezone.utc)
                new = datetime.fromisoformat(str(result['date'])).astimezone(timezone.utc)
                total = new - prev
                return {'minute':total_in_minute,'start':1, 'timer': int(300 - total.total_seconds())}
            else:
                return {'minute':0,'start':0}
    else:
        if user_info.autoWork == 1:
            return {'minute':total_in_minute,'start':1, 'timer': int(300 - total.total_seconds())}
        else:
            return {'minute':total_in_minute,'start':0}
    return{'test':'done'}

def serialize_factory(factory):
    owner_info = {
        'id': factory.factorys_owner.id,
        'user_name': factory.factorys_owner.name,
        'working_experience': factory.factorys_owner.working_experience
    }
    return {
        'id': factory.id,
        'name':factory.name,
        'owner': owner_info,
        'region': factory.region,
        'level': factory.level,
        'organization': factory.organization,
        'type': factory.type,
        'wage_type': factory.wage_type,
        'potentional_wage': factory.potentional_wage,
        'real_wage': factory.real_wage,
        'workers_amount': factory.workers_amount,
        'workers_count': factory.workers_count,
        'experience': factory.experience,
        'factory_icon': factory.factory_icon
        
    }
@app.route('/get_all_factory', methods=["GET","POST"])
def get_factory():
    result = request.get_json()
    region_info = db.session.query(User).get(result['id']).living_region
    print(region_info)
    factorys = db.session.query(Factory).filter(Factory.region == region_info).all()
    factory_list = [serialize_factory(factory) for factory in factorys]
    return jsonify(factory_list)


@app.route('/get_current_factory',methods=["GET","POST"])
def get_current_factory():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    # print(f'asdasdadasdasdsdas{user_info.current_factory}')
    factory_info = db.session.query(Factory).get(user_info.current_factory)
    test = []
    test.append(factory_info)
    factory_list = [serialize_factory(factory) for factory in test]
    return{'currentFactoryId':user_info.current_factory,'currentFactoryList':factory_list}


#profile page apis

#enter living Region
@app.route('/enter_living_region',methods=["GET","POST"])
def enterLivingRegion():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    return{'regionId':user_info.living_region}

@app.route('/enter_residental_region',methods=["GET","POST"])
def enterResidentalRegion():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    region_info = db.session.query(Region).filter(Region.name == user_info.res_region.capitalize()).first()
    return{"resRegionId":region_info.id}

@app.route('/enter_residental_state',methods=["GET","POST"])
def enterResState():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    region_info = db.session.query(Region).filter(Region.name == user_info.res_region.capitalize()).first()
    state_info = db.session.query(State).filter(State.name == region_info.country).first()
    print(f'asdasdasdasddasasd{state_info.id}')
    return{"resStateId":state_info.id}


#page of region apis
@app.route('/enter_res_region',methods=["GET","POST"])
def enterResRegion():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    return{'regionId':user_info.res_region.capitalize(),'livingRegion':user_info.living_region}


#page of state apis

def serialize_state(state):
    return {
        'id': state.id,
        'name':state.name,
        'region': state.region,
        'members': state.members
    }



@app.route('/create_state',methods=["GET","POST"])
def createState():
    result = request.get_json()
    stateName = f'State{random.randint(0,1000)}'
    party_info = db.session.query(Party).filter(Party.region == result['id']).all()
   
    party_info = [x for x in party_info]
    party_iteration = []
    for i in party_info:
        i.state = stateName
        db.session.commit()
        step = {
                'id':i.id,
                'name':i.name,
                'vote':0
                }
        party_iteration.append(step)
        step = {}
    print(party_iteration)
    election_info = Election(party = party_iteration, state = stateName, voter = [])
    db.session.add(election_info)
    db.session.commit()

    region_info = db.session.query(Region).get(result['id'])
    state_info = State(name = stateName,
                       teachersCount = region_info.teachersCount,doctorsCount=region_info.doctorsCount,hesCount=region_info.hesCount,
                       clinicsCount=region_info.clinicsCount,
                       schoolsCount=region_info.schoolsCount,militaryBases=region_info.militaryBases,generalCount=region_info.generalCount,residendalCount=region_info.residendalCount,
                       liverCount=region_info.liverCount,
                       gerb=region_info.gerb,factory=region_info.factory,party=region_info.party,
                       house=region_info.house,defenceSystems=region_info.defenceSystems,
                       election={'id':election_info.id,'isElection':1,'delay':result['date'],'startTimeSecDelay':86400,'endTime':0,'nextElection':0},
                       parlament={'member':[],'size': 30,'leader':'none','minister':[{
                           'economy':'none',
                           'defence':'none',
                           'foreign':'none',
                       }]},regions = [result['id']], laws = [],
                       defColor = 'white', color = 'white', country = 'none')
    db.session.add(state_info)
    db.session.commit()
    state = db.session.query(State).filter(func.json_extract_path_text(State.regions, 'regions', '1') == result['id']).first()
    region_info.country = state.name
    db.session.commit()
    print(f'asdsadasdsadasdadas{state}')
    return{'id': state.id}


@app.route('/get_state_data',methods=["GET","POST"])
def getStateData():
    result = request.get_json()
    state_info = db.session.query(State).get(result['id'])
    print(state_info)
    return{"done":"Done"}


@app.route('/get_state_election_data',methods=["GET","POST"])
def getIsElectionData():
    result = request.get_json()
    state_info = db.session.query(State).get(result['id'])
    isElection = state_info.election['isElection']
    electionId = state_info.election['id']
    if isElection == 1:
        return{"isElection":isElection,"electionId":electionId}
    else:
        end_time = state_info.election['endTime']
        prev = datetime.strptime(str(end_time),'%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
        new = datetime.strptime(str(result['date']),'%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
        difference_time = new-prev
        if (state_info.election['nextElection'] - difference_time.total_seconds()) <= 0:
            party_info = db.session.query(Party).filter(Party.region == result['id']).all()
            regions = [x for x in state_info.regions]
            party_iteration = []
            for i in regions:
                all_party = db.session.query(Party).filter(Party.region == i).all()
                party_info = [x for x in all_party]
            
                for i in party_info:
                    step = {
                            'id':i.id,
                            'name':i.name,
                            'vote':0
                            }
                    party_iteration.append(step)
                    step = {}
            election_info = Election(party = party_iteration, state = state_info.name, voter = [])
            db.session.add(election_info)
            db.session.commit()
            state_info.election = {'id':election_info.id,'isElection':1,'delay':result['date'],'startTimeSecDelay':86400,'endTime':0,'nextElection':604800}
            db.session.commit()
            isElection = state_info.election['isElection']
            electionId = state_info.election['id']
            return{"isElection":isElection,"electionId":electionId}
        else:
            return{"isElection":0,"electionId":0}


#page of parlament election

def serialize_election(election,visibility):
    return {
        'id': election.id,
        'party':election.party,
        'state': election.state,
        'visibility':visibility
    }


@app.route('/get_parlament_election_data',methods=["GET","POST"])
def getParlamentElectionData():
    result = request.get_json()
    election_info = db.session.query(Election).get(result['id'])
    # election_list = serialize_election(election_info)
    if str(result['user']) in election_info.voter:
        election_list = serialize_election(election_info,visibility=0)
    else:
        election_list = serialize_election(election_info,visibility=1)
    
    return jsonify(election_list)    


@app.route('/vote_up_parlament_election',methods=["GET","POST"])
def voteUpParlamentElection():
    result = request.get_json()
    election = db.session.query(Election).get(result['id'])
    party_info = [x for x in election.party if x['id'] == result['party']]
    afterUpdateParty = [x for x in election.party]
    afterUpdateParty.remove(party_info[0])
    party_info[0]['vote'] = party_info[0]['vote'] + 1
    afterUpdateParty.append(party_info[0])
    print(party_info[0])
    print(afterUpdateParty)
    election.party = afterUpdateParty
    voters = [x for x in election.voter]
    voters.append(result['user'])
    election.voter = voters
    db.session.commit()
    if str(result['user']) in election.voter:
        election_list = serialize_election(election,visibility=0)
    else:
        election_list = serialize_election(election,visibility=1)
    
    return jsonify(election_list)    

@app.route('/check_parlament_election_time',methods=["GET","POST"])
def checkPArlamentElectionTime():
    result = request.get_json()
    state_info = db.session.query(State).filter(State.name == result['state']).first()
    start_time = state_info.election['delay']
    prev = datetime.strptime(str(start_time),'%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
    new = datetime.strptime(str(result['date']),'%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
    difference_time = new-prev
    print(difference_time.total_seconds())
    if state_info.election['startTimeSecDelay']-difference_time.total_seconds() <= 0:
        # return {'time': state_info.election['startTimeSecDelay']-difference_time.total_seconds()}
        return{'time': 0}
    else:
        return {'time': state_info.election['startTimeSecDelay']-difference_time.total_seconds()}
@app.route('/send_election_info_in_db',methods=["GET","POST"])
def sendParlamentElectionInDb():
    result = request.get_json()
    newParlament = []
    election_info = db.session.query(Election).get(result['id'])
    state_info = db.session.query(State).filter(State.name == result['state']).first()
    election_party = [x for x in election_info.party]
    all_vote = 0
    members = []
    partysInParlament = []
    for i in election_party:
        all_vote = all_vote + i['vote']
        # partysInParlament = [x for x in state_info.parlament['member']]
        
    # print(all_vote)
    for i in election_party:
        partys = db.session.query(Party).get(i['id'])
        if i['vote'] != 0:
            percents = (all_vote*100)/i['vote']
        else:
            percents = 0
        members_count = (state_info.parlament["size"]*percents)/100
        print(members_count)
        if int(members_count) >= len(partys.members):
            newParty = {partys.name:partys.members}
        # print(newParty)
            partysInParlament.append(newParty)
        elif int(members_count) != 0:
            print(members_count)
            leader = [x for x in partys.members if x[0]['position'] == 'leader']
            # print(leader)
            newParty = {partys.name:[leader]}
            members.append(newParty)
            membersWithoutLeader = [x for x in partys.members if x[0]['position'] != 'leader']
            for i in range(0, int(members_count) - 1):
                
                members['partys.name'].append(membersWithoutLeader[i])
                # print(f'asdasdasdasds{members}')
            partysInParlament.append(members)
        # print(partys.members)
            
    parlament_info = {
                'member': partysInParlament,
                "size": 30,
                "leader": "none",
                "minister": [{"economy": "none", "defence": "none", "foreign": "none"}]
            }
    
    electionDict = {
        'id': result['id'],
        'isElection': 0,
        'delay': state_info.election['delay'],
        'startTimeSecDelay': state_info.election['startTimeSecDelay'],
        'endTime': result['date'],
        'nextElection': 604800
    }
    # print(partysInParlament)
    state_info.parlament = parlament_info
    state_info.election = electionDict
    db.session.commit()
    return{"isElection":0, 'state': state_info.id}

#page of party

def serialize_party(party):
    test = ([x[0] for x in party.members if x[0]['position'] == 'leader'])
    return {
        'id': party.id,
        'name':party.name,
        'region': party.region,
        'members': party.members,
        'leader': test[0]['name']
    }

@app.route('/create_party',methods=["GET","POST"])
def createParty():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    region_info = db.session.query(Region).get(result['region'])
    if user_info.party != 0:
        return{"Res":"First Leave Party", 'id': 0}
    else:
        party_info = Party(name = f'Party{random.randint(0,1000)}',
                        region = result['region'],
                        state = region_info.country,
                        gold = 30, budget = 0, 
                        members = [[{'name':user_info.name, 'id':user_info.id,'position':'leader','numeric':2}]],
                        waiter = [])
        db.session.add(party_info)
        region_info.party = int(region_info.party) + 1
        name = party_info.name
        db.session.commit()
        party_info = db.session.query(Party).filter(Party.name == name).first()
        user_info = db.session.query(User).get(result['id'])
        user_info.party = party_info.id
        db.session.commit()
        return {"id": party_info.id}


@app.route('/get_party_data',methods=['POST','GET'])
def getPartyData():
    result = request.get_json()
    party_info = db.session.query(Party).get(result['id'])
    test = ([x[0] for x in party_info.members if x[0]['position'] == 'leader'])
    print(f'asdasdasdadsasdmdjasmdkas{test}')
    return {"id":party_info.id,
            "name":party_info.name,
            "region":db.session.query(Region).get(party_info.region).name,
            "count":len(party_info.members),
            "members":party_info.members,
            "waiters":party_info.waiter,
            "leader":test[0]}

@app.route('/get_all_regional_party',methods=["GET","POST"])
def getAllRegionalParty():
    result = request.get_json()
    party_info = db.session.query(Party).filter(Party.region == result['id']).all()
    test = []
    test.append(party_info)
    party_list = [serialize_party(party) for party in party_info]
    return{"party":party_list}

@app.route('/send_party_request',methods=["GET","POST"])
def partyRequest():
    result = request.get_json()
    user_info = db.session.query(User).get(result['id'])
    party_info = db.session.query(Party).get(result['party'])
    
    if user_info.party != 0:
        return{'Res':"You have Already been on party"}
    else:
        requestedUser = [{
            "name":user_info.name,
            "id":user_info.id,
            "position":"member",
            "numeric":0
        }]
        # print(party_info.waiter)
        waiter = [x for x in party_info.waiter if x[0]['id'] == None or x[0]['id'] != int(result['id'])]
        # waiter.append(party_info.waiter)
        waiter.append(requestedUser)
        print(waiter)
        party_info.waiter = waiter
        db.session.commit()
        return{"Res":"User Add On List"}
        

@app.route('/add_user_in_party',methods=["GET","POST"])
def addUserInParty():
    result = request.get_json()
    party_info = db.session.query(Party).get(result['party'])
    user_info = db.session.query(User).get(result['id'])
    waiters = [x[0] for x in party_info.waiter if x[0]['id'] == int(user_info.id)]
    member = [x for x in party_info.members] 
    newUser = [{
        'name': waiters[0]['name'],
        'id': waiters[0]['id'],
        'position': waiters[0]['position'],
        'numeric': waiters[0]['numeric']
    }]
    member.append(newUser)
    party_info.members = member
    removeWaiter = [x for x in party_info.waiter]
    removeWaiter.remove(waiters)
    user_info.party = result['party']
    party_info.members = member
    party_info.waiter = removeWaiter
    db.session.commit()

    # print(member.append(newUser))
    return{"res":"User Add In Party"}


@app.route('/remove_user_from_request',methods=["GET","POST"])
def removeUserFromRequest():
    result = request.get_json()
    party_info = db.session.query(Party).get(result['party'])
    user_info = db.session.query(User).get(result['id'])
    waiters = [x[0] for x in party_info.waiter if x[0]['id'] == int(user_info.id)]
    removeWaiter = [x for x in party_info.waiter]
    removeWaiter.remove(waiters)
    party_info.waiter = removeWaiter
    db.session.commit()

    # print(member.append(newUser))
    return{"res":"User Remove From RequestList"}


@app.route('/remove_user_from_member',methods=["GET","POST"])
def removeUserFromMember():
    result = request.get_json()
    party_info = db.session.query(Party).get(result['party'])
    user_info = db.session.query(User).get(result['id'])
    member = [x[0] for x in party_info.members if x[0]['id'] == int(user_info.id)]
    removeMember = [x for x in party_info.members]
    removeMember.remove(member)
    party_info.members = removeMember
    db.session.commit()

    # print(member.append(newUser))
    return{"res":"User Remove From Party"}


@app.route('/promote_user_in_party',methods=["GET","POST"])
def promoteUserInParty():
    result = request.get_json()
    party_info = db.session.query(Party).get(result['party'])
    user_info = db.session.query(User).get(result['id'])
    member = [x[0] for x in party_info.members if x[0]['id'] == int(result['id'])]
    promoteMember = [x for x in party_info.members]
    promoteMember.remove(member)
    if member[0]['position'] == 'member':
        newUser=[{
            'name': member[0]['name'],
            'id': member[0]['id'],
            'position': 'support',
            'numeric': 1
        }]
        promoteMember.append(newUser)
        party_info.members = promoteMember
        db.session.commit()
    elif member[0]['position'] == 'support':
        newUser=[{
            'name': member[0]['name'],
            'id': member[0]['id'],
            'position': 'leader',
            'numeric': 2
        }]
        promoteMember.append(newUser)
        leader = [x[0] for x in party_info.members if x[0]['position'] == 'leader']
        promoteMember.remove(leader)
        newSupport = [{
            'name': leader[0]['name'],
            'id': leader[0]['id'],
            'position': 'support',
            'numeric': 1
        }]
        promoteMember.append(newSupport)
        party_info.members = promoteMember
        db.session.commit()
    return{'test':'test'}


    removeMember.append(member)
    print(member)
    db.session.commit()

    # print(member.append(newUser))
    return{"res":"User Remove From Party"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='80')



