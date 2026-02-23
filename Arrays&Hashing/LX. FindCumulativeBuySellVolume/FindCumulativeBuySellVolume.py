def totalSharesPerDay(stocks):
    volume = {} # {day: {company: stocks}}
    prev = {}
    for i in range(len(stocks)):
        comp = stocks[i]
        for data in comp:
            date = data[0]
            vol = data[-1]
            month, day = date[0], date[-1]
            if day in volume:
                volume[day][i] = vol
            else:
                volume[day] = {}
                volume[day][i] = vol 
    
    days = sorted(volume.keys())
    result = []

    for day in days:
        for comp, vol in volume[day].items():
            prev[comp] = vol 
    
        total = sum(prev.values())
        result.append(total)

    return result

stocks = [("5/1", 100), ("5/5", 200)],[("5/5",  50), ("5/8", 100)], [("5/1", 200), ("5/8", 100)]
print(totalSharesPerDay(stocks))  
