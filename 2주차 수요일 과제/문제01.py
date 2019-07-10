words = ['dog','dogs','doge']

words.sort(key=len)

for i in range(0, len(words[0])+1):
        for j in range(1, len(words)):
                if words[j][0:i] == words[0][0:i] :
                        x = words[0][0:i]
                else :
                        break

        
print(x)
                        

               
               



