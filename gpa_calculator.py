
def store_data_of_grades():
    n = input("get_num_of_courses")  # get number of courses
    big_dict = {}  # big_dict to store the whole data
    course_names = []
    
    for i in range (int(n) ):
        course_name = input ( 'enter course name!' )  # get name of courses
        n2 =input ( 'how many inputs?   from 1 to 7    <midterm,assignment,quiz,attendance,project,final,labs,final lab>' )  # num of (assignments,miderms,quizzes)
        
        while not n2.isdigit():
            n2 = input ( 'not valid, how many inputs?   (from 1 to 7)   the input must be from the following <midterm,assignment,quiz,attendance,project,final,labs,final lab> :' )
        n2=int(n2)            #'how many inputs?   (from 1 to 7)     from the following<midterm,assignment,quiz,attendance,project,final,labs,final lab>'  # num of (assignments,miderms,quizzes)

        course_names.append ( course_name )
        list_ = ['midterm', 'assignment', 'quiz', 'project', 'final', 'labs', 'attendance', 'final lab']

        while n2 > 7:
            n2 = int ( input (
                'not valid how many inputs?   (from 1 to 7)    <midterm,assignment,quiz,attendance,project,final,labs,final lab> :' ) )

        d = {}  # to store the data of the items and its grade
        for j in range ( n2 ):
            item_name = input (
                'what item to enter?     <midterm,assignment,quiz,attendance,project,final,labs,final lab>   ' )
            # if item_name in d.keys():
            #     d[item_name]
            while not item_name in list_:
                item_name = input ( 'Error! enter a valid item !!' )
            if item_name == 'attendance':
                grade = input ( 'enter how many hours have you  skipped ?' ).split ()
                d[item_name] = grade
            else:
                grade = input ( "Enter grade:" ).split ()  # get the grade of each item
                grade = [float ( i ) for i in grade]
            d[item_name] = grade  # store the item and its grade in the dictionary of the course
        big_dict[course_name] = d  # store the dictionaries of courses in the big dictionary

        return big_dict, course_names
import math

w_dict, course_list = store_data_of_grades ()  # (mid,assignment,quiz,project,final)
print (w_dict)

def sixty_fourty(y):
    z = 0.6 * (int ( max ( y ) )) + 0.4 * (int ( min ( y ) ))
    return z



dict ={calculus:{midterm:[78 ,7 , 9],quiz:[]}}

def n_out_m(y, x):
    y = sorted ( y )
    y = y[(x):]
    z = sum ( y ) / len ( y )
    return z


def calcmidterms(grades, course_name):
    k = int ( input ( 'what is the full mark of ' + course_name + ' midterm?' ) )
    grades = [int ( n ) for n in grades]
    while any ( [0 > n or n > k for n in grades] ):
        k = int ( input ( ' Error! the grades you have is ' + str ( grades ) + 'enter valid grade  ' ) )
    if len ( grades ) == 1:
        z = grades[0] / k
        return z
    elif len ( grades ) == 2:
        sixty_fourty_cond = input (
            'do you take 60% of the best mid and 40% of the worst ' + course_name + ' midterm ?\n <y/n>' )
        while sixty_fourty_cond != 'y' and sixty_fourty_cond != 'n':
            sixty_fourty_cond = input ( 'Error! enter a valid answer:' )
        if sixty_fourty_cond == 'y':
            z = sixty_fourty ( grades ) / k
        else:
            z = (sum ( grades ) / len ( grades )) / k
        return z
    elif len ( grades ) == 3:
        two_out_three_cond = input ( 'do you take best two out of three midtrems in ' + course_name + '?\n <y/n>' )
        while two_out_three_cond != 'y' and two_out_three_cond != 'n':
            two_out_three_cond = input ( 'Error! enter a valid answer:' )
        if two_out_three_cond == 'y':
            z = (n_out_m ( grades, 2 )) / k
        else:
            z = (sum ( grades ) / len ( grades )) / k
        return z


def best_assignments(assignments, course_name):
    l = int ( input ( 'how many assignments will you drop in ' + course_name + ' ?' ) )
    k = int ( input ( 'what is a full mark of an assignment of ' + course_name + ' ?' ) )
    while l >= len ( assignments ):
        l = int ( input (
            'error!! that\'s too many assingments to drop\nhow many assignments will you drop in ' + course_name + '?' ) )
    for i in range ( len ( assignments ) ):
        for j in range ( i + 1, len ( assignments ) ):
            if assignments[i] > assignments[j]:
                t = assignments[i]
                assignments[i] = assignments[j]
                assignments[j] = t
    b = n_out_m ( assignments, l ) / k
    return b


def calcquizes(quiz_grade, course_name):
    l = int ( input ( 'how many quizzes will you drop in ' + course_name + ' ?' ) )
    k = int ( input ( 'what is the full mark of a quiz ' + course_name + ' ?' ) )
    quiz_grade = [int ( i ) for i in quiz_grade]
    while int ( l ) >= len ( quiz_grade ) or any ( [0 > n or n > k for n in quiz_grade] ):
        if int ( l ) >= len ( quiz_grade ):
            m = 'Error! you can\'t drop ' + str ( l ) + ' out of ' + str (
                len ( quiz_grade ) ) + ' quizzes.\nhow many quizzes will you drop? '
            l = int ( input ( m ) )
        if any ( [0 > n or n > k for n in quiz_grade] ):
            quiz_grade = input ( 'Error!!enter valid grades: ' ).split ()
            quiz_grade = [int ( n ) for n in quiz_grade]
    z = n_out_m ( quiz_grade, l ) / k
    return z


def calc_labs(grades, course_name):
    l = int ( input ( 'how many labs will you drop in ' + course_name + ' ? ' ) )
    k = int ( input ( 'what is the full mark of a ' + course_name + ' lab? ' ) )
    grades = [int ( i ) for i in grades]
    while int ( l ) >= len ( grades ) or any ( [0 > n or n > k for n in grades] ):
        if int ( l ) >= len ( grades ):
            m = 'Error! you can\'t drop ' + str ( l ) + ' out of ' + str (
                len ( grades ) ) + ' labs.\nhow many labs will you drop in ' + course_name + ' ? '
            l = int ( input ( m ) )
        if any ( [0 > n or n > k for n in grades] ):
            grades = input ( 'Error in grades list!! enter valid grades for ' + course_name + ' : ' ).split ()
            grades = [int ( n ) for n in grades]
    z = n_out_m ( grades, l ) / k
    return z


def Atten_grade(absence, course_name):
    y = int ( input ( 'how many hours can you skip in ' + course_name + ' course?' ) )
    if int ( absence[0] ) <= y:
        return 1
    else:
        return 0


def calc_final(grade, course_name):
    total_grade = int ( input ( 'what is the full mark in final' + course_name + ' ?' ) )
    while total_grade < grade[0]:
        total_grade = input ( 'error!! what is the full mark in final' + course_name + ' ?' )
    final_grade = grade[0] / total_grade
    return final_grade


def calc_project(grade, course_name):
    total_grade = int ( input ( 'what is the full mark in the project of the ' + course_name + ' ?' ) )
    while total_grade < grade[0]:
        total_grade = input ( 'error!! what is the full mark in of the project of the ' + course_name + ' ?' )
    final_grade = grade[0] / total_grade
    return final_grade


def update_big_dict():
    grad_mids = {}
    grad_quiz = {}
    grad_assignments = {}
    grad_labs = {}
    grad_attend = {}
    for i in range ( len ( course_list ) ):
        if 'quiz' in w_dict[course_list[i]].keys ():
            grad_quiz[course_list[i]] = (calcquizes ( w_dict[course_list[i]]['quiz'], course_list[i] ))
            w_dict[course_list[i]]['quiz'] = grad_quiz[course_list[i]]
        if 'assignment' in w_dict[course_list[i]].keys ():
            grad_assignments[course_list[i]] = (
                best_assignments ( w_dict[course_list[i]]['assignment'], course_list[i] ))
            w_dict[course_list[i]]['assignment'] = grad_assignments[course_list[i]]
        if 'midterm' in w_dict[course_list[i]].keys ():
            grad_mids[course_list[i]] = (calcmidterms ( w_dict[course_list[i]]['midterm'], course_list[i] ))
            w_dict[course_list[i]]['midterm'] = grad_mids[course_list[i]]
        if 'labs' in w_dict[course_list[i]].keys ():
            grad_labs[course_list[i]] = (calc_labs ( w_dict[course_list[i]]['labs'], course_list[i] ))
            w_dict[course_list[i]]['labs'] = grad_labs[course_list[i]]
        if 'attendance' in w_dict[course_list[i]].keys ():
            grad_attend[course_list[i]] = (Atten_grade ( w_dict[course_list[i]]['attendance'], course_list[i] ))
            w_dict[course_list[i]]['attendance'] = grad_attend[course_list[i]]
        if 'project' in w_dict[course_list[i]].keys ():
            w_dict[course_list[i]]['project'] = calc_project ( w_dict[course_list[i]]['project'], course_list[i] )
        if 'final' in w_dict[course_list[i]].keys ():
            w_dict[course_list[i]]['final'] = calc_final ( w_dict[course_list[i]]['final'], course_list[i] )
    return w_dict


def get_weight_of_items():
    items_weight = {}
    for i in range ( len ( course_list ) ):
        course_items = {}
        for j in (list ( w_dict[course_list[i]] )):
            course_items[j] = int ( input ( 'the weight of ' + j + ' in ' + course_list[i] ) )
        items_weight[course_list[i]] = course_items
    return items_weight


w_dict, items_weight = update_big_dict (), get_weight_of_items ()

print (w_dict)
def calc_final_grades(w_dict, items_weight):
    w_dict_list = []
    items_weight_list = []
    final_grades_of_courses = {}
    for i in range ( len ( course_list ) ):
        sub_list_w_dict = list ( w_dict[course_list[i]].values () )
        w_dict_list.append ( sub_list_w_dict )
        sub_list_items_weight = list ( items_weight[course_list[i]].values () )
        items_weight_list.append ( sub_list_items_weight )
    grades_of_courses = [[a * b for a, b in zip ( i, j )] for i, j in zip ( w_dict_list, items_weight_list )]
    for i in range ( len ( grades_of_courses ) ):
        final_grades_of_courses[course_list[i]] = sum ( grades_of_courses[i] )
    return final_grades_of_courses


def max_till_highest_grade(g, course_name):
    grades_l = ['C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', ]
    x = (g) % 5
    if g >= 60:
        y = grades_l[math.ceil (
            (g - 100) // 5 )]  # calls for the next item in list grades for every 5% decrease in the grade
        if g == 100:
            print ( 'you can lose 5% of your grades but still get a A' )
        elif x == 0:
            print ( 'you can lose no more of your grades to get a ', y, ' in ', course_name )
        else:
            print ( 'you can lose ', x, '% of your grades but still get a ', y, ' in ', course_name )
    else:
        print ( 'you have already failed the ', course_name, ' course' )


c = calc_final_grades ( w_dict, items_weight )
print ( c )
for n in list ( c.keys () ):
    max_till_highest_grade ( c[n], n )


def get_weight_of_courses():
    course_weight = {}
    for i in range ( len ( course_list ) ):
        course_weight[course_list[i]] = int ( input ( 'the weight of ' + course_list[i] + ' is(credits) : ' ) )
    return course_weight


course_weight = get_weight_of_courses ()


def calc_grade(dict):  # dict is a dictionary that has the course name as value and the total grade as an integer
    rates = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-']
    for n in list ( dict.keys () ):
        if dict[n] < 60:
            dict[n] = 'F'
        elif dict[n] >= 100:
            dict[n] = 99
        else:
            dict[n] = rates[-((int ( dict[n] ) - 60) // 5 + 1)]  # this line refers to to different letter in list rates for each 5% change in grades in the dict
    return dict


b = []
b = course_weight
v = calc_grade ( c )
gpa = []


def calc_gpa(letters, course_weight):
    for i in range ( len ( course_list ) ):
        if letters[course_list[i]] == 'A':
            gpa.append ( float ( course_weight[course_list[i]] ) * 4 )
        if letters[course_list[i]] == 'A-':
            gpa.append ( course_weight[course_list[i]] * 3.67 )
        if letters[course_list[i]] == 'B+':
            gpa.append ( course_weight[course_list[i]] * 3.33 )
        if letters[course_list[i]] == 'B':
            gpa.append ( course_weight[course_list[i]] * 3 )
        if letters[course_list[i]] == 'B-':
            gpa.append ( course_weight[course_list[i]] * 2.67 )
        if letters[course_list[i]] == 'C+':
            gpa.append ( course_weight[course_list[i]] * 2.33 )
        if letters[course_list[i]] == 'C':
            gpa.append ( course_weight[course_list[i]] * 2 )
        if letters[course_list[i]] == 'C-':
            gpa.append ( course_weight[course_list[i]] * 1.67 )
        if letters[course_list[i]] == 'F':
            gpa.append ( course_weight[course_list[i]] * 0 )
    f_gpa = sum ( gpa ) / sum ( [int ( b[n] ) for n in list ( b.keys () )] )
    print('your gpa is ',f_gpa)
    return  f_gpa


z = calc_gpa ( v, course_weight )
print ( z )
print ( c )


def min_gpa(tot_credits, cgpa):
    mincgpa = float ( input ( 'what is the minimum cgpa you can get over the next period of time ?' ) )
    future_credits = float ( input (
        'how many credits you will register over the next period of time ?' ) )  # let's call theamount of credit a student will take m and the amount of credits he's taken l, and call the current cgpa x and minmun cgpa q and the cgpa he will need to have in the future to maintain his gpa y
    mingpa = (mincgpa * (
            tot_credits + future_credits) - cgpa * tot_credits) / future_credits  # q=(x*l+y*m)/(l+m) solve for y
    if mingpa > 4:
        print ( 'It is impossible to get a gpa of ' + str ( mincgpa ) + ' while taking ' + str (
            future_credits ) + ' credits.' )
    elif mingpa <= 0:
        print ( 'no matter what gpa you will get over the next period of time you will never get a cgpa below ' + str (
            mincgpa ) + '.' )
    else:
        print ( 'you need to get a gpa of ' + str ( mincgpa ) )

cond=input('do you want to know what future gpa you need to get in order to not get below a certain gpa? ')
if cond in 'YESyes':
    k=float(input('how many credits have you taken? '))
    l=float(input('what is your cgpa (Accumulative gpa) ? '))
    min_gpa(k,l)



