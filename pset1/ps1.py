###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    def load(herd, acc, rest_limit):
        rest_herd = herd[:]
        for (name, weight) in herd:
            if weight <= rest_limit:
                acc.append(name)
                rest_limit -= weight
                rest_herd.remove((name, weight))
                if rest_limit == 0:
                    break
        return (rest_herd, acc)

    loads = []
    herd = sorted(cows.items(), key = lambda x: x[1], reverse = True)
    while herd:
        (herd, cur_load) = load(herd, [], limit)
        loads.append(cur_load)
    return loads

def weight_of_load(cows, load):
    """
    Counts the total weight of a load.
    """
    weight = 0
    for cow in load:
        weight += cows[cow]
    return weight

def weight_is_valid(cows, loads, limit):
    """
    Checks that weight of each load in loads are whithin the limit.
    """
    for load in loads:
        if weight_of_load(cows, load) > limit:
            break
    else:
        return True
    return False


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    best_loads = []
    length_of_best_loads = len(list(cows))
    for loads in get_partitions(cows):
        if weight_is_valid(cows, loads, limit) and\
           len(loads) <= length_of_best_loads:
            best_loads = loads
            length_of_best_loads = len(loads)
    return best_loads

        
# Problem 3
def compare_cow_transport_algorithms(cows, limit):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    print("greedy time is {}".format(end - start))

    start = time.time()
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    print("brute time is {}".format(end - start))
    return None


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
compare_cow_transport_algorithms(cows,limit)
