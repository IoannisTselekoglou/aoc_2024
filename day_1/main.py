def prob_1():
    row_1 = []
    row_2 = []
   
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            value1, value2 = line.split()  
            row_1.append(int(value1))
            row_2.append(int(value2))
    
    row_1.sort()
    row_2.sort()
   
    results = [abs(row_1[i] - row_2[i]) for i in range(len(row_1))]
    print(sum(results))



def prob_2():
    row_1 = []
    row_2 = []
    sum_score = 0
    
    
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            value1, value2 = line.split()  
            row_1.append(value1)
            row_2.append(value2)

    sim_dict = {}
    
    for i in row_2:
        if i not in sim_dict:
            sim_dict[i] = 1
        else:
            sim_dict[i] += 1
    
    
    for i in row_1:
        if i in sim_dict:
            sum_score += int(i)*sim_dict[i]

    print(sum_score)

prob_1()
prob_2()
