import numpy as np
from fractions import Fraction as frac
import sys

def main():
    input_matrix = get_matrix()
    matrix1 = Matrix(input_matrix)
    while True:
        print('')
        choice1 = int(input('Choose the operation:\n1. Row echelom form\n2. Reduced row echelom form\n3. Determinant\n4. Transpose\n5. Inverse\n6. Basic calculation\n7. Add another matrix\n8. Exit and print the matrix\n: ').strip())
        if choice1 == 1:
            matrix1 = matrix1.ref()
            print('')
            print('Row echelom form:')
            sys.exit(print_matrix(matrix1))

        elif choice1 == 2:
            matrix1 = matrix1.rref()
            print('')
            print('Reduced row echelom form:')
            sys.exit(print_matrix(matrix1))

        elif choice1 == 3:
            if square_matrix(input_matrix) and valid_size(input_matrix):
                deter = matrix1.det()
                print('')
                sys.exit(f'Determinant: {deter}')

            else:
                print('')
                print('Only support 1 x 1, 2 x 2, and 3 x 3 square matrix')

        elif choice1 == 4:
            matrix1 = matrix1.transpose()
            print('')
            print('Transpose:')
            sys.exit(print_matrix(matrix1))

        elif choice1 == 5:
            try:
                if square_matrix(input_matrix) and valid_size(input_matrix):
                    matrix1 = matrix1.inverse()
                    print('')
                    print('Inverse:')
                    sys.exit(print_matrix(matrix1))

                else:
                    print('')
                    print('Only support 1 x 1, 2 x 2, and 3 x 3 square matrix')

            except ZeroDivisionError:
                print('')
                print('This is a non-invertible matrix')

        elif choice1 == 6:
            while True:
                print('')
                choice2 = int(input('1. Multiplication\n2. Division\n: ').strip())
                if choice2 == 1 or choice2 == 2:
                    print('')
                    num = input('By: ')
                    matrix1 = matrix1.basic_cal(choice2, num)
                    print('')
                    print('Result:')
                    sys.exit(print_matrix(matrix1))

                else:
                    print('')
                    print('Invalid choice, please try again.')
                    continue

        elif choice1 == 7:
            print('')
            matrix2 = Matrix(get_matrix())
            while True:
                print('')
                choice2 = int(input('Choose the operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n: ').strip())
                print('')
                if choice2 == 1:
                    matrix1 = matrix1 + matrix2
                    print('')
                    print('Result:')
                    sys.exit(print_matrix(matrix1))

                elif choice2 == 2:
                    matrix1 = matrix1 - matrix2
                    print('')
                    print('Result:')
                    sys.exit(print_matrix(matrix1))

                elif choice2 == 3:
                    matrix1 = matrix1 * matrix2
                    print('')
                    print('Result:')
                    sys.exit(print_matrix(matrix1))

                else:
                    print('')
                    print('Invalid choice, please try again.')
                    print('')
                    continue

        elif choice1 == 8:
            sys.exit(print_matrix(matrix1))

        else:
            print('')
            print('Invalid choice, please try again.')
            print('')
            continue


def get_matrix():
    matrix = {}
    i = 0
    while True:
        try:
            row = input(f'Row {i+1} (press enter to skip): ').strip()
            if row != '':
                row = row.split(',')
                for n in range(len(row)):
                    if frac(row[n]):
                        row[n] = frac(row[n])
                        pass
                matrix[f'row{i+1}'] = row
                if i > 0 and len(matrix[f'row{i}']) != len(matrix[f'row{i+1}']):
                    raise ValueError
                i += 1

            else:
                return matrix
        except ValueError:
            pass


def print_matrix(matrix):
    if type(matrix) == Matrix:
        matrix = matrix.basic_cal(1,1)
    for r in range(len(matrix)):
        for e in range(len(matrix[f'row{r+1}'])):
            matrix[f'row{r+1}'][e] = str(matrix[f'row{r+1}'][e])
    print('')
    for matrix_row in matrix:
        print('['+' '.join(matrix[matrix_row])+']')


def square_matrix(matrix):
    if len(matrix) == len(matrix['row1']):
        return True

    else:
        return False

def valid_size(matrix):
    if len(matrix) in (1,2,3):
        return True

    else:
        return False




class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def column(self, col_num):
        column = []
        for r in range(len(self.matrix)):
            entry = self.matrix[f'row{r+1}'][col_num-1]
            column.append(entry)
        return column


    def rank(self):
        row_array = [self.matrix[f'row{i+1}'] for i in range(len(self.matrix))]
        for i in range((len(row_array[0]))):
            if i == 0:
                rank_key = 'x[0]'

            else:
                rank_key = rank_key + f', x[{i}]'
        data = list(sorted(row_array, key=lambda rank_key: rank_key, reverse=True))
        data = list(enumerate(data, start=1))
        for row in data:
            self.matrix[f'row{row[0]}'] = row[1]
        return self.matrix


    def ref(self):
        for r in range(len(self.matrix)):
            for i in range(len(self.matrix[f'row{r+1}'])):
                if self.matrix[f'row{r+1}'][i] != frac(0):
                    div = self.matrix[f'row{r+1}'][i]
                    new_row = [frac(x) / frac(div) for x in self.matrix[f'row{r+1}']]
                    self.matrix[f'row{r+1}'] = new_row
                    break
        self.matrix = self.rank()

        for r in range(2, len(self.matrix)+1):
            try:
                for i in range(len(self.matrix[f'row{r}'])):
                    if ((self.matrix[f'row{r-1}'][i] == frac(1) and self.matrix[f'row{r}'][i] == frac(1) and self.matrix[f'row{r-1}'][i-1] == frac(0) and self.matrix[f'row{r}'][i-1] == frac(0) and i > 0) or
                        (self.matrix[f'row{r-1}'][i] == frac(1) and self.matrix[f'row{r}'][i] == frac(1) and i == 0)):
                        array1 = np.array([x for x in self.matrix[f'row{r-1}']])
                        array2 = np.array([x for x in self.matrix[f'row{r}']])
                        subtracted_array = np.subtract(array2, array1)

                        subtracted_list = (subtracted_array).tolist()
                        if all(subtracted_array == frac(0)):
                            self.matrix[f'row{r}'] = subtracted_list

                        else:
                            for x in subtracted_list:
                                if x != frac(0):
                                    x_num = np.array(x)
                                    new_array = np.divide(subtracted_array, x_num)
                                    self.matrix[f'row{r}'] = (new_array).tolist()
                                    break

                    elif ((self.matrix[f'row{r-1}'][i] == frac(0) and self.matrix[f'row{r}'][i] == frac(1) and self.matrix[f'row{r-1}'][i-1] == frac(0) and self.matrix[f'row{r}'][i-1] == frac(0) and i > 0) or
                          (self.matrix[f'row{r-1}'][i] == frac(0) and self.matrix[f'row{r}'][i] == frac(1) and i == 0)):
                        array1 = np.array([x for x in self.matrix[f'row{i+1}']])
                        array2 = np.array([x for x in self.matrix[f'row{r}']])
                        subtracted_array = np.subtract(array2, array1)
                        subtracted_list = (subtracted_array).tolist()
                        for x in subtracted_list:
                            if x != frac(0):
                                x_num = np.array(x)
                                new_array = np.divide(subtracted_array, x_num)
                                self.matrix[f'row{r}'] = (new_array).tolist()
                                break

                    else:
                        pass
            except (IndexError, KeyError):
                print('error')

        diff = len(self.matrix) - len(self.matrix['row1'])
        row_len = len(self.matrix['row1'])
        if diff > 0:
            for r in range(1, diff+1):
                try:
                    row_array = np.array(self.matrix[f'row{row_len + r}'])
                    new_row_array = np.multiply(row_array, np.array(frac(0)))
                    self.matrix[f'row{row_len + r}'] = new_row_array.tolist()
                except KeyError:
                    break
        return self.matrix


    def rref(self):
        self.matrix = self.ref()
        print(self.matrix)
        print('')
        print('')
        range_end = min(len(self.matrix), len(self.matrix['row1']))
        for r in range(1, range_end):
            for i in range(1, range_end+1-r):
                print(f'row{r}_before:')
                print(self.matrix[f'row{r}'])
                row_array = np.array(self.matrix[f'row{r}'])
                target_row_array = np.array(self.matrix[f'row{r+i}'])
                target_multiplier = np.array(self.matrix[f'row{r}'][r+i-1])
                multiplied_array = np.multiply(target_multiplier, target_row_array)
                self.matrix[f'row{r}'] = np.subtract(row_array, multiplied_array).tolist()
                print(f'target_multiplier: {target_multiplier}')
                print(f'target_row_array: {target_row_array}')
                print(f'row{r}_after:')
                print(self.matrix[f'row{r}'])
                print('')
                print('')
        return self.matrix


    def det(self):
        if len(self.matrix) == len(self.matrix['row1']) == 1:
            det = -self.matrix['row1'][0]

        elif len(self.matrix) == 2 and len(self.matrix['row1']) == 2:
            det = self.matrix['row1'][0] * self.matrix['row2'][1] - self.matrix['row1'][1] * self.matrix['row2'][0]

        elif len(self.matrix) == 3 and len(self.matrix['row1']) == 3:
            det = (self.matrix['row1'][0] * (self.matrix['row2'][1] * self.matrix['row3'][2] - self.matrix['row2'][2] * self.matrix['row3'][1]) -
                   self.matrix['row1'][1] * (self.matrix['row2'][0] * self.matrix['row3'][2] - self.matrix['row2'][2] * self.matrix['row3'][0]) +
                   self.matrix['row1'][2] * (self.matrix['row2'][0] * self.matrix['row3'][1] - self.matrix['row2'][1] * self.matrix['row3'][0]))

        return frac(det)


    def transpose(self):
        out_matrix = {}
        for i in range(len(self.matrix['row1'])):
            out_matrix[f'row{i+1}'] = self.column(i+1)
        return out_matrix


    def inverse(self):
        if len(self.matrix) == 1:
            out_matrix = frac(1) / self.matrix['row1'][0]
            return out_matrix

        elif len(self.matrix) == 2:
            deter = self.det()
            self.matrix['row1'][0], self.matrix['row2'][1] = self.matrix['row2'][1], self.matrix['row1'][0]
            self.matrix['row1'][1] = -self.matrix['row1'][1]
            self.matrix['row2'][0] = -self.matrix['row2'][0]
            for r in range(1,3):
                for i in range(2):
                    self.matrix[f'row{r}'][i] = self.matrix[f'row{r}'][i] / deter
            return self.matrix

        elif len(self.matrix) == 3:
            deter = self.det()

            c11 = ((-1)**(1+1)) * (self.matrix['row2'][1] * self.matrix['row3'][2] - self.matrix['row2'][2] * self.matrix['row3'][1])
            c12 = ((-1)**(1+2)) * (self.matrix['row2'][0] * self.matrix['row3'][2] - self.matrix['row2'][2] * self.matrix['row3'][0])
            c13 = ((-1)**(1+3)) * (self.matrix['row2'][0] * self.matrix['row3'][1] - self.matrix['row2'][1] * self.matrix['row3'][0])

            c21 = ((-1)**(2+1)) * (self.matrix['row1'][1] * self.matrix['row3'][2] - self.matrix['row1'][2] * self.matrix['row3'][1])
            c22 = ((-1)**(2+2)) * (self.matrix['row1'][0] * self.matrix['row3'][2] - self.matrix['row1'][2] * self.matrix['row3'][0])
            c23 = ((-1)**(2+3)) * (self.matrix['row1'][0] * self.matrix['row3'][1] - self.matrix['row1'][1] * self.matrix['row3'][0])

            c31 = ((-1)**(3+1)) * (self.matrix['row1'][1] * self.matrix['row2'][2] - self.matrix['row1'][2] * self.matrix['row2'][1])
            c32 = ((-1)**(3+2)) * (self.matrix['row1'][0] * self.matrix['row2'][2] - self.matrix['row1'][2] * self.matrix['row2'][0])
            c33 = ((-1)**(3+3)) * (self.matrix['row1'][0] * self.matrix['row2'][1] - self.matrix['row1'][1] * self.matrix['row2'][0])

            for r in range(1,4):
                for i in range(0,3):
                    self.matrix[f'row{r}'][i] = frac(locals()[f'c{r}{i+1}'])
                    # use locals()[f'c{r}{i+1}'] to iterate variables
            self.matrix = self.transpose()
            for r in range(1,4):
                for i in range(3):
                    self.matrix[f'row{r}'][i] = self.matrix[f'row{r}'][i] / deter
            return self.matrix

        else:
            sys.exit('Only support 1 x 1, 2 x 2, and 3 x 3 matrix')


    def basic_cal(self, choice, num):
        for r in range(len(self.matrix)):
            for e in range(len(self.matrix[f'row{r+1}'])):
                if choice == 1:
                    self.matrix[f'row{r+1}'][e] = frac(self.matrix[f'row{r+1}'][e]) * frac(num)

                elif choice == 2:
                    self.matrix[f'row{r+1}'][e] = frac(self.matrix[f'row{r+1}'][e]) / frac(num)
        return self.matrix


    def __add__(self, other):
        out_matrix = {}
        if len(self.matrix) == len(other.matrix) and len(self.matrix['row1']) == len(other.matrix['row1']):
            for i in range(len(self.matrix)):
                list1 = self.matrix[f'row{i+1}']
                list2 = other.matrix[f'row{i+1}']
                out_matrix[f'row{i+1}'] = [x+y for x,y in zip(list1, list2)]

        else:
            print('')
            sys.exit("Size don't match")
        return out_matrix


    def __sub__(self, other):
        out_matrix = {}
        if len(self.matrix) == len(other.matrix) and len(self.matrix['row1']) == len(other.matrix['row1']):
            for i in range(len(self.matrix)):
                list1 = self.matrix[f'row{i+1}']
                list2 = other.matrix[f'row{i+1}']
                out_matrix[f'row{i+1}'] = [x-y for x,y in zip(list1, list2)]

        else:
            print('')
            sys.exit("Size don't match")
        return out_matrix


    def __mul__(self, other):
        out_matrix = {}
        if len(self.matrix['row1']) == len(other.matrix):
            for r in range(len(self.matrix)):
                row = []
                for c in range(len(other.matrix['row1'])):
                    target_row_array = np.array(self.matrix[f'row{r+1}'])
                    target_column_array = np.array(other.column(c+1))
                    entry = np.multiply(target_row_array, target_column_array)
                    input = sum(entry)
                    row.append(input)
                out_matrix[f'row{r+1}'] = row

        else:
            print('')
            sys.exit("Size don't match")
        return out_matrix


if __name__ == '__main__':
    main()
