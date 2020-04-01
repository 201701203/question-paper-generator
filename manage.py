from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flaskapp import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskapp/site.db'
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
