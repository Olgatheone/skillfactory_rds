def my_game(number):
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
    return (count)
def score_game(my_game):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(500))
    for number in random_array:
        count_ls.append(my_game(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(my_game)
