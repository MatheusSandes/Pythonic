from functools import total_ordering

@total_ordering
class Students:
    def __init__(self, cgpa):
        self.cgpa = cgpa
  
    def __lt__(self, other):
        return self.cgpa<other.cgpa
  
Arjun = Students(8.6)
  
Ram = Students(7.5)
  
print(Arjun.__lt__(Ram))