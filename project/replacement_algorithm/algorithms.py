def fifo(numbers, num_frames):
    frames = []     # List of numbers
    hits = 0
    misses = 0
    result = []   # List of dictionaries

    for num in numbers:
        step = {}    # step is a dictionary
        step["page"] = num       # step["page"] is a key and num is a value
        # step["frames"] = frames.copy()   # step["frames"] is a key and frames.copy() is a value

        if num in frames:    # if num is in frames then it is a hit
            hits += 1
            step["hit_miss"] = "Hit"
        else:
            if len(frames) < num_frames:   # for the first time, frames is empty so len(frames) is 0 and num_frames is 3
                frames.append(num)    # append is a function to add a value to a list
            else:
                frames.pop(0)     # pop is a function to remove a value from a list.
                frames.append(num)
            misses += 1
            step["hit_miss"] = "Miss"

        step["frames"] = frames.copy()
        result.append(step)    # dictionary is added to the list

    total_faults = misses

    return result, total_faults



def lru(numbers, num_frames):
    frames = []
    hits = 0
    misses = 0
    result = []

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
            else:
                frames.pop(0)
                frames.append(num)
            misses += 1
            step["hit_miss"] = "Miss"

        step["frames"] = frames.copy()
        result.append(step)

    total_faults = misses

    return result, total_faults


def lfu(numbers, num_frames):
    frames = []
    hits = 0
    misses = 0
    counter = {}
    result = []

    for num in numbers:
        step = {}
        step["page"] = num
        # step["frames"] = frames.copy()

        if num in frames:
            hits += 1
            counter[num] += 1
            step["hit_miss"] = "Hit"
        else:
            if len(frames) < num_frames:
                frames.append(num)
                counter[num] = 1
            else:
                min_count = min(counter.values())
                least_frequent = [page for page, count in counter.items() if count == min_count]
                page_to_remove = least_frequent[0]
                frames.remove(page_to_remove)
                del counter[page_to_remove]
                frames.append(num)
                counter[num] = 1
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
    counter = {}
    result = []

    for num in numbers:
        step = {}
        step["page"] = num
        step["frames"] = frames.copy()

        if num in frames:
            hits += 1
            counter[num] += 1
            step["hit_miss"] = "Hit"
        else:
            if len(frames) < num_frames:
                frames.append(num)
                counter[num] = 1
            else:
                max_count = max(counter.values())
                most_frequent = [page for page, count in counter.items() if count == max_count]
                page_to_remove = most_frequent[0]
                frames.remove(page_to_remove)
                del counter[page_to_remove]
                frames.append(num)
                counter[num] = 1
            misses += 1
            step["hit_miss"] = "Miss"

        step["frames"] = frames.copy()
        result.append(step)

    total_faults = misses

    return result, total_faults
