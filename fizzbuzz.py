def fizzbuzz(num):
    for i in range(20):
        n = i+1
        if n%3 ==0 and n%5 == 0:
            print('fizzbuzz')
        elif n%3 == 0:
            print('fizz')
        elif n%5 == 0:
            print('buzz')
        else: print(n)
if __name__ == '__main__':
    fizzbuzz(5)