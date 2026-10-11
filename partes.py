import pandas as pd

#parte 1
print("\nPARTE 1: EXPLORACIÓN INICIAL\n")

df = pd.read_csv("ventas_tienda.csv")

print("\nPrimeras 10 filas:")
print(df.head(10))

print("\nÚltimas 5 filas:")
print(df.tail(5))

print("\nEstructura (info):")
df.info()

print("\nTipos de datos:")
print(df.dtypes)

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nRegistros duplicados:", df.duplicated().sum())

#parte 2

print("\nPARTE 2: LIMPIEZA Y TRANSFORMACIÓN\n")
df = df.dropna(subset=["precio", "cantidad"])
df = df.fillna({"cliente": "Desconocido", "ciudad": "Desconocida",
                "producto": "Desconocido", "categoria": "Desconocida",
                "metodo_pago": "Desconocido"})

df["fecha"] = pd.to_datetime(df["fecha"])

print("\nTipos después de la conversión:")
print(df.dtypes)
df = df.drop_duplicates()
df["total_venta"] = df["precio"] * df["cantidad"]
df["mes"] = df["fecha"].dt.month
df["dia_semana"] = df["fecha"].dt.day_name()

print("\nDataFrame transformado:")
print(df.head())

#parte 3
print("\nPARTE 3: EDA\n")

print("\nTotal de ingresos:", df["total_venta"].sum())
print("Promedio de venta:", round(df["total_venta"].mean(), 2))
print("Número total de ventas:", len(df))

ventas_por_ciudad = df["ciudad"].value_counts()
ingreso_por_ciudad = df.groupby("ciudad")["total_venta"].sum().sort_values(ascending=False)
print("\nNúmero de ventas por ciudad:")
print(ventas_por_ciudad)
print("\nCiudad con más ventas:", ventas_por_ciudad.idxmax())
print("\nIngreso por ciudad:")
print(ingreso_por_ciudad)
print("Ciudad con mayor ingreso:", ingreso_por_ciudad.idxmax())

unidades_producto = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False)
ingreso_producto = df.groupby("producto")["total_venta"].sum().sort_values(ascending=False)
print("\nUnidades vendidas por producto:")
print(unidades_producto)
print("Producto más vendido:", unidades_producto.idxmax())
print("\nIngreso por producto:")
print(ingreso_producto)
print("Producto más rentable:", ingreso_producto.idxmax())

conteo_pago = df["metodo_pago"].value_counts()
print("\nConteo por método de pago:")
print(conteo_pago)
print("Método más frecuente:", conteo_pago.idxmax())

ventas_mes = df.groupby("mes")["total_venta"].sum()
print("\nVentas (ingresos) por mes:")
print(ventas_mes)

ventas_por_dia = df["dia_semana"].value_counts()
print("\nNúmero de ventas por día de la semana:")
print(ventas_por_dia)
print("Día de la semana con más ventas:", ventas_por_dia.idxmax())

ingreso_por_fecha = df.groupby("fecha")["total_venta"].sum()
print("Fecha con mayor ingreso:", ingreso_por_fecha.idxmax().date(),
      "->", ingreso_por_fecha.max())

#parte 4
print("\nPARTE 4: GROUPBY\n")

print("\n1. Ventas por categoría:")
print(df.groupby("categoria")["total_venta"].sum())

print("\n2. Ventas por ciudad y categoría:")
print(df.groupby(["ciudad", "categoria"])["total_venta"].sum())

print("\n3. Top 5 clientes por gasto total:")
print(df.groupby("cliente")["total_venta"].sum().sort_values(ascending=False).head(5))

print("\n4. Promedio de compra por cliente:")
print(df.groupby("cliente")["total_venta"].mean().round(2).sort_values(ascending=False))

