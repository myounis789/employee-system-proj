from application import app

application=Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SECRET_KEY'] = os.getenv('secretkey')
db = SQLAlchemy(application)

app.run(debug=True, host = '0.0.0.0')


