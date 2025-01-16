#Imports practice

 #Make a directory with 2 modules; make a function in one of them; 
 #then import this function in the other module and use that in your script of choice.

from task1_1 import func_1


def func_2():
    print("I'm from task_1")


if __name__ == '__main__':
    func_2()
    func_1()


#________________________________________
#task1_1
def func_1():
    print("Hello I'm from other file")