# declare a function that takes two list arguments
def check_unique(list1, list2):
    # loop through list2 and store the numbers in val variable
    for number in list2:
        # check for the values of list2 not in list1 
        if number not in list1:
            # return the number not in list1
            return number


print check_unique([4, 66, 7], [66, 77, 7, 4])

