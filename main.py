#the knapsack problema with hill climbing steepest descent 2 statment from homework 

import random

def read_data():
    data = []
    with open('data.txt', 'r') as file:
        for line in file:
            data.append([int(x) for x in line.split()])
    return data[0][0], data[1:-1], data[-1][0]
    
len_of_data, data, max_weight = read_data()

def calculate_weight(x):
    weight_sum = 0
    for i in range(len_of_data):
        if x[i] == 1:
            weight_sum += data[i][1]
    return weight_sum

def calculate_value(x):
    value_sum = 0
    for i in range(len_of_data):
        if x[i] == 1:
            value_sum += data[i][0]
    return value_sum

def fitness(x):
    if calculate_weight(x) > max_weight:
        return -1
    return calculate_value(x)

def calculate_neighbours(x):
    neighbours = []
    for i in range(10):
        y = x.copy()
        j = random.randint(0, len_of_data-1)
        y[j] = 1 - y[j]
        neighbours.append(y)
    return neighbours

def steeptest_descent():
    x = [0 for _ in range(len_of_data)]
    for _ in range(10000):
        neighbours = calculate_neighbours(x)
        best_neighbour = neighbours[0]
        for neighbour in neighbours:
            if fitness(neighbour) > fitness(best_neighbour):
                best_neighbour = neighbour
        if fitness(best_neighbour) > fitness(x):
            x = best_neighbour
    print(fitness(x)) # the best total value that you can get after 10000 iterations, the iterations can be changed:)
    print(calculate_weight(x)) # the weight of the best value 
    print(x) # the best items to pick form the data list

steeptest_descent()
