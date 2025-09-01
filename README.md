# 📦 Billify ACME

Sistema de control de ventas para micromercados de **ACME SOFT**.
Este software permite gestionar facturación, clientes, productos y generar reportes de ventas a partir de archivos planos (`.dat`).

---

## 📋 Descripción del Proyecto

Billify ACME es un sistema de facturación desarrollado en Python que trabaja con tres archivos de datos:

* **productos.dat** → contiene el inventario de productos.
* **clientes.dat** → almacena los datos de clientes.
* **ventas.dat** → registra las ventas realizadas.

El sistema permite:

1. **Imprimir facturas** con desglose de IVA.
2. **Generar un resumen de facturación por cliente y mes.**
3. **Mostrar un diagrama de barras de facturación anual.**
4. **Obtener productos comunes comprados por dos clientes distintos.**

---

## 📂 Estructura del Proyecto

```
Billify-ACME/
│── main.py
│── README.md
│
├── data/
│   ├── clientes.dat
│   ├── productos.dat
│   └── ventas.dat
│
├── interfaz/
│   └── menu.py
│
├── modelo/
│   └── modelo.py
│
└── persistencia/
    └── persistencia.py

```

---

## ⚙️ Requerimientos

* Python **3.11+**
* No requiere librerías externas, solo **módulos estándar** de Python.

---

## ▶️ Ejecución

1. Clonar o descargar este repositorio.
2. Verificar que los archivos `productos.dat`, `clientes.dat` y `ventas.dat` estén en la raíz del proyecto.
3. Ejecutar el programa:

```bash
python main.py
```

4. Usar el menú interactivo:

```
----------------------------------------
*************** MENÚ *******************
 1. Imprimir Factura (R1)
 2. Resumen Cliente/Mes (R2)
 3. Diagrama Facturación Año (R3)
 4. Productos Comunes (R4)
 5. Salir
----------------------------------------
>>> Opción:
```

---

## 📊 Funcionalidades

✅ **R1 - Imprimir Factura**

* Muestra una factura detallada con subtotal, IVA (19%) y total.

✅ **R2 - Resumen de Cliente/Mes**

* Genera un informe con facturas de un cliente en un mes específico.

✅ **R3 - Diagrama de Facturación Anual**

* Imprime un gráfico de barras en consola comparando los valores de facturación por mes.

✅ **R4 - Productos Comunes**

* Lista los productos que dos clientes distintos han comprado en común.

---

## 🛠️ Validaciones

* Manejo de errores en lectura de archivos.
* Validación de códigos de cliente, producto y factura.
* Entradas controladas para evitar caídas inesperadas.

---

## 👨‍💻 Autor - Eimer Santiago

Proyecto académico desarrollado como práctica de **gestión de archivos y generación de reportes en Python**.
