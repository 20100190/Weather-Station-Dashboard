from flask import render_template, jsonify
from sqlalchemy.orm.exc import StaleDataError

from app import db
from . import bp
from .messages import STALE_DATA_ERROR


@bp.route('/')
def index():
    return render_template('other/index.html')
