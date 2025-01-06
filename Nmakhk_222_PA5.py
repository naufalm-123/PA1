'''
Name: Naufal Makhkamdjanov
Assignment: PA 5
Due Date: 11/11/2024
######################################################################################
Honor Code Statement: I received no assistance on this assignment that violates the ethical guidelines set forth by professor and class syllabus.
######################################################################################
Comments and Assumptions: N/A
######################################################################################
NOTE: width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
         10        20        30        40        50        60        70        80
######################################################################################
'''
tile_values = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,'H':4, 'I':1, 'J':8,
'K':5,'L':1,'M':3,'N':1,'O':1,
'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
#start count at 0, iterate the letters over the word, add the assigned value of each letter to the counter
def evaluate_word(letters_dict, word):
    counter = 0
    for letter in word: #letter iterates over word :-)
        counter += letters_dict.get(letter, 0)
    return counter
#
def unique_pt_vals(letters_dict):
    list_of_pts = set(letters_dict.values())
    return list_of_pts
'''
t1 = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4}
t2 = {'X':5, 'Y':5, 'Z':5}
'''
#a new list is created, iterates through unique_points, for each letter and its score, it checks if the score and the point match, if so, it appends to the new list.
def points_map(letters_dict):
    unique_points = unique_pt_vals(letters_dict)
    dict_of_pts = {}
    for point in unique_points:
        dict_of_pts[point] = []
        for letter, score in letters_dict.items():
            if score == point:
                dict_of_pts[point].append(letter)
    return dict_of_pts
'''
t1 = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4}
t2 = {'X':5, 'Y':5, 'Z':5}
'''
#Initializes best word and point, iterates over word_list, assigns current word and points as best if its greater than best_point
def best_word(letters_dict, word_list):
    best_word = ""
    best_point = 0
    for word in word_list:
        current_point = evaluate_word(letters_dict, word)
        if current_point > best_point:
            best_word = word
            best_point = current_point
    return (best_word, best_point)
#If the number is zero, it has 1 zero. If the number is less than ten, it has 0 zeroes. If the number is divisible by ten, we add 1 plus the divisor. Else we just add the divisor.
def count_zeros(num):
    if num == 0:
        return 1
    if num < 10:
        return 0
    elif num % 10 == 0:
        return 1 + count_zeros(num // 10)
    else:
        return count_zeros(num // 10)
#We assign digit as 9, if number is zero, it has 0 of the assigned number. Else, if divisible by 10, it is 1 + the divisor. Else it is just the divisor
def count_digits(num, digit=9):
    if num == 0:
        return 0
    if num % 10 == digit:
        return 1 + count_digits(num // 10, digit)  
    else:
        return count_digits(num // 10, digit)  
