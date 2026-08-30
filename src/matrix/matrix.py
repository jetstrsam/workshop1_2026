class Matrix:
    """
    Clase con métodos para operaciones sobre matrices.
    Incluye operaciones aritméticas, propiedades y transformaciones matriciales.
    """

    def suma_matrices(self, A, B):
        """
        Suma dos matrices elemento a elemento.

        Args:
            A (list): Primera matriz (lista de listas)
            B (list): Segunda matriz (lista de listas), debe tener las mismas dimensiones que A

        Returns:
            list: Matriz resultante de la suma

        Raises:
            ValueError: Si las matrices tienen dimensiones incompatibles

        Ejemplo:
            suma_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) -> [[6, 8], [10, 12]]
        """

        if len(A) != len(B):
            raise ValueError("Las matrices tienen dimensiones incompatibles")

        if not A and not B:
            return []

        filas = len(A)
        cols = len(A[0])

        for i in range(filas):
            if len(A[i]) != cols or len(B[i]) != cols:
                raise ValueError("Las matrices tienen dimensiones incompatibles")

        resultado = []
        for i in range(filas):
            fila_suma = [A[i][j] + B[i][j] for j in range(cols)]
            resultado.append(fila_suma)

        return resultado

    def resta_matrices(self, A, B):
        """
        Resta dos matrices elemento a elemento (A - B).

        Args:
            A (list): Primera matriz (lista de listas)
            B (list): Segunda matriz (lista de listas), debe tener las mismas dimensiones que A

        Returns:
            list: Matriz resultante de la resta

        Raises:
            ValueError: Si las matrices tienen dimensiones incompatibles

        Ejemplo:
            resta_matrices([[5, 6], [7, 8]], [[1, 2], [3, 4]]) -> [[4, 4], [4, 4]]
        """

        if len(A) != len(B):
            raise ValueError("Las matrices tienen dimensiones incompatibles")

        if not A and not B:
            return []

        filas = len(A)
        cols = len(A[0])

        for i in range(filas):
            if len(A[i]) != cols or len(B[i]) != cols:
                raise ValueError("Las matrices tienen dimensiones incompatibles")

        resultado = []
        for i in range(filas):
            fila_resta = [A[i][j] - B[i][j] for j in range(cols)]
            resultado.append(fila_resta)

        return resultado

    def multiplicar_matrices(self, A, B):
        """
        Multiplica dos matrices usando la multiplicación matricial estándar.
        El número de columnas de A debe ser igual al número de filas de B.

        Args:
            A (list): Primera matriz de dimensiones m x n
            B (list): Segunda matriz de dimensiones n x p

        Returns:
            list: Matriz resultante de dimensiones m x p

        Raises:
            ValueError: Si las dimensiones son incompatibles para multiplicación

        Ejemplo:
            multiplicar_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) -> [[19, 22], [43, 50]]
        """
        if not A or not B or not A[0] or not B[0]:
            raise ValueError("Las matrices no pueden estar vacías")

        columnas_A = len(A[0])
        filas_B = len(B)

        if any(len(fila) != columnas_A for fila in A) or any(len(fila) != len(B[0]) for fila in B):
            raise ValueError("Las dimensiones son incompatibles para multiplicación")

        if columnas_A != filas_B:
            raise ValueError("El número de columnas de A debe ser igual al número de filas de B")

        filas_A = len(A)
        columnas_B = len(B[0])

        resultado = []
        for i in range(filas_A):
            fila_resultado = []
            for j in range(columnas_B):
                suma = sum(A[i][k] * B[k][j] for k in range(columnas_A))
                fila_resultado.append(suma)
            resultado.append(fila_resultado)

        return resultado

    def multiplicar_escalar(self, matriz, escalar):
        """
        Multiplica cada elemento de la matriz por un escalar.

        Args:
            matriz (list): Matriz (lista de listas)
            escalar (number): Valor escalar por el que se multiplica

        Returns:
            list: Matriz con cada elemento multiplicado por el escalar

        Ejemplo:
            multiplicar_escalar([[1, 2], [3, 4]], 3) -> [[3, 6], [9, 12]]
        """
        mult_esc = [[val * escalar for val in fila] for fila in matriz]
        return mult_esc

    def transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz (intercambia filas por columnas).

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            list: Matriz transpuesta

        Ejemplo:
            transpuesta([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
        """
        if not matriz:
            return[]

        transpuesta = []
        for j in range(len(matriz[0])):
            fila = []
            for i in range(len(matriz)):
                fila.append(matriz[i][j])
            resultado.append(fila)
        return transpuesta


    def es_cuadrada(self, matriz):
        """
        Verifica si una matriz es cuadrada (mismo número de filas y columnas).

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            bool: True si la matriz es cuadrada, False en caso contrario

        Ejemplo:
            es_cuadrada([[1, 2], [3, 4]]) -> True
            es_cuadrada([[1, 2, 3], [4, 5, 6]]) -> False
        """
        if not matriz:
            return False

        cantidad_filas= len(matriz)

        for fila  in matriz:
            if len(fila != cantidad=filas):
                return False

        return True

    def es_simetrica(self, matriz):
        """
        Verifica si una matriz es simétrica (igual a su transpuesta).
        Solo aplica a matrices cuadradas.

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            bool: True si la matriz es simétrica, False en caso contrario

        Ejemplo:
            es_simetrica([[1, 2, 3], [2, 5, 6], [3, 6, 9]]) -> True
            es_simetrica([[1, 2], [3, 4]]) -> False
        """
        if not self.es_cuadradada(matriz):
            return False

        return matriz == self.transpuesta(matriz)

    def traza(self, matriz):
        """
        Calcula la traza de una matriz cuadrada (suma de los elementos de la diagonal principal).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            number: La suma de los elementos de la diagonal principal

        Raises:
            ValueError: Si la matriz no es cuadrada

        Ejemplo:
            traza([[1, 2], [3, 4]]) -> 5
            traza([[1, 0, 0], [0, 5, 0], [0, 0, 9]]) -> 15
        """
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada para calcular la traza.")

        return sum(matriz[i][j] for i in range(len(matriz)))

    def determinante_2x2(self, matriz):
        """
        Calcula el determinante de una matriz 2x2.
        det([[a, b], [c, d]]) = a*d - b*c

        Args:
            matriz (list): Matriz 2x2 (lista de listas)

        Returns:
            number: El determinante de la matriz

        Raises:
            ValueError: Si la matriz no es 2x2

        Ejemplo:
            determinante_2x2([[3, 8], [4, 6]]) -> -14
            determinante_2x2([[1, 2], [3, 4]]) -> -2
        """
        if not matriz or len(matriz) != 2:
            raise ValueError("La matriz debe ser de dimensión 2x2.")

        if len(matriz[0]) != 2 or len(matriz[1]) != 2:
            raise ValueError("La matriz debe ser de dimensión 2x2.")

        a, b = matriz[0][0], matriz[0][1]
        c, d = matriz[1][0], matriz[1][1]

        return a * d - b * c

    def determinante_3x3(self, matriz):
        """
        Calcula el determinante de una matriz 3x3 usando la regla de Sarrus.

        Args:
            matriz (list): Matriz 3x3 (lista de listas)

        Returns:
            number: El determinante de la matriz

        Raises:
            ValueError: Si la matriz no es 3x3

        Ejemplo:
            determinante_3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> 0
            determinante_3x3([[1, 0, 0], [0, 2, 0], [0, 0, 3]]) -> 6
        """
        if not matriz or len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            raise ValueError("La matriz debe ser de dimensión 3x3.")

        m = matriz
    
        d1 = m[0][0] * m[1][1] * m[2][2]
        d2 = m[0][1] * m[1][2] * m[2][0]
        d3 = m[0][2] * m[1][0] * m[2][1]
    
        d4 = m[0][2] * m[1][1] * m[2][0]
        d5 = m[0][0] * m[1][2] * m[2][1]
        d6 = m[0][1] * m[1][0] * m[2][2]

        return (d1 + d2 + d3) - (d4 + d5 + d6)

    def identidad(self, n):
        """
        Genera una matriz identidad de tamaño n x n.
        La diagonal principal tiene 1s y el resto 0s.

        Args:
            n (int): Tamaño de la matriz identidad

        Returns:
            list: Matriz identidad n x n

        Ejemplo:
            identidad(2) -> [[1, 0], [0, 1]]
            identidad(3) -> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        """

        matriz = []
        for i in range(n):
            fila = []
            for j in range(n):
                if i == j:
                    fila.append(1)
                else:
                    fila.append(0)
            matriz.append(fila)
        
        return matriz

    def diagonal(self, matriz):
        """
        Extrae los elementos de la diagonal principal de una matriz cuadrada.

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            list: Lista con los elementos de la diagonal principal

        Raises:
            ValueError: Si la matriz no es cuadrada

        Ejemplo:
            diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 5, 9]
            diagonal([[3, 0], [0, 7]]) -> [3, 7]
        """
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada.")

        return [matriz[i][i] for i in range(len(matriz))]

    def es_diagonal(self, matriz):
        """
        Verifica si una matriz cuadrada es diagonal
        (todos los elementos fuera de la diagonal principal son cero).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            bool: True si la matriz es diagonal, False en caso contrario

        Ejemplo:
            es_diagonal([[3, 0], [0, 7]]) -> True
            es_diagonal([[1, 2], [0, 4]]) -> False
        """
        if not self.es_cuadrada(matriz):
            return False

        n = len(matriz)
        return all(
            matriz[i][j] == 0
            for i in range(n)
            for j in range(n)
            if i != j
        )

    def rotar_90(self, matriz):
        """
        Rota una matriz 90 grados en sentido horario.

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            list: Matriz rotada 90 grados en sentido horario

        Ejemplo:
            rotar_90([[1, 2], [3, 4]]) -> [[3, 1], [4, 2]]
            rotar_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        """
        return [list(fila) for fila in zip(*matriz[::-1])]

    def buscar_en_matriz(self, matriz, valor):
        """
        Busca un valor en la matriz y retorna todas las posiciones donde se encuentra.

        Args:
            matriz (list): Matriz (lista de listas)
            valor: Valor a buscar en la matriz

        Returns:
            list: Lista de tuplas (fila, columna) con las posiciones del valor.
                  Retorna lista vacía si no se encuentra.

        Ejemplo:
            buscar_en_matriz([[1, 2, 3], [4, 2, 6], [7, 8, 2]], 2) -> [(0, 1), (1, 1), (2, 2)]
            buscar_en_matriz([[1, 2], [3, 4]], 9) -> []
        """

        for f in range(len(matriz)):
            for c in range(len(matriz[f])):
                if matriz[f][c] == valor:
                    posiciones.append((f, c))
                
        return posiciones
