from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# FIXME write your app below
class Time:
    def __init__(self, time_str): ##03:00pm
        time_split = time_str.split(':')
        self.hour = time_split[0]
        self.min = time_split[1][0:2]
        self.datetime = time_split[1][2:]
    def get_hour(self):
        if self.datetime == 'pm':
            return int(self.hour) + 12
        else:
            return int(self.hour)
    def get_min(self):
        return int(self.min)

class TimeFrame:
    def __init__(self, beginning, end, date):
        self.beginning = beginning
        self.end = end
        self.date = date
    def checkIfOffered(self, date_str):
        if date_str in self.date:
            return True
        else:
            return False


class Course:
    def __init__(self, year, season, department, number, section, time):
        self.year = year
        self.season = season
        self.department = department
        self.number = number
        self.section = section
        self.time = time
        self.title = ''
        self.unit = ''
        self.instructor = ''
        self.core = ''
        self.seats = ''
        self.enrolled = ''
        self.reserved = ''
        self.reservedOpen = ''
        self.waitlisted = ''

class Course_Counts:


def get_course_counts():
    Subject.department
class Subject:
    def __init__(self, department, semester):
        dictionary = dictionary = {"Fall 2017":"f2017","Spring 2016":"S2016", "Fall 2016":"f2016",
                      "Spring 2015":"s2015", "Fall 2015":"f2015","Spring 2014":"s2014",
                      "Fall 2014":"f2014","Spring 2013":"s2013","Fall 2013":"f2013",
                      "Spring 2012":"s2012", "Fall 2012":"f2012", "Spring 2011":"s2011",
                      "Fall 2011":"f2011","Spring 2010":"s2010","Fall 2010":"f2010"}
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
