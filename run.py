from app import app
from db import db

db.init_app(app)

@app.before_first_request
def crate_tabels():
  db.create_all()