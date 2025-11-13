def canFinish(numCourses: int, prerequisites: list[list[int]]) -> int:
    # first we do the premapping of courses
    premap = {i : [] for i in range(numCourses)}

    visiting = set()
    def dfs(course):
        if premap[course] == []:
            return True 
        if course in visiting:
            return False 

        visiting.add(course)
        for pre in premap[course]:
            if not dfs(pre):
                return False 
        visiting.remove(course)
        premap[course] = []
        return True 
    
    for course in range(numCourses):
        if not dfs(course):
            return False 
    
    return True 