class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        m = 1
        types = {}
        while r < len(fruits):
            if fruits[r] not in types:
                if len(types.keys())==2:
                    #cannot add
                    key1, key2 = types.keys()
                    m = max(m, (types[key1]+types[key2]))

                    while True:
                        types[fruits[l]]-=1
                        if types[fruits[l]]==0:
                            del types[fruits[l]]
                            l+=1
                            break
                        l+=1
                    #add the third new fruit and remove the first one
                
                types[fruits[r]]=1
            else:
                types[fruits[r]]+=1
            r+=1
        if len(types.keys())==2:
            key1, key2 = types.keys() 
            m = max(m, (types[key1]+types[key2]))
        if len(types.keys())==1:
            for key in types.keys():
                m = max(m, types[key])
        return m


        