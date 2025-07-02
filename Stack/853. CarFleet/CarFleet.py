def carFleet(target: int, position, speed) -> int:
    pairs = [(p, s) for p, s in zip(postion, speed)]
    pairs.sort(reverse=True)
    stack = []


    for p, s in pairs:
        stack.append((target - p) / s)

        # The check for redundant car fleets
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    
    return len(stack)