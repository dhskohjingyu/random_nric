import random

class Person:
    def __init__(self, new_nric, new_name):
        self.__nric__ = new_nric
        self.__name__ = new_name

    def get_nric(self):
        return self.__nric__

    def get_name(self):
        return self.__name__

def generate_checksum(nric):
    # n is a string consisting of 8 characters, first denoting the IC type
    # followed by 7 numbers
    weight = [2, 7, 6, 5, 4, 3, 2]
    codes = [['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'],\
                ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']]
    alphabet = []
    total = 0

    first_char = nric[0]

    if first_char == 'S' or first_char == 'T':
        alphabet = codes[0]
    else:
        alphabet = codes[1]
    
    for i in range(1, len(nric)):
        total += int(nric[i]) * weight[i - 1]
        
    checksum = total % 11
    return alphabet[checksum]

def generate_name():
    first_names = ['Tan', 'Lim', 'Lee', 'Ng', 'Ong', 'Wong', 'Goh', 'Chua', 'Chan',\
                   'Koh', 'Teo', 'Ang', 'Yeo', 'Tay', 'Ho', 'Low', 'Toh', 'Sim',\
                   'Chong', 'Chia Seah']
    last_names = ['Rachel', 'Nicole', 'Ashley', 'Cheryl', 'Michelle', 'Yi Ling', 'Claudia',\
                  'Jasline', 'Debbie', 'Jasmine', 'Natalie', 'Jamie', 'Alvira', 'Judy',\
                  'Jenny', 'Amanda', 'Melissa', 'Eunice', 'Cherilyn', 'Andrea', 'Rin',\
                  'Kelly', 'Sherilyn', 'Nicolette', 'Wong', 'Zeth', 'Sarah', 'Xin Yi',\
                  'Karan', 'Faith', 'Adeline', 'Joey', 'Joy', 'Serene', 'Mindy',\
                  'Gladys', 'Felicia', 'Vicky', 'Angeline', 'Chelsea', 'Dorothy', 'Ziqian',\
                  'Alexis', 'Cathy', 'Hui Min', 'Jonathan', 'Nicholas', 'Justin', 'Joel',\
                  'Darren', 'Joseph', 'Darryl', 'Felix', 'Sean', 'Dale', 'Ben',\
                  'Alex', 'Matthew', 'Johnathan', 'Alexander', 'Steven', 'Wei Xuan', 'Marcus',\
                  'Eric', 'Xian Wei', 'Alvin', 'Damien', 'Daniel', 'Richard', 'John',\
                  'Feng', 'Albert', 'Winston', 'Julien', 'Amos', 'Johnson', 'Raymond',\
                  'Cheng', 'Bert', 'Lex', 'Gerald', 'Benjamin', 'Jun', 'Wei Jie']

    first_name = first_names[random.randrange(len(first_names))]
    last_name = last_names[random.randrange(len(last_names))]

    return first_name + " " + last_name

def generate_new_nric(used):
    start = ['S', 'T', 'F', 'G']
    nric_list = []

    nric_list.append(start[random.randrange(len(start))])
    nric_list.append('9')
    nric_list.append('5')

    # only need to generate 5 numbers as they are JC1 students
    for i in range(0, 5):
        random_num = str(random.randrange(0, 10))
        nric_list.append(random_num)

    nric = "".join(nric_list)
    checksum = generate_checksum(nric)
    nric_list.append(checksum)
    nric = "".join(nric_list)

    if nric in used:
        return generate_new_nric(used)
    else:
        used.append(nric)
        return nric

def sort_people(people):
    if people == []:
        return []
    else:
        pivot = people[0]
        lesser = []
        greater = []

        for person in people[1:]:
            if person.get_name() < pivot.get_name():
                #print(person.get_name() + "<" + pivot.get_name())
                lesser.append(person)
            else:
                #print(person.get_name() + ">=" + pivot.get_name())
                greater.append(person)

        return sort_people(lesser) + [pivot] + sort_people(greater)

infile = open("STUDENTS.DAT", "w")
ordered_infile = open("STUDENTS_SORTED.DAT", "w")

used_nrics = []
people = []

for i in range(0, 10000):
    nric = generate_new_nric(used_nrics)
    name = generate_name()
    person = Person(nric, name)
    people.append(person)
    infile.write(nric + ", " + name + "\n")

people = sort_people(people)

for person in people:
    ordered_infile.write(person.get_name() + ", " + person.get_nric() + "\n")

infile.close()
ordered_infile.close()
