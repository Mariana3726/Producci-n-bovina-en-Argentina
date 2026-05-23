# Análisis de Producción y Rentabilidad Bovina en Argentina
## Introducción
En este proyecto se realiza un análisis exploratorio de datos (EDA) sobre la producción bovina en Argentina, con el objetivo de comprender la relación entre producción, ingrsos, costos y rentabilidad.
A partir de datos correspondientes al período 2015 - 2018, se busca identificar patrones, tendencias y posibles ineficiencias dentro del sistema productivo.

---

## Objetivos
- Analizar la evolución de la producción a lo largo del tiempo
- Evaluar la rentabilidad del sector
- Comparar distintos tipos de actividad productiva
- Identificar el impacto de los costos en el resultado económico
- Detectar relaciones entre producción y rentabilidad

---

## Dataset
El dataset contiene información productiva y económica del sector bovino en Argentina.

### Variables principales:
- Fecha_Medicion
- producción_(kh/ha)
- Ingreso_Bruto
- Costos_Directos
- Costos_Indirectos
- Resultado_Neto
- Id_Actividad

### Tipo de actividad:
- **1 → Ciclo completo** (cría + recría + engorde o invernada)
- **2 → Cría** (producción de terneros)
- **3 → Invernada** (engorde de animales)

## Tecnologías utilizadas
- Python
- Pandas
- Matplotlib

---

## Análisis realizados

### 🔹 1- Análisis temporal
Se analizó la evolución de la producción y el resultado neto por año.

**Resultados:**
- La producción alcanza su punto máximo en 2016
- A partir de 2017 se observa una caída en la producción
- El año 2018 presenta valores menores (posiblemente por datos incompletos)

---

### 🔹 2- Producción vs Rentabilidad
Se comparó la producción con el resultado económico.

**Insight:**
- El crecimiento del resultado neto en 2016 es mayor que el de la producción
- Ésto sugiere una mejora en la eficiencia o en las condiciones económicas

---

### 🔹 3- Análisis por actividad

Se evaluó el resultado neto promedio según el tipo de actividad.

**Resultados:**
- Ciclo completo -> mayor rentabilidad
- Cría -> rentabilidad intermedia
- Invernada -> rentabilidad significativamente baja

---

### 🔹 4- Producción por actividad

Se compararon los niveles de producción entre actividades.

**Resultados:**
- La invernada presenta la mayor producción
- Sin embargo, no es la más rentable

  **Insight clave:**
  Una mayor producción no implica necesariamente una mayor rentabilidad.

---

### 🔹 5- Análisis de costos

Se analizaron ingresos y costos promedio por actividad.

**Resultados:**
- La invernada tiene los ingresos más altos
- Pero también presenta los costos más elevados
- Esto reduce significativamente su resultado neto

---

## Principales insights

- El año 2016 presenta el mejor desempeño general
- El ciclo completo es la actividad más rentable
- La invernada, a pesar de producir más, no es eficiente económicamente
- Los costos tienen un impacto determinante en la rentabilidad
- Mayor ingreso no garantiza mayor ganancia

## ✔️Conclusión✔️
El análisis demuestra que la rentabilidad en la producción bovina no depende únicamente del nivel de producción, sino principalmente de la eficiencia en la gestión de costos.
El ciclo completo se posiciona como la estartegia más eficiente, al capturar mayor valor a lo largo de toda la cadena productiva. Por otro lado, la invernada, si bien genera altoso niveles de producción e ingresos, presenta una estructura de costos que limita significativamente su rentabilidad. 





