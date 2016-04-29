from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory, request

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
    def __init__(self, year, season, department, number, section):
        self.year = year
        self.season = season
        self.department = department
        self.number = number
        self.section = section
        self.title = ''
        self.unit = ''
        self.instructor = ''
        self.meeting = []
        self.core = []
        self.seats = ''
        self.enrolled = ''
        self.reserved = ''
        self.reservedOpen = ''
        self.waitlisted = ''
        self.id = ''
    def get_department_number(self):
        number = ''
        number += self.department + self.number
        return number
    def generate_id(self):
        self.id = self.year + self.season + self.department + self.number

class Course_Counts:
    def __init__(self, list):
        self.course_counts = list

    def search_by_semester(self, sem):
        ans_list = []
        if sem == '':
            return self.course_counts
        else:
            for course in self.course_counts:
                sem_num = course.year
                if course.season == 'fall':
                    sem_num += '01'
                elif course.season == 'spring':
                    sem_num += '02'
                else:
                    sem_num += '03'
                if sem == sem_num:
                    ans_list.append(course)
            return ans_list

    def search_by_core(self, core):
        ans_list = []
        if core == '':
            return self.course_counts
        else:
            for course in self.course_counts:
                if course.core == core:
                    ans_list.append(course)
            return ans_list

    def search_by_subject(self, sub):
        ans_list = []
        if sub == '':
            return self.course_counts
        else:
            for course in self.course_counts:
                if course.department == sub:
                    ans_list.append(course)
            return ans_list

    def find_course(self, sem_num, department, number):
        year_list = self.search_by_semester(sem_num)
        for index in range(0, len(year_list)):
            if year_list[index].department == department and year_list[index].number == number:
                return year_list[index]


def divide(str):
    list = str.split(' ')
    return list


def get_course_counts():
    coursecounts = Course_Counts([])
    with open('counts.tsv') as fd:
        for line in fd.read().splitlines():
            fields = line.split('\t')
            course = Course(fields[0], fields[1], fields[2], fields[3], fields[4])
            course.title = fields[5]
            course.unit = fields[6]
            course.instructors = fields[7]
            course.meeting = fields[8]
            course.core = fields[9]
            course.seats = fields[10]
            course.enrolled = fields[11]
            course.reserved = fields[12]
            course.reservedOpen = fields[13]
            course.waitlisted = fields[14]
            course.generate_id()
            coursecounts.course_counts.append(course)
    return coursecounts

course_counts = get_course_counts()
@app.route('/')
def view_root():
    ans_list_by_sem = course_counts.search_by_semester(request.args.get('semester'))
    temp_list = Course_Counts(ans_list_by_sem)
    ans_list_by_dept = temp_list.search_by_subject(request.args.get('department'))
    temp_list = Course_Counts(ans_list_by_dept)
    ans_list_by_core = temp_list.search_by_core(request.args.get('core'))
    print(ans_list_by_core)
    return render_template('base.html', result_list=ans_list_by_core)
# The functions below lets you access files in the css, js, and images folders.
# You should not change them unless you know what you are doing.

@app.route('/base/<id>')
def view_course(id):
    for course in course_counts.course_counts:
        if course.id == id:
            return render_template('course.html', course=course)


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
