class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count = 0
        #sort the arrays
        seats.sort()
        students.sort()
        print(seats, students)
        for i in range(0, len(students)):
            if seats[i]!=students[i]:
                count+=abs(students[i]-seats[i])
        return count 
        