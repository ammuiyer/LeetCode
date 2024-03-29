class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students[0])
                students.pop(0)
            if len(sandwiches)>0 and sandwiches[0] not in students:
                return len(students)
        return len(students)

        