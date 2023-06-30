def fifo(numbers, num_frames):
    frames = []     # List of numbers
    hits = 0
    misses = 0
    result = []   # List of dictionaries
    tempFrames = [] #this list have the same number of elements as num_frames

    for num in numbers:
        step = {}    # step is a dictionary
        step["page"] = num       # step["page"] is a key and num is a value

        if num in frames:    # if num is in frames then it is a hit
            hits += 1
            step["hit_miss"] = "Hit"
        else:
            if len(frames) < num_frames:   # for the first time, frames is empty so len(frames) is 0 
                frames.append(num)    # append is a function to add a value to a list
                tempFrames.append(num)
            else:
                
                if frames[0] in tempFrames:
                        index = tempFrames.index(frames[0])
                        tempFrames[index] = num 
                        
                frames.pop(0)     # pop is a function to remove the oldest value from a list.
                frames.append(num)        

            misses += 1
            step["hit_miss"] = "Miss"
            
        step["frames"] = tempFrames.copy()
        result.append(step)    # dictionary is added to the list

    total_faults = misses

    return result, total_faults




def lru(numbers, num_frames):
    frames = []
    hits = 0
    misses = 0
    result = []
    tempFrames = []

    for num in numbers:
        step = {}
        step["page"] = num
        #step["frames"] = frames.copy()

        if num in frames:
            hits += 1
            frames.remove(num)
            frames.append(num)
            step["hit_miss"] = "Hit"
            
        else:
            if len(frames) < num_frames:
                frames.append(num)
                tempFrames.append(num)
                
            else:
                
                if frames[0] in tempFrames:
                        index = tempFrames.index(frames[0])
                        tempFrames[index] = num 
                        
                frames.pop(0)
                frames.append(num)
                
            misses += 1
            step["hit_miss"] = "Miss"

        step["frames"] = tempFrames.copy()
        result.append(step)

    total_faults = misses

    return result, total_faults


def lfu(numbers, num_frames):
    frames = []
    hits = 0
    misses = 0
    counter = {}
    result = []
    tempFrames = []

    for num in numbers:
        step = {}
        step["page"] = num

        if num in frames:
            hits += 1
            counter[num] += 1
            step["hit_miss"] = "Hit"
        else:
            if len(frames) < num_frames:
                frames.append(num)
                tempFrames.append(num)
                counter[num] = 1
            else:
                min_count = min(counter.values())
                least_frequent = [page for page, count in counter.items() if count == min_count]
                page_to_remove = least_frequent[0]  
                frames.remove(page_to_remove)
                
                if page_to_remove in tempFrames:
                        index = tempFrames.index(page_to_remove)
                        tempFrames[index] = num 
                
                del counter[page_to_remove]  
                frames.append(num)
                counter[num] = 1
            misses += 1
            step["hit_miss"] = "Miss"

        step["frames"] = tempFrames.copy()
        result.append(step)

    total_faults = misses

    return result, total_faults




def mfu(numbers, num_frames):
    frames = []
    hits = 0
    misses = 0
    counter = {} 
    result = []
    tempFrames = []
    
    tempCounter = {}
    for num in numbers:
        if num in tempCounter:
            tempCounter[num] = 0 
        else:
            tempCounter[num] = 0
            
    # print("val",tempCounter)       #make tempCounter dictionary size of numbers values and set all values to 0

    for num in numbers:
        step = {}
        step["page"] = num
        
        
        if num in tempCounter:
            tempCounter[num] += 1
        
        if num in frames:
            hits += 1
            counter[num] += 1
            
            step["hit_miss"] = "Hit"
        else:
            if len(frames) < num_frames:
                frames.append(num)
                tempFrames.append(num)
                counter[num] = 1
                tempCounter[num] = 1
            else:
                max_count = max(counter.values()) # max_count is largest value in the dictionary
                most_frequent = [page for page, count in counter.items() if count == max_count]  #most_frequent is a list
                
                # print("most_frequent",most_frequent)
                # print("tempCounter",tempCounter)
                # print("counter",counter)
                
                max_value = None
                max_count = 0

                for value in most_frequent:
                    if value in tempCounter:
                        count1 = tempCounter[value] # count1 is the value of the key in tempCounter dictionary
                        
                        # print (value,count1)
                        
                        if count1 > max_count:
                            max_count = count1
                            max_value = value

                page_to_remove = max_value
                # page_to_remove = most_frequent[0] # if there are more than one page with the same count, then the first one is removed
                
                if page_to_remove in frames:
                    frames.remove(page_to_remove)
            
                    if page_to_remove in tempFrames:
                            index = tempFrames.index(page_to_remove)
                            tempFrames[index] = num 
                
                
                if page_to_remove in counter:
                    del counter[page_to_remove]
                    frames.append(num)
                    counter[num] = 1
                
            misses += 1
            step["hit_miss"] = "Miss"

        step["frames"] = tempFrames.copy()
        result.append(step)

    # print(counter)
    # print("val",tempCounter)
    total_faults = misses

    return result, total_faults

# def mfu(numbers, num_frames):
#     frames = []
#     hits = 0
#     misses = 0
#     counter = {}  
#     result = []
#     tempFrames = []
    
#     for num in numbers:
#         if num in counter:
#             counter[num] = 0 
#         else:
#             counter[num] = 0
            
#     print("val",counter) 

#     for num in numbers:
#         step = {}
#         step["page"] = num

#         if num in frames:
#             hits += 1
#             counter[num] += 1
#             step["hit_miss"] = "Hit"
#         else:
#             if len(frames) < num_frames:
#                 frames.append(num)
#                 tempFrames.append(num)
#                 counter[num] = 1
#             else:
#                 max_count = max(counter.values())
#                 print(max_count)
#                 print(counter)
#                 most_frequent = [page for page, count in counter.items() if count == max_count]  #most_frequent is a list
#                 page_to_remove = most_frequent[0] # if there are more than one page with the same count, then the first one is removed
#                 frames.remove(page_to_remove)
                
#                 if page_to_remove in tempFrames:
#                         index = tempFrames.index(page_to_remove)
#                         tempFrames[index] = num 
                
#                 # del counter[page_to_remove]   # del is a function to remove a key from a dictionary
#                 frames.append(num)
#                 counter[num] = 1
#             misses += 1
#             step["hit_miss"] = "Miss"

#         step["frames"] = tempFrames.copy()
#         result.append(step)

#     # print(counter)
#     total_faults = misses

#     return result, total_faults

