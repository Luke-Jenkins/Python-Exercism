class Matrix:
    def __init__(self, matrix_string):
        # variables
        self.rows = []
        self.columns = []
        # constant
        self.row_count = matrix_string.count('\n') + 1

        # split the input into arrays of rows
        self.input = matrix_string.split('\n')

        # convert arrays of rows from str to int
        for i in range(self.row_count):
            self.rows.append(self.input[i].split(' '))
            self.rows[i] = [int(j) for j in self.rows[i]]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        for i in range(len(self.rows)):
            self.columns.append(self.rows[i][index - 1])

        return self.columns
