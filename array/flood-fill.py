class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = [(sr, sc)]
        scolor = image[sr][sc]
        visited = set()
        image[sr][sc] = color
        while q:
            currr, currc = q.pop(0)
            #print(currr, currc)
            if currr<len(image)-1 and image[currr+1][currc] == scolor:
                image[currr+1][currc] = color
                if (currr+1, currc) not in visited:
                    q.append((currr+1, currc))
            if currr>0 and image[currr-1][currc] == scolor:
                image[currr-1][currc] = color
                if (currr-1, currc) not in visited:
                    q.append((currr-1, currc))
            if currc<len(image[0])-1 and image[currr][currc+1] == scolor:
                image[currr][currc+1] = color
                if (currr, currc+1) not in visited:
                    q.append((currr, currc+1))
            if currc>0 and image[currr][currc-1] == scolor:
                image[currr][currc-1] = color
                if (currr, currc-1) not in visited:
                    q.append((currr, currc-1))
            visited.add((currr, currc))
        return image

