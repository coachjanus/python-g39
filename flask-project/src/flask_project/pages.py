from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route('/')
def index():
    return render_template('pages/index.html')
    # return "Hello Flask Factory"

@bp.route('/about')
def about():
    return render_template('pages/about.html')
    # return "About Page"
    
@bp.route('/contact')
def contact():
    return render_template('pages/contact.html')
    # return "Contact Us"
