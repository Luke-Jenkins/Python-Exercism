class Matrix:
    def __init__(self, matrix_string):
        # class variables
        self.rows = []
        self.columns = []

        # split the input into arrays of rows
        self.input = matrix_string.splitlines()

        # convert arrays of rows from str to int
        for row in self.input:
            row = row.split()
            row = [int(i) for i in row]
            self.rows.append(row)

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        for row in self.rows:
            self.columns.append(row[index - 1])

        return self.columns
