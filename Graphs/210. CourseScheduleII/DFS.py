def findOrder(numCourses: int, prerequisites) -> list[int]:
    # First we do the premapping
    premap = {i : [] for i in range(numCourses)}

    for course, pre in prerequisites:
        premap[course].append(pre)
    

    visiting = set()
    added = set()
    result = []

    def dfs(course):
        if course in visiting:
            return False 
    
        if course in added:
            return True 

        visiting.add(course)
        for prereq in premap[course]:
            if not dfs(prereq):
                return False 
            if prereq not in added:
                added.add(prereq)
                result.append(prereq)
        
        visiting.remove(course)
        added.add(course)
        result.append(course)

        return True 
    
    for course in range(numCourses):
        if not dfs(course):
            return []
        if course not in added:
            added.add(course)
            result.append(course) 
    
    return result