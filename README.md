# Formateador de Listas de Estudiantes para la UCR

## Resumen

Al bajar una lista de estudiantes de ematrícula existen dos opciones: bajarlas como hoja de cálculo o como un pdf.
La segunda opción funciona bien para clases pequeñas, sin embargo se vuelve poco útil en clases grandes en las que uno tendría que copiar los numbres y carnets de los estudiantes uno por uno a su propia hoja de cálculo para llevar las notas de la clase.
La primera opción tiene el problema de que la hoja de cálculo comúnmente viene formateada de una forma extraña, con múltiples filas vacías entre estudiantes, con ciertas columnas que están desfasadas con respecto a otras columnas, etc.
Además, me dí cuenta como docente que no todas las columnas de esta lista de clase son relevantes, y de hecho que en la práctica sólo necesitaba las columnas con nombre completo, el carnet y el correo institucional del estudiante.

Por estas razones creé este pequeño script que automatiza en buena parte el proceso de crear un excel con las listas de clase.

## Uso

1. Copie este repositorio `git clone https://github.com/felimomo/FormateadorListasEmatricula.git`, `cd FormateadorListasEmatricula`. Si no cuenta con `git` instalado, puede bajar este repositorio manualmente en la parte superior de esta página.
2. Baje sus listas de clase en el login administrativo de ematrícula
3. Mueva los archivos al folder `FormateadorListasEmatricula / Input`
4. Instale dependencias `pip install -r requirements.txt`
5. Corra el script `python formateador.py -f Input/[archivo con la lista]`

El script crea un archivo csv en el folder Output. Este puede ser abierto con Excel, Numbers (Mac), etc, a conveniencia.