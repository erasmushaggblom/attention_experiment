import random

schools = ["Pleasant High", "Deer High", "Wood High", "Lone High", "Raven High", "Timber High", "Coast High", "Church High", "Fork High", "Green High", "Sky High", "Sun High", "Beach High", "Harbour High", "View High", "Marble High", "Willow High", "Moon High", "Oak High", "Hill High"]
statistical_historical = ["statistical_historical_negative_1", "statistical_historical_negative_2", "statistical_historical_positive_1", "statistical_historical_positive_2"]
statistical_relative = ["statistical_relative_negative_1", "statistical_relative_negative_2", "statistical_relative_positive_1", "statistical_relative_positive_2"]
narrative_historical = ["narrative_historical_negative_1", "narrative_historical_negative_2", "narrative_historical_positive_1", "narrative_historical_positive_2"]
narrative_relative = ["narrative_relative_negative_1", "narrative_relative_negative_2", "narrative_relative_positive_1", "narrative_relative_positive_2"]
no_comparison = ["no_comparison_1", "no_comparison_2", "no_comparison_3", "no_comparison_4"]
final_list = []
number3 = 0
count = 0

for i in range(10000): #generate 10000 random combinations
    conditions = []
    for i in statistical_historical:
        conditions.append((i, 1))
    for i in statistical_relative:
        conditions.append((i, 2))
    for i in narrative_historical:
        conditions.append((i, 3))
    for i in narrative_relative:
        conditions.append((i, 4))
    for i in no_comparison:
        conditions.append((i, 5))
    number = 10
    number2 = 9
    pairs = []
    pairs1 = []
    pairs2 = []
    new_conditions = []
    random.shuffle(schools)
    random.shuffle(conditions)

    new_conditions = conditions

    failure_point = False
    while True: #the same condition cannot be paired wirh itself
        for i in range(number):
            if conditions[i][1] == conditions[i+number][1]:
                item_shuffle = conditions[i]
                conditions.pop(i)
                conditions.append(item_shuffle)
        for i in range(number):
            if conditions[i][1] == conditions[i+number][1]:
                number3 += 1
        
        if number3 > 0:
            failure_point = True
            number3 = 0
        
        else:
            failure_point = False
            number3 = 0
            number2 += 1
        if failure_point == False:    
            break
        
    new_conditions = conditions
    temp_list = []
    for u in range(len(new_conditions)):
        temp_list.append((new_conditions[u][0], schools[u]))
    if temp_list not in final_list: #each combination needs to be unique
        final_list.append(temp_list)
        count += 1

print(f"{count} unique random combinations created")


with open("randomised_list.txt", "w") as my_file:
    for i in final_list:
        my_file.write(f"{i}")
        my_file.write("\n")

