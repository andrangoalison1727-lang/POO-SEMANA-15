import tkinter as tk
from tkinter import messagebox, ttk
from pathlib import Path

class MainView(tk.Frame):

    def __init__(self, master, restaurante_servicio, usuario_actual, al_cerrar_sesion):
        super().__init__(master, bg="#fff8f0")

        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion

        self.contenido = None
        self.etiqueta_estado = None
        self.botones_menu = []
        self.iconos = {}
        self.logo_sidebar = None

        self.producto_nombre_entry = None
        self.producto_codigo_entry = None
        self.producto_precio_entry = None
        self.producto_categoria_entry = None
        self.producto_stock_entry = None
        self.tabla_productos = None
        self.usuario_venta_combo = None
        self.producto_venta_combo = None
        self.tabla_ventas = None
        self.opciones_usuarios_venta = {}
        self.opciones_productos_venta = {}
    

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        self.color_fondo = "#FFF8F0"
        self.color_encabezado = "#4A3426"
        self.color_texto = "#4A3426"
        self.color_secundario = "#F3E5C8"
        self.color_resaltado = "#C9A227"

        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "MenuApp.TButton",
            background="#C9A227",
            foreground="#FFFFFF",
            font=("Arial", 10, "bold"),
            padding=(12, 8),
            borderwidth=0,
            anchor="w",
        )

        estilo.map(
            "MenuApp.TButton",
            background=[("active", "#A8841E")],
        )

        estilo.configure(
            "CerrarSesion.TButton",
            background="#9A5B3A",
            foreground="#FFFFFF",
            font=("Arial", 10, "bold"),
            padding=(12, 8),
            borderwidth=0,
            anchor="w",
        )

        estilo.map(
            "CerrarSesion.TButton",
            background=[("active", "#7D472F")],
        )

        estilo.configure(
            "MenuActivo.TButton",
            background=self.color_resaltado,
            foreground="#FFFFFF",
            font=("Arial", 10, "bold"),
            padding=(12, 10),
            borderwidth=0,
            anchor="w",
        )

        estilo.map(
            "MenuActivo.TButton",
            background=[("active", "#A8841E")],
        )

        estilo.configure(
            "Accion.TButton",
            background=self.color_resaltado,
            foreground="#FFFFFF",
            font=("Arial", 10, "bold"),
            padding=(10, 7),
            borderwidth=0,
        )

        estilo.map(
            "Accion.TButton",
            background=[("active", "#A8841E")],
        )
        estilo.configure(
            "Secundaria.TButton",
            background="#C9A227",
            foreground="#FFFFFF",
            font=("Arial", 10, "bold"),
            padding=(10, 7),
            borderwidth=0,
            anchor="center",
        )

        estilo.map(
            "Secundaria.TButton",
            background=[("active", "#A8841E")],
        )

        estilo.configure(
            "Eliminar.TButton",
            background="#9A5B3A",
            foreground="#FFFFFF",
            font=("Arial", 10, "bold"),
            padding=(10, 7),
            borderwidth=0,
            anchor="center",
        )

        estilo.map(
            "Eliminar.TButton",
            background=[("active", "#7D472F")],
        )

        estilo.configure(
            "Treeview.Heading",
            background=self.color_secundario,
            foreground=self.color_encabezado,
            font=("Arial", 10, "bold"),
        )

    def cargar_icono(self, nombre_archivo):
        ruta_base = Path(__file__).resolve().parent.parent
        ruta_icono = ruta_base / "assets" / nombre_archivo

        if not ruta_icono.exists():
            return None

        imagen = tk.PhotoImage(file=ruta_icono)
        self.iconos[nombre_archivo] = imagen
        return imagen


    def crear_boton(self, contenedor, texto, comando, estilo, icono=None):
        imagen = self.cargar_icono(icono) if icono else None

        if imagen is not None:
            boton = ttk.Button(
                contenedor,
                text=texto,
                command=comando,
                style=estilo,
                image=imagen,
                compound="left",
            )
        else:
            boton = ttk.Button(
                contenedor,
                text=texto,
                command=comando,
                style=estilo,
            )

        return boton

    def construir_interfaz(self):
        frame_sidebar = tk.Frame(
                self,
                bg=self.color_encabezado,
                width=280,
                padx=22,
                pady=24,
            )
        frame_sidebar.pack(side="left", fill="y")
        frame_sidebar.pack_propagate(False)
        
        
        tk.Label(
            frame_sidebar,
            text="RESTAURANTE APP",
            bg=self.color_encabezado,
            fg="#FFFFFF",
            font=("Arial", 17, "bold"),
        ).pack(anchor="w", pady=(0, 8))

        tk.Label(
            frame_sidebar,
            text=f"Bienvenido, {self.usuario_actual.nombre}",
            bg=self.color_encabezado,
            fg="#F3E5C8",
            font=("Arial", 10),
        ).pack(anchor="w", pady=(0, 24))

        self.crear_boton(
            frame_sidebar,
            "Inicio",
            self.mostrar_inicio,
            "MenuApp.TButton",
            "home.png",
        ).pack(fill="x", pady=(0, 8))

        self.crear_boton(
            frame_sidebar,
            "Productos",
            self.mostrar_productos,
            "MenuApp.TButton",
            "products.png",
        ).pack(fill="x", pady=(0, 8))

        self.crear_boton(
            frame_sidebar,
            "Usuarios",
            self.mostrar_usuarios,
            "MenuApp.TButton",
            "users.png",
        ).pack(fill="x", pady=(0, 8))

        self.crear_boton(
            frame_sidebar,
            "Ventas",
            self.mostrar_ventas,
            "MenuApp.TButton",
            "sell.png",
        ).pack(fill="x")

        tk.Frame(
            frame_sidebar,
            bg=self.color_encabezado,
        ).pack(fill="both", expand=True)

        self.crear_boton(
            frame_sidebar,
            "Cerrar sesion",
            self.cerrar_sesion,
            "CerrarSesion.TButton",
            "logout.png",
        ).pack(fill="x", pady=(16, 0))

        frame_principal = tk.Frame(
            self,
            bg=self.color_fondo,
        )
        frame_principal.pack(side="left", fill="both", expand=True)

        self.contenido = tk.Frame(
            frame_principal,
            bg=self.color_fondo,
            padx=28,
            pady=24,
        )
        self.contenido.pack(fill="both", expand=True)

        self.crear_barra_estado()

        self.mostrar_inicio()

    def limpiar_contenido(self):
        assert self.contenido is not None
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_contenido()

        assert self.contenido is not None

        tk.Label(
            self.contenido,
            text="Panel principal",
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 18, "bold"),
        ).pack(anchor="w", pady=(0, 8))

        tk.Label(
            self.contenido,
            text="Seleccione una opcion del menu para visualizar la informacion.",
            bg=self.color_fondo,
            fg=self.color_texto,
            font=("Arial", 12),
        ).pack(anchor="w")

    def mostrar_productos(self):
        self.limpiar_contenido()

        assert self.contenido is not None

        cuerpo = tk.Frame(self.contenido, bg=self.color_fondo)
        cuerpo.pack(fill="both", expand=True)
        cuerpo.grid_columnconfigure(1, weight=1)
        cuerpo.grid_rowconfigure(0, weight=1)

        formulario = tk.LabelFrame(
            cuerpo,
            text="Datos del producto",
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 10, "bold"),
            padx=14,
            pady=14,
        )
        formulario.grid(row=0, column=0, sticky="ns", padx=(0, 18))

        self.producto_codigo_entry = self.crear_campo(formulario, "Codigo", 0)
        self.producto_nombre_entry = self.crear_campo(formulario, "Nombre", 1)
        self.producto_precio_entry = self.crear_campo(formulario, "Precio", 2)
        self.producto_categoria_entry = self.crear_campo(formulario, "Categoria", 3)
        self.producto_stock_entry = self.crear_campo(formulario, "Stock", 4)

        acciones = tk.Frame(formulario, bg=self.color_fondo)
        acciones.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(12, 0))

        botones = (
            ("Registrar", self.registrar_producto, "Accion.TButton", "add.png"),
            ("Cargar por codigo", self.cargar_producto, "Secundaria.TButton", "search.png"),
            ("Actualizar", self.actualizar_producto, "Accion.TButton", "edit.png"),
            ("Eliminar", self.eliminar_producto, "Eliminar.TButton", "delete.png"),
            ("Limpiar", self.limpiar_formulario_producto, "Secundaria.TButton", "clean.png"),
        )
        

        for texto, comando, estilo, icono in botones:
            self.crear_boton(
                acciones,
                texto,
                comando,
                estilo,
                icono,
            ).pack(fill="x", pady=(0, 7))

        listado = self.crear_listado(cuerpo, "Productos registrados")

        self.tabla_productos = self.crear_tabla(
            listado,
            ("codigo", "nombre", "precio", "categoria", "stock"),
            ("Codigo", "Nombre", "Precio", "Categoria", "Stock"),
        )

        self.actualizar_tabla_productos()

    def crear_campo(self, contenedor, texto, fila):
        tk.Label(
            contenedor,
            text=texto,
            bg=self.color_fondo,
            fg=self.color_texto,
            font=("Arial", 10),
        ).grid(row=fila, column=0, sticky="w", pady=(0, 6))

        entrada = ttk.Entry(contenedor, width=24)
        entrada.grid(row=fila, column=1, sticky="ew", pady=(0, 6))

        return entrada

    def crear_listado(self, contenedor, titulo):
        listado = tk.LabelFrame(
            contenedor,
            text=titulo,
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 10, "bold"),
            padx=10,
            pady=10,
        )
        listado.grid(row=0, column=1, sticky="nsew")

        return listado

    def crear_tabla(self, contenedor, columnas, encabezados):
        frame_tabla = tk.Frame(contenedor, bg=self.color_fondo)
        frame_tabla.pack(fill="both", expand=True)

        tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=12,
        )

        barra = ttk.Scrollbar(
            frame_tabla,
            orient="vertical",
            command=tabla.yview,
        )

        tabla.configure(yscrollcommand=barra.set)

        for columna, encabezado in zip(columnas, encabezados):
            tabla.heading(columna, text=encabezado)

            if columna == "identificador":
                ancho = 80
            elif columna == "fecha":
                ancho = 100
            else:
                ancho = 150

            tabla.column(columna, width=ancho, anchor="w")

        tabla.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

        return tabla

    def actualizar_tabla_productos(self):
        assert self.tabla_productos is not None

        self.limpiar_tabla(self.tabla_productos)
        for producto in self.restaurante_servicio.listar_productos():
            self.tabla_productos.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.precio,
                    producto.categoria,
                    producto.stock,
                ),
            )

    def limpiar_tabla(self, tabla):
        for item in tabla.get_children():
            tabla.delete(item)

    def obtener_datos_producto(self):
        assert self.producto_nombre_entry is not None
        assert self.producto_codigo_entry is not None
        assert self.producto_precio_entry is not None
        assert self.producto_categoria_entry is not None
        assert self.producto_stock_entry is not None

        return (
            self.producto_nombre_entry.get(),
            self.producto_codigo_entry.get(),
            float(self.producto_precio_entry.get()),
            self.producto_categoria_entry.get(),
            int(self.producto_stock_entry.get()),
        )

    def registrar_producto(self):
        try:
            self.restaurante_servicio.registrar_producto(
                *self.obtener_datos_producto()
            )
            self.limpiar_formulario_producto()
            self.actualizar_tabla_productos()
            self.actualizar_barra_estado()
            messagebox.showinfo(
                "Productos",
                "Producto registrado correctamente.",
            )
        except ValueError as error:
            messagebox.showerror("Productos", str(error))

    def cargar_producto(self):

        assert self.producto_codigo_entry is not None
        assert self.producto_nombre_entry is not None
        assert self.producto_precio_entry is not None
        assert self.producto_categoria_entry is not None
        assert self.producto_stock_entry is not None

        producto = self.restaurante_servicio.buscar_producto_por_codigo(
            self.producto_codigo_entry.get()
        )

        if producto is None:
            messagebox.showerror(
                "Productos",
                "No existe un producto con ese codigo.",
            )
            return

        self.limpiar_formulario_producto()

        self.producto_codigo_entry.insert(0, producto.codigo)
        self.producto_nombre_entry.insert(0, producto.nombre)
        self.producto_precio_entry.insert(0, producto.precio)
        self.producto_categoria_entry.insert(0, producto.categoria)
        self.producto_stock_entry.insert(0, producto.stock)


    def actualizar_producto(self):
        try:
            self.restaurante_servicio.actualizar_producto(
                *self.obtener_datos_producto()
            )
            self.actualizar_tabla_productos()
            messagebox.showinfo(
                "Productos",
                "Producto actualizado correctamente.",
            )
        except ValueError as error:
            messagebox.showerror("Productos", str(error))

    def eliminar_producto(self):
        assert self.producto_codigo_entry is not None

        try:
            self.restaurante_servicio.eliminar_producto(
                self.producto_codigo_entry.get()
            )
            self.limpiar_formulario_producto()
            self.actualizar_tabla_productos()
            self.actualizar_barra_estado()
            messagebox.showinfo(
                "Productos",
                "Producto eliminado correctamente.",
            )
        except ValueError as error:
            messagebox.showerror("Productos", str(error))

    def limpiar_formulario_producto(self):
        for entrada in (
            self.producto_codigo_entry,
            self.producto_nombre_entry,
            self.producto_precio_entry,
            self.producto_categoria_entry,
            self.producto_stock_entry,
        ):
            assert entrada is not None
            entrada.delete(0, tk.END)

        
    def mostrar_usuarios(self):
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_titulo_seccion("Usuarios registrados")

        for usuario in self.restaurante_servicio.listar_usuarios():
            texto = f"{usuario.identificacion} - {usuario.nombre} | usuario: {usuario.usuario}"
            self.crear_fila_informacion(texto)


    def obtener_opciones_usuarios_venta(self):
        self.opciones_usuarios_venta = {
        f"{usuario.identificacion} - {usuario.nombre}": usuario.identificacion
        for usuario in self.restaurante_servicio.listar_usuarios()
    }
        return self.opciones_usuarios_venta

    def obtener_opciones_productos_venta(self):
        self.opciones_productos_venta = {
        f"{producto.codigo} - {producto.nombre}": producto.codigo
        for producto in self.restaurante_servicio.listar_productos()
    }
        return self.opciones_productos_venta

    def crear_selector_venta(self, contenedor, etiqueta, fila, opciones):
        tk.Label(
            contenedor,
            text=etiqueta,
            bg=self.color_fondo,
            fg=self.color_texto,
            font=("Arial", 10, "bold"),
        ).grid(row=fila, column=0, sticky="w", pady=(0, 8), padx=(0, 10))

        selector = ttk.Combobox(
            contenedor,
            values=list(opciones.keys()),
            state="readonly",
            width=34,
        )
        selector.grid(row=fila, column=1, sticky="ew", pady=(0, 8))

        return selector

    def crear_titulo_seccion(self, texto):
        assert self.contenido is not None

        tk.Label(
            self.contenido,
            text=texto,
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 17, "bold"),
        ).pack(anchor="w", pady=(0, 14))

    def crear_fila_informacion(self, texto):
        assert self.contenido is not None

        fila = tk.Frame(
            self.contenido,
            bg="#FFFFFF",
            padx=14,
            pady=10,
        )
        fila.pack(fill="x", pady=(0, 8))

        tk.Label(
            fila,
            text=texto,
            bg="#FFFFFF",
            fg=self.color_texto,
            font=("Arial", 11),
        ).pack(anchor="w")

    def crear_barra_estado(self):
        barra_estado = tk.Frame(
            self,
            bg=self.color_secundario,
            padx=18,
            pady=8,
        )
        barra_estado.pack(fill="x", side="bottom")

        self.etiqueta_estado = tk.Label(
            barra_estado,
        text=(
            f"Productos: {self.restaurante_servicio.cantidad_productos()} | "
            f"Usuarios: {self.restaurante_servicio.cantidad_usuarios()} | "
            "Datos JSON locales"
        ),
        bg=self.color_secundario,
        fg=self.color_texto,
        font=("Arial", 10),
    )
        self.etiqueta_estado.pack(side="left")


    def actualizar_barra_estado(self):
        assert self.etiqueta_estado is not None

        self.etiqueta_estado.config(
            text=(
                f"Productos: {self.restaurante_servicio.cantidad_productos()} | "
                f"Usuarios: {self.restaurante_servicio.cantidad_usuarios()} | "
                "Datos JSON locales"
            )
        )


    def mostrar_ventas(self):
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_titulo_seccion("Ventas")

        cuerpo = tk.Frame(self.contenido, bg=self.color_fondo)
        cuerpo.pack(fill="both", expand=True)
        cuerpo.grid_columnconfigure(1, weight=1)
        cuerpo.grid_rowconfigure(0, weight=1)
        formulario = tk.LabelFrame(
            cuerpo,
            text="Registrar venta",
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 10, "bold"),
            padx=14,
            pady=14,
        )
        formulario.grid(row=0, column=0, sticky="n", padx=(0, 18))

        self.usuario_venta_combo = self.crear_selector_venta(
            formulario,
            "Usuario",
            0,
            self.obtener_opciones_usuarios_venta(),
        )

        self.producto_venta_combo = self.crear_selector_venta(
            formulario,
            "Producto",
            1,
            self.obtener_opciones_productos_venta(),
        )

        acciones = tk.Frame(formulario, bg=self.color_fondo)
        acciones.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(12, 0))

        self.crear_boton(
            acciones,
            "Registrar venta",
            self.registrar_venta,
            "Accion.TButton",
            "add.png",
        ).pack(fill="x")

        listado = self.crear_listado(cuerpo, "Ventas registradas")

        self.tabla_ventas = self.crear_tabla(
            listado,
            ("identificador", "usuario", "producto", "fecha"),
            ("Venta", "Usuario", "Producto", "Fecha"),
        )

        self.refrescar_ventas()

    def registrar_venta(self):
        assert self.usuario_venta_combo is not None
        assert self.producto_venta_combo is not None

        usuario_id = self.opciones_usuarios_venta.get(
            self.usuario_venta_combo.get(), ""
        )
        producto_codigo = self.opciones_productos_venta.get(
            self.producto_venta_combo.get(), ""
        )

        try:
            self.restaurante_servicio.registrar_venta(
                usuario_id,
                producto_codigo,
            )
            self.limpiar_formulario_venta()
            self.refrescar_ventas()
            messagebox.showinfo(
                "Ventas",
                "Venta registrada correctamente.",
            )
        except ValueError as error:
            messagebox.showerror("Ventas", str(error))

    def limpiar_formulario_venta(self):
        assert self.usuario_venta_combo is not None
        assert self.producto_venta_combo is not None

        self.usuario_venta_combo.set("")
        self.producto_venta_combo.set("")

    def refrescar_ventas(self):
        assert self.tabla_ventas is not None

        self.limpiar_tabla(self.tabla_ventas)

        for venta in self.restaurante_servicio.listar_ventas():
            usuario = self.restaurante_servicio.buscar_usuario_por_identificacion(
                venta.usuario_id
            )
            producto = self.restaurante_servicio.buscar_producto_por_codigo(
                venta.producto_codigo
            )

            texto_usuario = (
                venta.usuario_id
                if usuario is None
                else f"{usuario.identificacion} - {usuario.nombre}"
            )

            texto_producto = (
                venta.producto_codigo
                if producto is None
                else f"{producto.codigo} - {producto.nombre}"
            )

            self.tabla_ventas.insert(
                "",
                tk.END,
                values=(
                    venta.identificador,
                    texto_usuario,
                    texto_producto,
                    venta.fecha,
                ),
            )

        self.actualizar_barra_estado()

    def cerrar_sesion(self):
        self.al_cerrar_sesion()