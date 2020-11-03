import numpy as np
import timeit
from time import time


def main():
    a = int(input('Введите число строк: '))
    b = int(input('Введите число столбцов: '))
    m1 = np.random.randint(-50, 50, (a, b))
    m2 = np.random.randint(-50, 50, (a, b))
    print(m1, m2, sep='\n\n', end='\n\n\n')

    print('Сумма: \n', m1 + m2, '\n\nПроизведение: \n', m1 * m2)

    try:
        print('\n\nОпределитель первой матрицы: ', np.linalg.det(m1))
        print('Определитель второй матрицы: ', np.linalg.det(m2))
    except:
        print('\n\nНевозможно вычислить определители')

    try:
        print('\n\nОбратная матрица для первой:\n', np.linalg.inv(m1))
        print('\n\nОбратная матрица для второй:\n', np.linalg.inv(m2))
    except:
        print('\n\nОбратные матрицы не существуют')

    def save_matrix(matrix, filename: str = "matrix.txt"):
        try:
            np.savetxt(filename, matrix, delimiter=",")
        except Exception as err:
            print(err)

    def load(filename: str = "matrix.txt") -> np.array:
        try:
            matrix = np.loadtxt(filename, delimiter=",")
            print('\nОбратная матрица из файла:\n', np.linalg.inv(matrix))
            return matrix
        except Exception as err:
            print(err)

    start = time()
    np.linalg.inv(np.random.randint(-50, 50, (10, 10)))
    print('\nВремя обращения матрицы 10х10: ', time() - start)

    start = time()
    np.linalg.inv(np.random.randint(-50, 50, (100, 100)))
    print('\nВремя обращения матрицы 100х100: ', time() - start)

    start = time()
    np.linalg.inv(np.random.randint(-50, 50, (1000, 1000)))
    print('\nВремя обращения матрицы 1000х1000: ', time() - start)

    save_matrix(m1)
    m1 = load()


if __name__ == "__main__":
    main()
