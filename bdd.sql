create database bdd1;
use bdd1;
CREATE TABLE administrador (
  admin_id VARCHAR(200) NOT NULL,
  nombre VARCHAR(45) NOT NULL,
  apellidoP VARCHAR(45) NOT NULL,
  apellidoM VARCHAR(45) NOT NULL,
  email VARCHAR(45) NOT NULL,
  password VARCHAR(45) NOT NULL,
  telefono VARCHAR(20),
  PRIMARY KEY (admin_id)
);

CREATE TABLE usuario (
    usuario_id INT NOT NULL auto_increment,
    nombre VARCHAR(50) NOT NULL,
    apellidoP VARCHAR(50) NOT NULL,
    apellidoM VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    telefono VARCHAR(20),
    PRIMARY KEY (usuario_id)
);

CREATE TABLE vendedor (
    vendedor_id INT NOT NULL auto_increment,
    nombre VARCHAR(50) NOT NULL,
    apellidoP VARCHAR(50) NOT NULL,
    apellidoM VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    telefono VARCHAR(20),
    PRIMARY KEY (vendedor_id)
);

CREATE TABLE producto (
    id_producto INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    descripcion MEDIUMTEXT NOT NULL,
    img VARCHAR(100),
    inventario INT NOT NULL,
    PRIMARY KEY (id_producto)
);

CREATE TABLE reporte (
    reporte_id INT NOT NULL,
    cliente_id INT NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    monto INT NOT NULL,
    pedido_id INT NOT NULL,
    PRIMARY KEY (reporte_id),
    FOREIGN KEY (cliente_id) REFERENCES usuario (usuario_id)
);

CREATE TABLE pedido (
    pedido_id INT NOT NULL,
    cliente_id INT NOT NULL,
    reporte_generado_id INT NOT NULL,
    status VARCHAR(20) NOT NULL,
    PRIMARY KEY (pedido_id),
    FOREIGN KEY (cliente_id) REFERENCES usuario (usuario_id) ON DELETE CASCADE
);

CREATE TABLE generar_reporte (
    reporte_id INT NOT NULL,
    pedido_id INT NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedido (pedido_id),
    FOREIGN KEY (reporte_id) REFERENCES reporte (reporte_id)
);

CREATE TABLE realizar_pedido (
    pedido_id INT NOT NULL,
    cliente_id INT NOT NULL,
    total INT NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedido (pedido_id),
    FOREIGN KEY (cliente_id) REFERENCES usuario (usuario_id)
);

CREATE TABLE atender_pedido (
    pedido_id INT NOT NULL,
    vendedor_id INT NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedido(pedido_id),
    FOREIGN KEY (vendedor_id) REFERENCES vendedor(vendedor_id)
);

CREATE TABLE contener_productos (
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedido(pedido_id),
    FOREIGN KEY (producto_id) REFERENCES producto(id_producto)
);
