class Matrix:
    def __init__(self, data):
        self.__data = data
        self.__row_num = Matrix.row_num(data)
        self.__column_num = Matrix.column_num(data)

    @property
    def data(self):
        """Return two-dimencional massive"""
        return self.__data

    @data.setter
    def data(self, new_data):
        """Set data and return None"""
        self.__data = new_data

    @staticmethod
    def row_num(data):
        """Return Int"""
        return int(len(data))
    
    @staticmethod
    def column_num(data):
        """Return Int"""
        if isinstance(data[0], int) or isinstance(data[0], float):
            column_num = 1
            for i in data:
                if not isinstance(i, int) and not isinstance(i, float):
                    raise ValueError("Matrix need to consist same lenght rows")
        else:
            column_num = len(data[0])
            for i in data:
                if len(i) != column_num:
                    raise ValueError("Matrix need to consist same lenght rows")

        return column_num

    def transponing(self):
        """Calculate transponse matrix and return object Matrix"""
        new_data = []
        for i in range(self.__column_num):
            new_row = []
            for j in range(self.__row_num):
                new_row.append(self.__data[j][i])
            new_data.append(new_row)
        Transponse = Matrix(new_data)
        return Transponse               

    def sum(self, other):
        """Calculate sum of two matrix and return object Matrix"""
        new_data = []
        for i in range(len(self.__data)):
            row = []
            for j in range(len(self.__data[i])):
                row.append(self.__data(j)+other.__data(j))
            new_data.append(row)       
        return Matrix(new_data)
    
    def multiply(self, other):
        """Multiply two matrix and return object Matrix"""
        new_data = []
        for i in range(self.__row_num):
            new_data.append([])
            for j in range(self.__column_num):
                new_data[i].append([])
                sum = 0
                for k in range(self.__row_num):
                    sum += self.__data[i][j]*other.__data[j][i]
                new_data[i][j] = sum
        return Matrix(new_data)
    
    @staticmethod
    def determinant(data):
        """Calculate determinant and return float"""
        if len(data) != len(data[0]):
            raise ValueError(f"Unbeliveble to found deskriminant. Number of rows not equal number of columns, num of rows = {len(data)}, num of columns = {len(data[0])}")

        PF = 0
        determinant = 0
        if len(data) == 1:
            determinant = data[0][0]
        else:
            for i in range(len(data[0])):
                new_data = []
                for j in range(1, len(data)):
                    new_data.append([])
                    for k in range(len(data[0])):
                        if k != i:
                            new_data[j-1].append(data[j][k])
                if PF%2 == 0:
                    determinant += Matrix.determinant(new_data)*data[0][i]
                else:
                    determinant -= Matrix.determinant(new_data)*data[0][i]

                PF += 1
        return determinant
    
    @staticmethod
    def reverse(data):
        """Calculate reversed matrix and return object Matrix"""
        det = Matrix.determinant(data)
        for i in data:
            for j in i:
                j /= det
        Reversed = Matrix(data).transponing
        return Reversed