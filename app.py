from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Student, AcademicRecord, Skill, CareerGoal

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///education_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    students = Student.query.all()
    return render_template('dashboard.html', students=students)



@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

@app.route('/market')
def market():
    return render_template('market.html')



@app.route('/mentors')
def mentors():
    return render_template('mentors.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')

@app.route('/institution')
def institution():
    return render_template('institution.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/profile') # Kept for backward compatibility/sub-routing
def profile():
    return render_template('profile.html')

@app.route('/skills') # Kept for backward compatibility/sub-routing
def skills():
    return render_template('skills.html')


# Initialize DB
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
