import datetime
import functools
import os
import re 
import urllib

from flask import (Flask, abort, flash, Markup, redirect, render_template,
                    request, Response, session, url_for)
from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache
from peewee import *
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *

ADMIN_PASSWORD = "top_secret" #For prototyping only, use one-way hash to store it
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = "sqliteext:///%" % os.path.join(APP_DIR, "blog.db")
DEBUG = False
SECRET_KEY = "1094103358" # Secret key used by Flask for session encryption
SITE_WIDTH = 800

#Initiate app
app = Flask(__name__)
app.config.from_object(__name__)
#Initiate database
flask_db = FlaskDB(app)
database = flask_db.database

oembed_providers = bootstrap_basic(OEmbedCache())