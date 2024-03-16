class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

        return (int(coordinates[1]) + dict[coordinates[0]])%2 == 1
        