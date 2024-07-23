from .views import HomeView, SendMail

def init_routes(app):
    app.add_url_rule('/', view_func=HomeView.as_view('home'))
    app.add_url_rule('/sendemail/', view_func=SendMail.as_view('email'))
