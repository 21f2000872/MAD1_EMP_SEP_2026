from Flask import Flask



@app.route('/')
def index():
    data = dict(courses,exams,students)
  return render_template('index.html', data=data)
