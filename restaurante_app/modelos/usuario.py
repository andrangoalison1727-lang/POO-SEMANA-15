class Usuario:
    def __init__(self, identificacion: str, nombre: str, email: str, usuario: str, contrasena: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.email = email
        self.usuario = usuario
        self.contrasena = contrasena

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La identificacion no puede estar vacia.")
        self._identificacion = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacio.")
        self._nombre = valor.strip()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El email no puede estar vacio.")
        self._email = valor.strip()

    @property
    def usuario(self) -> str:
        return self._usuario

    @usuario.setter
    def usuario(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El usuario no puede estar vacio.")
        self._usuario = valor.strip()

    @property
    def contrasena(self) -> str:
        return self._contrasena

    @contrasena.setter
    def contrasena(self, valor: str) -> None:
        if not valor:
            raise ValueError("La contrasena no puede estar vacia.")
        self._contrasena = valor

    def __str__(self) -> str:
        return f"Usuario: {self.nombre}, Identificacion: {self.identificacion}, Email: {self.email}"