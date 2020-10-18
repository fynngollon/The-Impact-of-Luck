from random import randint

instance_set, picked_list = [], []
skill_rating, luck_rating, total_rating = 0, 0, 0

def create_set(applicants, skill_ratio):
    for i in range(0, applicants):
        skill_rating = randint(0, 10000) / 10000
        luck_rating = randint(0, 10000) / 10000
        total_rating = round(skill_rating * skill_ratio + luck_rating * (1 - skill_ratio), 4)

        instance_set.append(
            [len(instance_set), skill_rating, luck_rating, total_rating])
        
def pick(picking):
    sorted_list = quicksort(instance_set, 3)
    global picked_list
    picked_list = sorted_list[len(sorted_list)-picking:]
    picked_list.reverse()

def pick_skill(picking):
    sorted_list = quicksort(instance_set, 1)
    global picked_list
    picked_list = sorted_list[len(sorted_list)-picking:]
    picked_list.reverse()

def get_picked():
    return picked_list

def measure_overlap(picking, picked_by_total, picked_by_skill):
    overlap = 0
    for i in range(0, picking):
        for j in range(0, picking):
            if picked_by_total[i][0] == picked_by_skill[j][0]:
                overlap += 1

    return overlap

def run(applicants = 18300, picking = 48, skill_ratio = 0.95):
    global instance_set
    instance_set = []
    create_set(applicants, skill_ratio)

    pick(picking)
    picked_list = get_picked()
    pick_skill(picking)
    picked_skill_list = get_picked()
    
    for i in range(0, picking):
        skill_ranking = ""
        for j in range(0, picking):
            if picked_list[i][0] == picked_skill_list[j][0]:
                skill_ranking = "(" + str(j+1) + ")"
        print('{:2d}'.format(i+1) + ": " + '{:<6}'.format(picked_list[i][3]) + 
              "         [SR: " + '{:<6}'.format(picked_list[i][1]) + "; LR: " + '{:<6}'.format(picked_list[i][2]) + "; ID: " + '{:5}'.format(picked_list[i][0]) + "] " + skill_ranking)

    print("")
    
    for i in range(0, picking):
        total_ranking = ""
        for j in range(0, picking):
            if picked_skill_list[i][0] == picked_list[j][0]:
                total_ranking = "(" + str(j+1) + ")"
        print('{:2d}'.format(i+1) + ": " + '{:<6}'.format(picked_skill_list[i][1]) + 
              "         [SR: " + '{:<6}'.format(picked_skill_list[i][1]) + "; LR: " + '{:<6}'.format(picked_skill_list[i][2]) + "; ID: " + '{:5}'.format(picked_skill_list[i][0]) + "] " + total_ranking)

    lucky_ones = picking - measure_overlap(picking, picked_list, picked_skill_list)
    print("\n" + str(lucky_ones) + " of " + str(picking) + " applicants were picked with the help of luck!")

    


# Quicksort
    
def partition(i_set, start, end, index):
    follower = pivot = start
    while pivot < end:
        if i_set[pivot][index] <= i_set[end][index]:
            i_set[follower], i_set[pivot] = i_set[pivot], i_set[follower]
            follower += 1
        pivot += 1
    i_set[follower], i_set[end] = i_set[end], i_set[follower]
    return follower

def _quicksort(i_set, start, end, index):
    if start >= end:
        return
    p = partition(i_set, start, end, index)
    _quicksort(i_set, start, p-1, index)
    _quicksort(i_set, p+1, end, index)
    
def quicksort(i_set, index):
    _quicksort(i_set, 0, len(i_set)-1, index)
    return i_set
