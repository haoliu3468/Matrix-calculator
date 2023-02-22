# Matrix-calculator
#### Video Demo: <https://youtu.be/jvI8rtPwKkI>
## Features
"Matrix calculator" has eight main functions:
1. Find the row echelom form of the matrix (any size)
2. Find the reduced row echelom form of the matrix (any size)
3. Find the determinant of the square matrix (1x1, 2x2, and 3x3)
4. Find the transpose of the matrix (any size)
5. Find the inverse of the square matrix (1x1, 2x2, and 3x3)
6. Basic calculation:
   1. Single matrix multiplication (any size)
   2. Single matrix division (any size)
7. Two matrices calculation:
   1. Two matrices multiplication
   2. Two matrices addition
   3. Two matrices subtraction


## Input types
"Matrix calculator" support three types of input:

- Integer: '1', '-3', '0', '05', '-07', '82', '137', etc.
- Decimal: '1.3', '-2.1', '0.0', '02.3', '7.10', etc.
- Fraction: '2/3', '-4/5' ,'0/0', '02/03', etc.

The "Matrix caculator" presents 'row: ' to ask for the row input.

The expected input is:

'(integer/decimal/fraction),(integer/decimal/fraction),(integer/decimal/fraction),...'

### Examples:
```python
> row1: 1,2,3
> row2: 1.4,1.5,1.6
> row3: 2/3,-2/3,0
> row4: 1,1.2,13/10
```

## Input rules
If the input violates any of the three rules, the input would be rejected, and the program would ask for the same row again.

### Rule 1
Must use and only use ',' to seperate different columns in the same row.

Examples of violation of the first rule:
```python
> row1: 1, 2, 3

# row1:
```
```python
> row1: 1.2.3

# row1:
```
```python
> row1: 1;2;3

# row1:
```
```python
> row1: 1 2 3

# row1:
```

### Rule 2
Cannot enter not supported input type after any ',', leave nothing before any ',', or leave nothing after any ','.

Examples of violation of the second rule:
```python
> row1: 1,string,3

# row1:
```
```python
> row1: 1, ,3

# row1:
```
```python
> row1: 1,2,

# row1:
```
```python
> row1:  ,2,3

# row1:
```

### Rule 3
Row sizes must match with each other.

Examples of violation of the third rule:
```python
> row1: 1,2,3
> row2: 4,5

# row2:
```
```python
> row1: 1,2,3
> row2: 4,5,6,7

# row2:
```

## End matrix input
Press 'enter' after any prompt to end entering and store the matrix.
```python
> row1: 1,2,3
> row2: 'press enter'

# Stored matrix: {'row1': [Fraction(1,1), Fraction(2,1), Fraction(3,1)]}
```
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 'press enter'

# Stored matrix: {'row1': [Fraction(1,1), Fraction(2,1), Fraction(3,1)], 'row2': [Fraction(4,1), Fraction(5,1), Fraction(6,1)]}
```


## Functions
After ending the matrix entering, the program would ask users for the matrix operations. There are seven main functions and one exit option. Users could access any function by entering the corresponding leading number. If users enter 6 or 7, the program would lead users to a sub-menu which provide more sepcific available matrix operations.

1. Find the row echelom form of the matrix (any size)
2. Find the reduced row echelom form of the matrix (any size)
3. Find the determinant of the square matrix (1x1, 2x2, and 3x3)
4. Find the transpose of the matrix (any size)
5. Find the inverse of the square matrix (1x1, 2x2, and 3x3)
6. Basic calculation:
   1. Single matrix multiplication (any size)
   2. Single matrix division (any size)
7. Two matrices calculation:
   1. Two matrices multiplication
   2. Two matrices addition
   3. Two matrices subtraction
8. Exit and print the matrix


### Row echelom form
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> 1

# [1 2 3]
# [0 1 2]
# [0 0 0]
```
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> 1

# [1 2 3 4]
# [0 1 2 3]
# [0 0 0 0]
```
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> row4: 10,11,12
> 1

# [1 2 3]
# [0 1 2]
# [0 0 0]
# [0 0 0]
```



### Reduced row echelom form
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> 2

# [1 0 -1]
# [0 1 2]
# [0 0 0]
```
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> 2

# [1 0 -1 -2]
# [0 1 2 3]
# [0 0 0 0]
```
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> row4: 10,11,12
> 2

# [1 0 -1]
# [0 1 2]
# [0 0 0]
# [0 0 0]
```



### Determinant
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> 3

# Determinant: 0
```
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> 3

# Only support 1 x 1, 2 x 2, and 3 x 3 square matrix
```
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> row4: 10,11,12
> 3

# Only support 1 x 1, 2 x 2, and 3 x 3 square matrix
```
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> row4: 13,14,15,16
> 3

# Only support 1 x 1, 2 x 2, and 3 x 3 square matrix
```


### Transpose
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> 4

# [1 4 7]
# [2 5 8]
# [3 6 9]
```
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> 4

# [1 5 9]
# [2 6 10]
# [3 7 11]
# [4 8 12]
```
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> row4: 10,11,12
> 4

# [1 4 7 10]
# [2 5 8 11]
# [3 6 9 12]
```


### Inverse
```python
> row1: 1,3
> row2: 2,4
> 5

# [-2 3/2]
# [1 -1/2]
```
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> 5

# This is a non-invertible matrix
```
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> 5

# Only support 1 x 1, 2 x 2, and 3 x 3 square matrix
```
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> row4: 10,11,12
> 5

# Only support 1 x 1, 2 x 2, and 3 x 3 square matrix
```
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> row4: 13,14,15,16
> 5

# Only support 1 x 1, 2 x 2, and 3 x 3 square matrix
```


### Basic calculation
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> 6
```
#### Multiplication
```python
> 1
> By: 2

# [2 4 6]
# [8 10 12]
# [14 16 18]
```

#### Division
```python
> 2
> By: 2

# [1/2 1 3/2]
# [2 5/2 3]
# [7/2 4 9/2]
```


### Two matrices calculation
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> 7

# Size don't match
```
#### Two matrices multiplication
```python
> row1: 1,2,3
> row2: 4,5,6
> row3: 7,8,9
> row4: 10,11,12
> 1

# [70 80 90]
# [158 184 210]
# [246 288 330]
```

#### Two matrices addition
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> 2

# [2 4 6 8]
# [10 12 14 16]
# [18 20 22 24]
```
#### Two matrices subtraction
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> 3

# [0 0 0 0]
# [0 0 0 0]
# [0 0 0 0]
```

### Exit and print the matrix
```python
> row1: 1,2,3,4
> row2: 5,6,7,8
> row3: 9,10,11,12
> 8

# [1 2 3 4]
# [5 6 7 8]
# [9 10 11 12]
```


## Use methods in class 'Method'

Beside running the 'Matrix calculator.py' program, you could also use instance methods in the class 'Method' included in the program.

prerequesite packages:

- Fraction: <https://pypi.org/project/Fraction/>
- numpy: <https://pypi.org/project/numpy/>

To use methods in the 'Matrix' class:

Use 'Matrix(get_matrix())' to get a matrix belongs to the 'Matrix' class

```python
> matrix = Matrix(get_matrix())
```
## .ref()
```python
> row_echelom = matrix.ref()
> print_matrix(row_echelom)
```
## .rref()
```python
> reduced_row_echelom = matrix.rref()
> print_matrix(reducd_row_echelom)
```
## .det()
```python
> determinant = matrix.det()
> print(determinant)
```
## .transpose()
```python
> transpose = matrix.transpose()
> print_matrix(transpose)
```
## .inverse()
```python
> inverse = matrix.inverse()
> print_matrix(inverse)
```
## .basic_cal()
```python
> basic_cal = matrix.basic_cal(1, 2)
# multiply by 2
> print_matrix(basic_cal)
```
```python
> basic_cal = matrix.basic_cal(2, 2)
# devide by 2
> print_matrix(basic_cal)
```
## add new matrix
```python
> matrix2 = Matrix(get_matrix())
```
```python
> add = matrix + matrix2
> print_matrix(add)
```
```python
> subtract = matrix - matrix2
> print_matrix(subtract)
```
```python
> multiply = matrix * matrix2
> print_matrix(multiply)
```



