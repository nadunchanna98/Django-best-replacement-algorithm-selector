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
    result = []
    tempNumbers = []

    for num2 in numbers:
        step = {}
        step["page"] = num2
        tempNumbers.append(num2)

        if num2 in frames:
            hits += 1
            step["hit_miss"] = "Hit"
        else:
            if len(frames) < num_frames:
                frames.append(num2)
                misses += 1
                step["hit_miss"] = "Miss"
            else:
                min_freq = float('inf')
                min_freq_num = None

                for num3 in frames:
                    freq = tempNumbers.count(num3)
                    if freq < min_freq:
                        min_freq = freq
                        min_freq_num = num3
                    elif freq == min_freq:
                        if tempNumbers.index(num3) > tempNumbers.index(min_freq_num):
                            min_freq_num = min_freq_num
                        else:
                            min_freq_num = num3

                frames[frames.index(min_freq_num)] = num2
                misses += 1
                step["hit_miss"] = "Miss"

        step["frames"] = frames.copy()
        result.append(step)

    total_faults = misses

    return result, total_faults

def mfu(numbers, num_frames):
    frames = []
    hits = 0
    misses = 0
    result = []
    tempNumbers = []

    for num2 in numbers:
        step = {}
        step["page"] = num2
        tempNumbers.append(num2)

        if num2 in frames:
            hits += 1
            step["hit_miss"] = "Hit"
        else:
             if len(frames) < num_frames:
                 frames.append(num2)
                 misses += 1
                 step["hit_miss"] = "Miss"
             else:
                 frq = 0
                 frqNum = 0
                 for num3 in frames:
                     tempFrq = 0
                     for num4 in tempNumbers:
                         if num3 == num4:
                             tempFrq =  tempFrq + 1
                     if tempFrq > frq:
                         frq = tempFrq
                         frqNum = num3
                     elif tempFrq == frq:
                         if tempNumbers.index(num3) > tempNumbers.index(frqNum):
                             frqNum = frqNum
                         else:
                             frqNum = num3
                 frames[frames.index(frqNum)] = num2
                 misses += 1
                 step["hit_miss"] = "Miss"

        step["frames"] = frames.copy()
        result.append(step)

    total_faults = misses

    return result, total_faults


