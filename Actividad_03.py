# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 12:29:13 2022

@author: HP EliteBook 2470p
"""

import tkinter as tk

ventana = tk.Tk()
ventana.geometry ("1000x700")
ventana.config(bg="Turquoise")

#Primera Fila Añadiendo Parametros
espacio = tk.Label(ventana, bg="Turquoise", fg="Turquoise")
espacio.grid (row = 0, column = 0)

texto1 = tk.Label(ventana, text="Focal (mm)=", bg="Turquoise", fg="gray20")
texto1.grid (row = 1, column = 0)

cuadro1 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro1.grid (row = 1, column = 1)

texto2 = tk.Label(ventana, text="Ancho de la imagen (Pixel) =", bg="Turquoise", fg="gray20")
texto2.grid (row = 1, column = 2)

cuadro2 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro2.grid (row = 1, column = 3)

texto3 = tk.Label(ventana, text="Alto de la imagen (Pixel) =", bg="Turquoise", fg="gray20")
texto3.grid (row = 1, column = 4)

cuadro3 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro3.grid (row = 1, column = 5)

#Segunda Fila Añadiendo Parametros 
espacio1 = tk.Label(ventana, bg="Turquoise", fg="Turquoise")
espacio1.grid (row = 2, column = 0)

texto4 = tk.Label(ventana, text="Ancho el sensor (mm) = ", bg="Turquoise", fg="gray20")
texto4.grid (row = 3, column = 0)

cuadro4 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro4.grid (row = 3, column = 1)

texto5 = tk.Label(ventana, text="Alto del sensor (mm)=", bg="Turquoise", fg="gray20")
texto5.grid (row = 3, column = 2)

cuadro5 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro5.grid (row = 3, column = 3)

texto6 = tk.Label(ventana, text="Altura del vuelo (m)=", bg="Turquoise", fg="gray20")
texto6.grid (row = 3, column = 4)

cuadro6 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro6.grid (row = 3, column = 5)

#Tercera Fila Añadiendo Parametros
espacio2 = tk.Label(ventana, bg="Turquoise", fg="gray20")
espacio2.grid (row = 4, column = 0)

texto7 = tk.Label(ventana, text="Solape Longitudinal (%) =", bg="Turquoise", fg="gray20")
texto7.grid (row = 5, column = 0)

cuadro7 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro7.grid (row = 5, column = 1)

texto8 = tk.Label(ventana, text="Solape Transversal (%) =", bg="Turquoise", fg="gray20")
texto8.grid (row = 5, column = 2)

cuadro8 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro8.grid (row = 5, column = 3)

texto9 = tk.Label(ventana, text="Largo de la parcela (m)=", bg="Turquoise", fg="gray20")
texto9.grid (row = 5, column = 4)

cuadro9 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro9.grid (row = 5, column = 5)

#Cuarta Fila Añadiendo Parametros
espacio3 = tk.Label(ventana, bg="Turquoise", fg="gray20")
espacio3.grid (row = 6, column = 0)

texto10 = tk.Label(ventana, text="Ancho de la parcela (m)=", bg="Turquoise", fg="gray20")
texto10.grid (row = 7, column = 0)

cuadro10 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro10.grid (row = 7, column = 1)

texto11 = tk.Label(ventana, text="Velocidad del vuelo (m/s)=", bg="Turquoise", fg="gray20")
texto11.grid (row = 7, column = 2)

cuadro11 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro11.grid (row = 7, column = 3)

espacio3 = tk.Label(ventana, bg="Turquoise", fg="Turquoise")
espacio3.grid (row = 8, column = 0)


espacio3 = tk.Label(ventana, bg="Turquoise", fg="coral")
espacio3.grid (row = 10, column = 0)


#Cálculo de los Parametros de la Variables
def resultados():
    textoResult.delete(1.0, tk.END)
    focal = float(cuadro1.get())
    Ancho_Img = float(cuadro2.get())
    Alto_Img = int(cuadro3.get())
    Ancho_Sensor = float(cuadro4.get())
    Alto_Sensor = float(cuadro5.get())
    RSI = Ancho_Sensor/Ancho_Img
    Altura_Vuelo = float(cuadro6.get())
    Solape_Long = float(cuadro7.get())
    solape_trans = float(cuadro8.get())
    largo_parcela = float(cuadro9.get())
    ancho_parcela = float(cuadro10.get())
    vel_vuelo = float(cuadro11.get())
    
    
    #GSD
    GSD = (((Altura_Vuelo * 100 )/ (focal)) * RSI)
    textoResult.insert(tk.END, f"GSD = {GSD}cm/pixel\n\n")
    
    #Escala de Vuelo
    escala_vuelo = 1/((focal/1000)/Altura_Vuelo)
    textoResult.insert(tk.END, f"Escala de vuelo = {escala_vuelo}\n\n")
    
    #Ancho de la imagen
    areatomada = (Ancho_Sensor*escala_vuelo)/1000
    textoResult.insert(tk.END, f"Ancho de la Imagen Sobre el Terreno = {areatomada}m\n\n")
    
    #Alto de la imagen
    areatomada = (Alto_Sensor*escala_vuelo)/1000
    textoResult.insert(tk.END, f"Alto de la Imagen Sobre el Terreno = {areatomada}m\n\n")
    
    #Base Aérea
    base_aer = (((Ancho_Img * GSD )/100)* (1-(Solape_Long/100)))
    textoResult.insert(tk.END, f"Base Aérea = {base_aer}\n\n")
    
    #Distancia entre vueltas
    Dist_vueltas = (((Alto_Img * GSD )/100)) * (1-(solape_trans/100))
    textoResult.insert(tk.END, f"Distancia entre vueltas = {Dist_vueltas}m\n\n")
    
    #Tiempo entre fotos y velocidad de vuelo
    tiem_fotos = base_aer/vel_vuelo
    vel_vuelo= base_aer/tiem_fotos
    textoResult.insert(tk.END, f"Tiempo entre fotos = {tiem_fotos}s\n\n")
    textoResult.insert(tk.END, f"Velocidad de Vuelo= {vel_vuelo}m/s\n\n")
    
    #Número de pasadas
    num_pasadas = round (ancho_parcela/Dist_vueltas)
    textoResult.insert(tk.END, f"Numero de pasadas = {num_pasadas}\n\n")
    
    #Número de fotos por vueltas
    num_fotos = round (largo_parcela/base_aer)+1
    textoResult.insert(tk.END, f"Numero de Fotos por vueltas = {num_fotos}\n\n")
    
    #Número de fotos por pasada
    num_vuelta= round (num_fotos)*(num_pasadas)+1
    textoResult.insert(tk.END, f"Numero de Fotos por Vuelo = {num_vuelta}\n\n")
    
    #Distancia de Vuelo
    dist_vuelo = (num_pasadas*largo_parcela)+ancho_parcela
    textoResult.insert(tk.END, f"Distancia de Vuelo = {dist_vuelo}m\n\n")
    
    #Duración de vuelo 
    t_vuelo= ((num_vuelta * tiem_fotos)/60)
    textoResult.insert(tk.END, f"Duracion del Vuelo = {t_vuelo}min")

    
#Resultados de los Calculos de los Parametros de las Variables
textoResult = tk.Text(ventana)
textoResult.grid(row = 9, column = 0, columnspan = 5)
  

#Botón de Cálculo 
boton_calculo = tk.Button(text = "Calcular", font= 'Calibri 12', command = resultados)
boton_calculo.grid(row = 12, column = 1, columnspan = 1)


#Título 
ventana.title("Calculadora de parámetros de vuelo de drone (Autor: Bryan Martinez)")

ventana.mainloop()