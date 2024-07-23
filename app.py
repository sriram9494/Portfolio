from flask import Flask
app = Flask(__name__) 

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from api import urls
        urls.init_routes(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

