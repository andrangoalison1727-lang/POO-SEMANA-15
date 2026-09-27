class Producto:
    def __init__(self, nombre: str, codigo: str, precio: float, categoria: str, stock: int) -> None:
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, value: str) -> None:
        if not value:
            raise ValueError("El código no puede estar vacío.")
        self._codigo = value

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, value: float) -> None:
        if value <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = value

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, value: str) -> None:
        if not value:
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = value

    def __str__(self) -> str:
        return (
            f"Producto: {self.nombre}, Código: {self.codigo}, "
            f"Precio: ${self.precio:.2f}, Categoría: {self.categoria}, "
            f"Stock: {self.stock}"
        )

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        try:
            stock = int(value)
        except (TypeError, ValueError):
            raise ValueError("El stock debe ser un numero entero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = stock

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock disponible.")
        self.stock -= cantidad

    def convertir_a_diccionario(self) -> dict:
        return {
            "nombre": self.nombre,
            "codigo": self.codigo,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock
        }