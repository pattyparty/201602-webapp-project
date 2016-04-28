from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# FIXME write your app below
#course count is talking about the classes from the selected semester
#in that department

#we will need to creat a list of all the departments' classes during
    #specific semesters

# also we need to fill the dictionary with the semesters

class Subject:
    def __init__(self, department, semester):
        dictionary = {"Fall 2017":"f2017"}
        self.department = department
        self.semester = semester
        if (semester == dictionary.keys):
            course_code = department+"_"+dictionary.values()
            print(course_code)
            return course_code
    

@app.route('/')
def view_root():
    return render_template('base.html')

# The functions below lets you access files in the css, js, and images folders.
# You should not change them unless you know what you are doing.

@app.route('/images/<file>')
def get_image(file):
    return send_from_directory('images', file)

@app.route('/css/<file>')
def get_css(file):
    return send_from_directory('css', file)

@app.route('/js/<file>')
def get_js(file):
    return send_from_directory('js', file)

if __name__ == '__main__':
    chdir(dirname(realpath(__file__)))
    app.run(debug=True)
