import random
column1 = ["10/15/21","10/22/21","10/29/21"]
column2 = ["blank","10/15/21","10/22/21","10/29/21"]
column3 = column2
column_list = [column1,column2,column3]
outcome_set = []
for i in list(range(250)):
    new_outcome_list = []
    new_element = column1[random.randint(0,2)]
    new_outcome_list.append(new_element)
    count = 0
    while count < 1:
        new_element = column2[random.randint(0,3)]
        if new_element not in new_outcome_list:
            new_outcome_list.append(new_element)
            count += 1
        else:
            pass
    while count < 2:
        if new_outcome_list[-1] == "blank":
            new_outcome_list.append("blank")
            count += 1
        else:
            new_element = column3[random.randint(0,3)]
            if new_element not in new_outcome_list:
                new_outcome_list.append(new_element)
                count += 1
            else:
                pass
    if new_outcome_list not in outcome_set:
        outcome_set.append(new_outcome_list)
print(len(outcome_set))
for i in outcome_set:
    print(i)
    
