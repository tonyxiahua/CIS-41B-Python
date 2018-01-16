# CIS 41B Assignment 1
# Name:

from scores import Scores
    
def main() :
    data = Scores()     # create Scores object
    gen=data.getOne()   # create generator object
    print("---")
    print(next(gen))    # fetch first data of object
    print("---")
    data.printByLast()  # print all data sorted by last field
    print("---")
    print(next(gen))    # fetch next data of object
    print("---")
    data.printMaxMin()  # print the max and min of the total scores
    print("---")
    print(next(gen))    # fetch next data of object
    print("---")
    
main()