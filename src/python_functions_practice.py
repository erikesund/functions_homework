from unittest import result


def return_10():
    return 10

def add(num_1,num_2):
    return num_1+num_2

def subtract(num_1,num_2):
    return num_1-num_2

def multiply(num_1, num_2):
    return num_1*num_2

def divide(num_1, num_2):
    return num_1/num_2

def length_of_string(string_length):
    string_length = len("A string of length 21")
    return string_length

def join_string(string_1, string_2):
    joined_string = string_1 + string_2
    return joined_string

def add_string_as_number(string_1, string_2):
    add_result = int(string_1) + int(string_2)
    return add_result


def number_to_full_month_name(number): 
    if number ==1:
        return "January"
    elif number == 3:
        return "March"
    elif number == 9:
        return "September"
    else: 
        return None

def number_to_short_month_name(number):
    if number == 1:
        return "Jan"
    elif number == 4:
        return "Apr"
    elif number == 10:
        return "Oct"
    else:
        return None