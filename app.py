from Flask import (Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    data = dict(courses=one('SELECT COUNT(*) AS n FROM courses')['n'],
                exams=one('SELECT COUNT(*) AS n FROM examinations')['n'],
                students=one('SELECT COUNT(*) AS n FROM users WHERE role= "student')['n'])
  return render_template('index.html', data=data)

@app.route('/Examinations')
def Examinations():
    exam = [{ "Physics": 'Electronics' }, {"Chemistry": "Organic Chemistry"}]
  return render_template 'Examinations.html'



@app.route('/about')
def about():
    return("This Examination management portal allows us to create and manage examination courses")



if __name__ == '__main__':
    app.run(debug=True)
