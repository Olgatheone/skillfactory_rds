import numpy as np
number = np.random.randint(1,100)    # загадали число
print ("Загадано число",number)
numbers=[x for x in range(1, 100)]
a=int (len(numbers)/2)
for i in range(1,120):
    if number in numbers[0:a]:
        numbers=numbers[0:a]
        a=int(len(numbers)/2)
        if a==0:
            break
    else:
        numbers=numbers[a:]
        a=int(len(numbers)/2)
        if a==0:
            break
predict=numbers[0]
print ('За '+str(i)+ ' попыток отгадано число ' + str(predict))
