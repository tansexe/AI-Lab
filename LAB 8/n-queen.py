def placeQueens(i, cols, leftDiagonal, rightDiagonal, cur):
    n = len(cols)

    # base case: If all queens are placed then return true
    if i == n:
        return True

    # Consider the row and try placing queen in all columns one by one
    for j in range(n):

        # Check if the queen can be placed
        if cols[j] or rightDiagonal[i + j] or leftDiagonal[i - j + n - 1]:
            continue

        # mark the cell occupied
        cols[j] = 1
        rightDiagonal[i + j] = 1
        leftDiagonal[i - j + n - 1] = 1
        cur.append(j + 1)

        if placeQueens(i + 1, cols, leftDiagonal, rightDiagonal, cur):
            return True

        # remove the queen from current cell
        cur.pop()
        cols[j] = 0
        rightDiagonal[i + j] = 0
        leftDiagonal[i - j + n - 1] = 0

    return False

# Function to find the solution to the N-Queens problem
def nQueen(n):
  
    # array to mark the occupied cells
    cols = [0] * n
    leftDiagonal = [0] * (n * 2)
    rightDiagonal = [0] * (n * 2)
    cur = []

    # If the solution exists
    if placeQueens(0, cols, leftDiagonal, rightDiagonal, cur):
        return cur
    else:
        return [-1]

if __name__ == "__main__":
    n = int(input())
    ans = nQueen(n)
    print(" ".join(map(str, ans)))
