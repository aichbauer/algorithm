import time


def fibIter(n):
    """ calculate the fibonacci number for n iterative

        :param      n:      (int) number to calculate
        :return     b:      (int) fibonacci for n
    """

    a = 0
    b = 1
    temp = 0
    while n >= 0:
        temp = a
        a = a + b
        b = temp
        n = n - 1
    return b


def fibRecur(n):
    """ calculate the fibonacci number for n recursive

        :param              n:      (int) number to calculate
        :return f(n-1)+f(n-2):      (int) fibonacci for n
    """
    if n <= 2:
        return 1

    return fibRecur(n - 1) + fibRecur(n - 2)

def fibIterSquar(n):
    """ calculate the fibonacci number for n with iterative squaring

        :param        n:        (int) number to calculate
        :return     a+c:        (int) fibonacci for n
    """
    if n <= 2: return 1;
    result = matrixMultiplication(n - 2)
    return result[0] + result[2]


def matrixMultiplication(n):
    """ calculate the matrix for n

        :param               n:     (int) number to calculate
        :return         matrix:     (list) the matrix
    """
    mat = [1, 1, 1, 0]
    if n < 2:
        return mat
    elif n % 2 == 0:  # even
        result = matrixMultiplication(n / 2)
        return [(result[0] * result[0]) + (result[1] * result[2]),
                (result[0] * result[1]) + (result[1] * result[3]),
                (result[2] * result[0]) + (result[2] * result[3]),
                (result[2] * result[1]) + (result[3] * result[3])]
    else:  # odd
        result = matrixMultiplication(n / 2)
        return [(result[0] * result[0]) + (result[1] * result[2]) + (result[0] * result[1]) + (result[1] * result[3]),
                (result[0] * result[0]) + (result[1] * result[2]),
                (result[2] * result[0]) + (result[2] * result[3]) + (result[2] * result[1]) + (result[3] * result[3]),
                (result[2] * result[0]) + (result[3] * result[2])]


# Main program
if __name__ == '__main__':
    start_time = time.time()
    for i in range(0, 5):
        print fibIter(100000)
    print("--- %s seconds ---" % (time.time() - start_time))


