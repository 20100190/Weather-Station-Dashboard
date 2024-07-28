from flask import Blueprint

bp = Blueprint('error', __name__, static_folder="static")
# if this script is run directly then __name__ = __main__
# else it's the module name where this is defined, in this case it will be error

from . import handlers
