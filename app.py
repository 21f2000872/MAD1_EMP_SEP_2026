from Flask import Flask



@app.route('/')
def index():
    data = dict(courses=one('SELECT COUNT(*) AS n FROM courses')['n'],exams=one('SELECT COUNT(*) AS n FROM examinations')['n'],students=one('SELECT COUNT(*) AS n FROM users WHERE role= "student')['n'])
  return render_template('index.html', data=data)
