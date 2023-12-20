# def shortestWithBaseCase(makeRecursiveCall): 
#     print ('shortestWithBaseCase(%s) called' % makeRecursiveCall)
#     if not makeRecursiveCall:
#         # BASE CASE
#         print('Returning from base case')
#         return
#     else:
#         # RECURSIVE
#         shortestWithBaseCase(False)
#         print('Returning from recursive case')
#         return
#
# print('Calling fn with false')
# shortestWithBaseCase(False)
#
# print('Calling fn with true')
# shortestWithBaseCase(True)

# Counts down to 0, and then back up to the number
def countDownAndUp(number):
    print(number)
    if number == 0:
        print("Reached 0")
        return
    countDownAndUp(number - 1)
    print(number, 'returning')  
    return

countDownAndUp(10)
