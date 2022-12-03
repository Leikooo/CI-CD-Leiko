import test
from calculator import Calculator

def main():
    test.test_func()
    a=int(input('Enter a first number: '))
    b=int(input('Enter a second number: '))
    calc=Calculator()
    print('Результат', calc.add(a,b))

if __name__ == "__main__":
    main()
    input('Press ENTER to exit')

