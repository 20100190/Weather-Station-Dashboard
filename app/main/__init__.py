from flask import Blueprint

main = Blueprint('main', __name__)
# if this script is run directly then __name__ = __main__
# else it's the module name where this is defined

from . import views  # to avoid circular dependency we import at end, import is necessary to register routes
