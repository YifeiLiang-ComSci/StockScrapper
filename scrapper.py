import collections
def getLargestString(originalLabel, charLimit):
    # WRITE YOUR CODE HERE
    def findIndex(arr,i):
        found = -1
        for c in range(i+1, len(arr)):
            
            key,value = arr[c]
            if(value == 0):
                continue
            if value != 0:
                return c
        return found
    freq = collections.Counter(originalLabel)
    temp = [[key,value] for key,value in freq.items()]
    arr = sorted(temp, key = lambda w:w[0], reverse = True)
    ans = ""
    label = "".join(sorted(originalLabel,reverse = True))
    for i in range(len(arr)):
        key,value = arr[i]
        if value == 0:
            return 
        while(value > charLimit):
            nextIndex = findIndex(arr, i)
            
            ans += key* charLimit
            print(ans)
            print(arr)
            if(nextIndex == -1):
                return ans
            
            value -= charLimit
            ans += arr[nextIndex][0]
            arr[nextIndex][1] -= 1
        if(value != 0):
            ans += (value * key)
    return ans
        
    pass
print(getLargestString("zzxxax",2))