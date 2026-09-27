# Restaurante App

**Estudiante:** Alison Dayana Andrango Nieto

Aplicación gráfica desarrollada en Python con Tkinter como parte de la asignatura Programación Orientada a Objetos. El proyecto se ha desarrollado progresivamente durante las semanas anteriores, manteniendo una organización modular y el uso de archivos JSON para conservar la información.

## Semana 15

La Semana 15 aborda los **conceptos fundamentales de manejo de eventos**. A partir del proyecto desarrollado anteriormente, se incorporó una sección de **Ventas** para aplicar el flujo de una acción realizada por el usuario, un botón con `command=`, un callback y la delegación de la operación al servicio correspondiente.

La nueva funcionalidad permite relacionar un usuario registrado con un producto registrado y guardar la venta realizada.

Se conservaron las funcionalidades desarrolladas en las semanas anteriores, incluyendo el inicio de sesión, la navegación, la consulta de usuarios y la gestión de productos.

## Evolución del proyecto

La Semana 15 parte de la versión existente de `restaurante_app` y mantiene su estructura modular.

Se incorporaron los siguientes elementos:

* Modelo `Venta`.
* Archivo `datos/ventas.json`.
* Sección **Ventas** dentro de la interfaz principal.
* Selección de usuarios mediante `Combobox`.
* Selección de productos mediante `Combobox`.
* Botón **Registrar venta**.
* Callback para procesar el registro de la venta.
* Métodos en `RestauranteServicio` para validar, registrar y guardar las ventas.
* Tabla `Treeview` para mostrar las ventas registradas.
* Actualización de la tabla después de registrar una venta.
* Íconos y logotipo integrados mediante la carpeta `assets`.

## Gestión de ventas

La venta relaciona un usuario existente con un producto existente y registra la fecha de la operación.

Cada venta contiene:

* Identificador.
* Identificación del usuario.
* Código del producto.
* Fecha.

Las ventas se guardan en:

```text
datos/ventas.json
```

El registro de una venta se realiza mediante `RestauranteServicio`, donde se verifica que el usuario y el producto seleccionados existan antes de guardar la operación.

## Manejo de eventos

La sección de Ventas permite aplicar el flujo de eventos trabajado en la Semana 15:

**Acción del usuario → botón → `command=` → callback → `RestauranteServicio` → persistencia → actualización de la interfaz**

El botón **Registrar venta** utiliza `command=` para asociar la acción con el callback correspondiente.

El callback obtiene las selecciones realizadas en la interfaz y solicita a `RestauranteServicio` que registre la venta. El servicio se encarga de las validaciones, la creación de la venta y la persistencia en `ventas.json`.

Después del registro, la interfaz actualiza la tabla de ventas y muestra el resultado de la operación al usuario.

La interfaz no realiza directamente la lectura o escritura de `ventas.json`.

## Persistencia

La aplicación utiliza archivos JSON para conservar la información:

```text
datos/
├── productos.json
├── usuarios.json
└── ventas.json
```

`ArchivoServicio` se utiliza para la lectura y escritura de los archivos JSON.

`RestauranteServicio` utiliza este servicio para guardar los productos y las ventas.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│   ├── logo.png
│   ├── home.png
│   ├── products.png
│   ├── users.png
│   ├── sell.png
│   ├── logout.png
│   ├── add.png
│   ├── search.png
│   ├── edit.png
│   ├── delete.png
│   └── clean.png
│
└── main.py
```

## Interfaz

La interfaz está desarrollada con Tkinter y ttk.

La aplicación mantiene una barra lateral para navegar entre las secciones de **Inicio, Productos, Usuarios y Ventas**, además de la opción para cerrar sesión.

En la sección de Ventas se utilizan `Combobox` para seleccionar un usuario y un producto, un botón para registrar la venta y un `Treeview` para mostrar las ventas registradas.

La carpeta `assets/` contiene los recursos visuales utilizados en la aplicación, incluyendo el logotipo y los íconos de las diferentes secciones y acciones.

## Ejecución

Para ejecutar la aplicación se necesita tener Python instalado.

Desde la carpeta `restaurante_app` ejecutar:

```bash
python main.py
```

La aplicación inicia mostrando la pantalla de inicio de sesión. Después de ingresar con un usuario registrado, se puede acceder a las diferentes secciones de la aplicación.

## Comprobación de la funcionalidad de ventas

Para comprobar la nueva funcionalidad:

1. Ejecutar `main.py`.
2. Iniciar sesión con un usuario registrado.
3. Ingresar a la sección **Ventas**.
4. Seleccionar un usuario.
5. Seleccionar un producto.
6. Presionar **Registrar venta**.
7. Verificar que la nueva venta aparezca en la tabla.
8. Verificar que la información se haya guardado en `datos/ventas.json`.
9. Cerrar y volver a ejecutar la aplicación para comprobar que la venta guardada se cargue nuevamente.

## Conclusión

La Semana 15 permitió continuar el desarrollo de `restaurante_app` incorporando una sección de Ventas y aplicando los conceptos básicos de manejo de eventos. Mediante el uso de `command=` y callbacks, la interfaz puede iniciar una operación y delegarla a `RestauranteServicio`, donde se realizan las validaciones y se guarda la información en `ventas.json`.

Con esta implementación se mantiene la estructura modular desarrollada en las semanas anteriores y se continúa ampliando el sistema de manera progresiva, relacionando usuarios y productos mediante el registro de ventas.
