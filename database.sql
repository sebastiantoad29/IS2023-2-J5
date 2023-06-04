-- Tabla: Administrador
DROP TABLE IF EXISTS administrador;
CREATE TABLE administrador (
    id_admin VARCHAR(200) NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    apellidoP VARCHAR(45) NOT NULL,
    apellidoM VARCHAR(45) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    contraseña VARCHAR(45) NOT NULL,
    PRIMARY KEY (id_admin)
);

-- Tabla: Vendedor
DROP TABLE IF EXISTS vendedor;
CREATE TABLE vendedor (
    id_vendedor INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellidoP VARCHAR(50) NOT NULL,
    apellidoM VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(50) NOT NULL,
    telefono VARCHAR(20),
    rol VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_vendedor)
);

-- Tabla: Usuario
DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario (
    id_usuario INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellidoP VARCHAR(50) NOT NULL,
    apellidoM VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(50) NOT NULL,
    telefono VARCHAR(20),
    rol VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_usuario)
);

-- Tabla: Producto
DROP TABLE IF EXISTS producto;
CREATE TABLE producto (
    id_producto INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    descripcion MEDIUMTEXT NOT NULL,
    img VARCHAR(100),
    inventario INT NOT NULL,
    PRIMARY KEY (id_producto)
);

-- Tabla: Pedido
DROP TABLE IF EXISTS pedido;
CREATE TABLE pedido (
    id_pedido INT NOT NULL,
    id_cliente INT NOT NULL,
    id_vendedor INT NOT NULL,
    reporte_generado_id INT,
    status VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id_cliente) REFERENCES usuario (id_usuario),
    FOREIGN KEY (id_vendedor) REFERENCES usuario (id_usuario),
    FOREIGN KEY (reporte_generado_id) REFERENCES reporte (id_reporte)
);

-- Tabla: Reporte
DROP TABLE IF EXISTS reporte;
CREATE TABLE reporte (
    id_reporte INT NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    monto INT NOT NULL,
    id_cliente INT NOT NULL,
    forma_pago VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_reporte),
    FOREIGN KEY (id_cliente) REFERENCES usuario (id_usuario)
);

-- Tabla: Contener_productos
DROP TABLE IF EXISTS contener_productos;
CREATE TABLE contener_productos (
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    PRIMARY KEY (id_pedido, id_producto),
    FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
    FOREIGN KEY (id_producto) REFERENCES producto (id_producto)
);

-- Tabla: Generar_reporte
DROP TABLE IF EXISTS generar_reporte;
CREATE TABLE generar_reporte (
    id_reporte INT NOT NULL,
    id_pedido INT NOT NULL,
    PRIMARY KEY (id_reporte, id_pedido),
    FOREIGN KEY (id_reporte) REFERENCES reporte (id_reporte),
    FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido)
);

-- Tabla: Realizar_pedido
DROP TABLE IF EXISTS realizar_pedido;
CREATE TABLE realizar_pedido (
    id_pedido INT NOT NULL,
    id_cliente INT NOT NULL,
    total INT NOT NULL,
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
    FOREIGN KEY (id_cliente) REFERENCES usuario (id_usuario)
);

-- Tabla: Atender_pedido
DROP TABLE IF EXISTS atender_pedido;
CREATE TABLE atender_pedido (
    id_pedido INT NOT NULL,
    id_vendedor INT NOT NULL,
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
    FOREIGN KEY (id_vendedor) REFERENCES vendedor (id_vendedor)
);
