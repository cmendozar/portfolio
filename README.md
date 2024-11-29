# Portfolio Simulation

Este proyecto simula un portafolio de acciones y calcula las ganancias y retornos de un conjunto de activos entre dos fechas. Utiliza valores aleatorios para simular los precios de las acciones y realiza los cálculos de retorno total y retorno anualizado.

## Descripción

El script permite crear un portafolio de acciones, agregarle diferentes cantidades de cada acción, y luego calcular:

1. **Ganancia Total:** La diferencia entre el valor final y el valor inicial del portafolio.
2. **Retorno Anualizado:** El retorno que el portafolio habría obtenido si el rendimiento se mantuviera constante durante todo un año.

## Estructura del Proyecto

El código se divide en dos clases principales:

- **`Stock`**: Representa una acción en el portafolio. Cada acción tiene un precio que varía aleatoriamente entre 1 y 100.
  
- **`Portfolio`**: Representa el portafolio que contiene varias acciones (`Stock`). Permite agregar acciones, calcular el valor del portafolio en un día específico y calcular las ganancias y los retornos.

### Funcionalidades principales:

1. **`add_stock(stock, quantity)`**: Agrega una acción y su cantidad al portafolio.
2. **`value_at_date(date)`**: Calcula el valor total del portafolio en una fecha específica.
3. **`profit(init_date, final_date)`**: Calcula la ganancia del portafolio entre dos fechas.
4. **`annualized_return(ret, init_date, final_date)`**: Calcula el retorno anualizado basado en el retorno total del portafolio entre dos fechas.

## Uso

### Requisitos:

1. **Python 3.x**  
2. Librerías estándar de Python: `random`, `datetime`.

### Cómo ejecutar el script:

1. **Clonar el repositorio**:
   Si deseas usar este código, puedes clonar este repositorio o simplemente copiar el archivo `portfolio_simulation.py` a tu máquina local.

2. **Ejecutar el script**:
   Para ejecutar el script, simplemente corre el archivo `portfolio_simulation.py`:
   Ya tiene un metodo que simula un portafolio random.

   ```bash
   python3 portfolio.py
   ```

### Resultados:
   ```bash
        The portafolio Muguiwara:
        Has an initial capital amount of: $739.00.
        Has a final capital amount of: $808.00.
        Has a proft of : 69.00 u.
        The return between 01/11/2024 and 28/11/2024 is: 9.34%
        This is equivalent to a annual return of 234.25%.
   ```

   ```bash
        The portafolio Muguiwara:
        Has an initial capital amount of: $823.00.
        Has a final capital amount of: $819.00.
        Has a proft of : -4.00 u.
        The return between 01/11/2024 and 28/11/2024 is: -0.49%
        This is equivalent to a annual return of -6.37%.
   ```


### Mejoras

Me hubiese gustado añadir la fecha de inicio de cada stock cuando se agrega así tener un registro de cuando se agregó esa acción al portafolio ya que uno usualmente va a agregando diferentes activos en diferentes momentos al portafolio entonces las ganancias/rentabilidades van dependiendo de eso. (No lo hice por tiempo/alcance.)
