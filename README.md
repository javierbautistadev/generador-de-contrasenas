# Generador de contraseñas seguras

Un programa pequeño de Python con una ventana para crear contraseñas. Usa Tkinter, la interfaz gráfica de Python.

## Cómo usarlo

```bash
python3 generador.py
```

Necesitas una instalación de Python con Tkinter disponible.

Escribe una longitud entre 12 y 128 en la casilla y pulsa **Intro** o **Generar contraseña**. La longitud inicial es 20. La contraseña aparecerá debajo, repartida en varias líneas si es larga; pulsa **Copiar** para llevarla completa al portapapeles. Si escribes una longitud incorrecta, la ventana te indicará el rango permitido.

## Cómo está construido

1. `string.ascii_letters`, `string.digits` y `string.punctuation` forman el conjunto de caracteres posibles.
2. `secrets.choice` elige cada carácter con aleatoriedad adecuada para contraseñas.
3. La función comprueba que haya al menos una minúscula, una mayúscula, un número y un símbolo. Si falta alguno, vuelve a generar.
4. `crear_ventana()` conecta la casilla de longitud y los botones con la función. La contraseña se muestra en pantalla y no se guarda en ningún archivo.

Para ejecutar las pruebas:

```bash
python3 -m unittest -v
```

**Ejercicio:** cambia `LONGITUD_INICIAL` de 20 a 24. Recuerda actualizar también la prueba correspondiente.
