words = ['apple','apps','ape']

words.sort(key=len)

x=''

breaking = 1
                        
for i in range(0, len(words[0])):
        for j in range(1, len(words)):
                if words[j][0:i+1] != words[0][0:i+1]:
                        x = words[0][0:i]
                        breaking = 0
                        break
                else :
                        x = words[0][0:i+1]


        if breaking == 0:
                break
                        
                        
        
        
               
print(x)               



