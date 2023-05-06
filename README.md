# Sudoku-AI
Solving the sudoku game as a CSP and heuristics like MRV and AC-3 and LCV

An example:
```
python main.py
```
entering the input, n(size of grid), c (number of known values) and c lines each contain i, j, value:
```
9 
34
1 2 2
1 3 6
1 7 8
1 8 1
2 1 3
2 4 7
2 6 8
2 9 6
3 1 4
3 5 5
3 9 7
4 2 5
4 4 1
4 6 7
4 8 9
5 3 3
5 4 9
5 6 5
5 7 1
6 2 4
6 4 3
6 6 2
6 8 5
7 1 1
7 5 3
7 9 2
8 1 5
8 4 2
8 6 4
8 9 9
9 2 3
9 3 8
9 7 4
9 8 6
```
output:
```
Elapsed time: 0.035 seconds
Solution:
7 2 6 4 9 3 8 1 5 
3 1 5 7 2 8 9 4 6 
4 8 9 6 5 1 2 3 7 
8 5 2 1 4 7 6 9 3 
6 7 3 9 8 5 1 2 4 
9 4 1 3 6 2 7 5 8 
1 9 4 8 3 6 5 7 2 
5 6 7 2 1 4 3 8 9 
2 3 8 5 7 9 4 6 1 
```
