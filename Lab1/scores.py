#Lab1
#Author: Xia Hua

class Scores :
    def __init__(self):
        '''
        a constructor that reads in data from the ile and stores it in an appropriate data structure. 
        The data structure is an instance variable. 
        Code check for ile open success and end the program with an error message if the ile open fails.
        Extra Mission for Not using a loop
        
        Use dictionary to contain different country data
        '''
        FILENAME = "input1.txt"
        try:
            with open(FILENAME) as f:
                self._data = {data[0]:data[1:] #Collect Data throgh the files create dic files to put into
                              for data in zip(*[line.split() for line in f])} #Use zip command to put data into differnt country dictionary. Split the data by space or tab 
                if len(self._data) == 0 : #Check the input file is correct 
                    raise EOFError(FILENAME + "is not a valid input file")
        #exception handle
        except EOFError as e:
            raise SystemExit(e + "Please Check Valid Data inside?")        
        except IOError as e:
            raise SystemExit(e + "IOError")
        except FileNotFoundError:
            raise SystemExit(FILENAME+"unable to access")        
    '''
    Serves as a generator for the data. 
    It will return one country's name and corresponding scores with each next() call. 
    The order of the country being returned is alphabeical order based on country abbreviaion.
    iterates all country from A-Z
    return list of scores and country tuple
    '''
    def getOne(self):
        for elem in sorted(self._data): # Generator of the type of the object 
            yield elem,list(self._data[elem]) # Using yield to make the object to country Solved by Dicussion Form Student help
    '''
    prints all countries and all corresponding scores
    Each country and its scores are on one line of output
    the print order is by descending order of the last score of each country
    '''
    def printByLast(self):
        for elem in sorted(self._data, key = lambda elem : self._data[elem][-1], reverse = True): # use sorted to sort data sorted by the last score(biggest on the top)
            print(elem + ":", ' '.join(self._data[elem])) # print by last score of each country take data from tuple form the class material 
    '''
    prints the maximum and minimum of all the total scores of each country.
    Solved by the help in the discussion form. 
    Created a list list to slove the question.
    Create the sum of the score list in every country, use the max and min function to calculate the biggest and smallest score.
    '''
    def printMaxMin(self):
        data = [sum([float(digit) for digit in self._data[elem]]) for elem in self._data]
        print("max total:", max(data)) #Using Max to compare the Max sum in the dictionary 
        print("min total:", min(data)) #Using Min to compare the Min sum in the dictionary 
