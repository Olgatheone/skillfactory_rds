import numpy as np
#count=1
def my_game(*args):
    count = 0
    number = np.random.randint(1,100)
    numbers=[x for x in range(1, 100)]
    a=int(len(numbers)/2)
    while True:
        count+=1
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
    return (count, predict)
print ('За '+ str(my_game()[0])+ ' попыток отгадано число '+ str(my_game()[1]))
