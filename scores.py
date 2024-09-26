import json


class Scores():
    global data_SAT

    with open('data.json', 'r') as data_file:
        raw_data = json.load(data_file)
        data_SAT = raw_data['data']

    def most_tests(self):
        most_num = int(data_SAT[0][10])
        most_school = None
        for school in data_SAT:
            try:
                if int(school[10]) > most_num:
                    most_num = int(school[10])
                    most_school = school[9]
            except:
                pass
        return (most_school, most_num)

    def best_score(self):
        best_school = int(data_SAT[0][11]) + int(data_SAT[0][11]) + int(data_SAT[0][11])
        school_name = data_SAT[0][9]
        total_score = 0
        
        for school in data_SAT:
            try:
                total_score = int(school[11]) + int(school[12]) + int(school[13])
            except:
                total_score = 0
            if total_score > best_school:
                best_school = total_score
                school_name = school[9]
        return (school_name, best_school)

    def best_score_small(self):
        small_schools = []
        small_schools_score = []

        for school in data_SAT:
            try:
                if (int(school[10]) <= 50):
                    try:
                        small_schools_score.append(int(school[11]) + int(school[12]) + int(school[13]))
                        small_schools.append(school[9])
                    except:
                        pass
            except:
                pass

        biggest = small_schools[0]
        biggest_num = small_schools_score[0]

        for i in range(50):
            if (small_schools_score[i] > biggest_num):
                biggest = small_schools[i]
                biggest_num = small_schools_score[i]
        return (biggest, biggest_num)

    def x_most_tests(self, x):
        most_test = [[None] * 2] * len(data_SAT)
        for i in range(len(data_SAT)):
            most_test[i][0] = data_SAT[i][9]
            print(data_SAT[i][9])
        return most_test

    def x_highest_scores(self, x):
        return None
    
