from logging import debug
import os

from flask_migrate import Migrate

from app.api    import db, create_app
from seed.product import seed_product

from app        import api_v1

app = create_app(os.getenv("ENVIRONMENT") or 'prod')
app.register_blueprint(api_v1, url_prefix="/v1")


@app.cli.command("init")
def init():
    """ create init function here """
    seed_product()
    

app.app_context().push()
migrate = Migrate(app, db)