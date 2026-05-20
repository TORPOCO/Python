from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

#ORM para conectarnos a la BD
db = SQLAlchemy()
#Para sincronizar nuestros obj con la BD
migrate = Migrate()
#Para cerealizar y deseriazar estos objetos
ma = Marshmallow()
