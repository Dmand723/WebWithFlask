from flask import Blueprint,render_template

veiws = Blueprint('views',__name__)

@veiws.route('/')
def home():
    return render_template('home.html')