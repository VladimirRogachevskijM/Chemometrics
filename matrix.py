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
        self.__deta = new_data

    @staticmethod
    def row_num(data):
        """Return Int"""
        return int(len(data))
    
    @staticmethod
    def column_num(data):
        """Return Int"""
        column_num = data[0]
        for i in data:
            if len(i) != column_num:
                raise ValueError("Matrix deed to consist same lenght rows")

        return int(len(data[0]))

    def sum(self, other):
        """Calculete sum of two matrix and return object Matrix"""
        new_data = []
        for i in range(len(self.__data)):
            row = []
            for j in range(len(self.__data[i])):
                row.append(self.__data(j)+other.__data(j))
            new_data.append(row)       
        return Matrix(new_data)
   