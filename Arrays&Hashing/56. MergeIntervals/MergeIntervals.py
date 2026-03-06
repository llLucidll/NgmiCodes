def merge(intervals):
    intervals.sort(key = lambda interval: interval[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = output[-1][1]

        if last_end >= start:
            output[-1][1] = max(end, last_end)
        else:
            output.append([start, end])
    
    return output