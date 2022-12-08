
import json
import pytest

from manage import app
from app.api.base_model import db
# configuration
from app.config import config

BASE_URL = "/v1"
TEST_CONFIG = config.TestingConfig

class TestApp:

    @pytest.fixture
    def client(self):
        app_ = self.create_app()
        db.create_all()
        db.session.commit()
        yield app_.test_client()  # tests run here
        self.tearDown()

    @pytest.fixture(autouse=True)
    def set_client(self, client):
        self._client = client

    def create_app(self):
        app.config.from_object(TEST_CONFIG)

        #reinit db after change app.config
        try:
            with app.app_context():
                db.init_app(app)
        except:
            pass
   
        return app

    def tearDown(self):
        db.session.remove()
        db.drop_all()
