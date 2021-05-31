# Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# Output: 11
# Explanation:
# Employee 1 has importance value 5, and he has two direct
# subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.

def getImportance(employee_list, id):
    # importance = 0
    # subordinates = []
    # print('id', id)
    # print('importance', importance)
    # if id in existed:

    for emp in employee_list:
        if id == emp[0]:
            importance = emp[1]
            subordinates = emp[2]
    
            if len(subordinates) <= 0:
                return importance
        
            else:
                for i in subordinates:
                    print('subordinates', i)
                    importance = importance + getImportance(employee_list, i)
                return importance

employee = [[1,2,[2]], [2,3,[]]]
id = 2

print(getImportance(employee, id))