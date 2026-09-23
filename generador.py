"""Generador sencillo de contraseñas con una pequeña ventana."""

import secrets
import string

LONGITUD_MINIMA = 12
LONGITUD_MAXIMA = 128
LONGITUD_INICIAL = 20
RANGO_LONGITUD = f"{LONGITUD_MINIMA} y {LONGITUD_MAXIMA}"


def generar_contrasena(longitud=LONGITUD_INICIAL):
    """Devuelve una contraseña con letras, números y símbolos."""
    if not LONGITUD_MINIMA <= longitud <= LONGITUD_MAXIMA:
        raise ValueError(
            f"La longitud debe estar entre {RANGO_LONGITUD} caracteres."
        )

    alfabeto = string.ascii_letters + string.digits + string.punctuation

    while True:
        contrasena = "".join(secrets.choice(alfabeto) for _ in range(longitud))
        if (
            any(c in string.ascii_lowercase for c in contrasena)
            and any(c in string.ascii_uppercase for c in contrasena)
            and any(c in string.digits for c in contrasena)
            and any(c in string.punctuation for c in contrasena)
        ):
            return contrasena


def crear_ventana():
    """Construye la ventana y conecta sus botones."""
    import tkinter as tk
    from tkinter import ttk

    ventana = tk.Tk()
    ventana.title("Generador de contraseñas")
    ventana.resizable(False, False)

    estilo = ttk.Style(ventana)
    estilo.configure("Titulo.TLabel", font=("Helvetica Neue", 19, "bold"))
    estilo.configure("Ayuda.TLabel", font=("Helvetica Neue", 11))

    contenido = ttk.Frame(ventana, padding=24)
    contenido.grid(sticky="nsew")
    contenido.columnconfigure(0, weight=1)

    ttk.Label(contenido, text="Generador de contraseñas", style="Titulo.TLabel").grid(
        row=0, column=0, columnspan=2, sticky="w"
    )
    ttk.Label(
        contenido,
        text="Escribe la longitud y pulsa Intro o Generar.",
        style="Ayuda.TLabel",
    ).grid(row=1, column=0, columnspan=2, pady=(4, 22), sticky="w")

    ttk.Label(contenido, text="Longitud de la contraseña").grid(
        row=2, column=0, columnspan=2, sticky="w"
    )
    longitud = tk.StringVar(value=str(LONGITUD_INICIAL))
    entrada = ttk.Entry(contenido, name="longitud", textvariable=longitud, width=28)
    entrada.grid(row=3, column=0, pady=(8, 0), sticky="ew")

    resultado = tk.StringVar()
    mensaje = tk.StringVar(value="La contraseña aparecerá aquí.")

    def generar():
        try:
            nueva = generar_contrasena(int(longitud.get()))
        except ValueError:
            resultado.set("")
            boton_copiar.state(["disabled"])
            mensaje.set(f"Escribe un número entre {RANGO_LONGITUD}.")
        else:
            resultado.set(nueva)
            boton_copiar.state(["!disabled"])
            mensaje.set("Contraseña lista para copiar.")

    def copiar():
        ventana.clipboard_clear()
        ventana.clipboard_append(resultado.get())
        mensaje.set("Contraseña copiada.")

    ttk.Button(contenido, text="Generar contraseña", command=generar).grid(
        row=3, column=1, padx=(12, 0), pady=(8, 0), sticky="ew"
    )
    ttk.Label(
        contenido,
        text=f"Introduce un número entre {RANGO_LONGITUD}.",
        style="Ayuda.TLabel",
    ).grid(row=4, column=0, columnspan=2, pady=(8, 18), sticky="w")
    ttk.Separator(contenido).grid(
        row=5, column=0, columnspan=2, pady=(0, 18), sticky="ew"
    )
    ttk.Label(contenido, text="Contraseña generada").grid(
        row=6, column=0, columnspan=2, sticky="w"
    )
    ttk.Label(
        contenido,
        name="resultado",
        textvariable=resultado,
        font=("Menlo", 12),
        wraplength=440,
        justify="left",
        anchor="w",
        padding=12,
        relief="solid",
    ).grid(row=7, column=0, columnspan=2, pady=(8, 0), sticky="ew")
    boton_copiar = ttk.Button(contenido, text="Copiar", command=copiar)
    boton_copiar.grid(row=8, column=1, padx=(12, 0), pady=(10, 0), sticky="e")
    boton_copiar.state(["disabled"])
    ttk.Label(contenido, textvariable=mensaje, style="Ayuda.TLabel").grid(
        row=8, column=0, pady=(10, 0), sticky="w"
    )

    entrada.bind("<Return>", lambda _evento: generar())
    entrada.focus_set()
    entrada.selection_range(0, "end")
    return ventana


def main():
    crear_ventana().mainloop()


if __name__ == "__main__":
    main()
