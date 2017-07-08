Animación del viajante
=============================

Él siguiente código nos indicará los caminos que tendrá que realizar el repartidor del delivery.

Tenemos un conjunto de 20 puntos de reparto para 4 añgoritmos que usaremos para encontrar el camino más corto entre estos
Los algoritmos son:

1. Ruta random, inicia en un punto y selecciona aleatoriamente el siguiente punto no visitado, hasta visitar todas.
2. Greedy, inicia en un punto y selecciona como próxima punto a repartir el punto no visitado que esté más cerca al punto actual.
3. 2-Opt, Crea una ruta random y luego optimiza con el algoritmo 2-opt
4. Alineamiento simultaneo. Primero crea una ruta aleatoria, y optimiza las visitas con el algoritmo 2-opt y el alineamiento simultaneo

Para poder apreciar la animación, necesitas tener instalado:
-Python (Versión 2)
-ffmeg
		sudo apt-get install ffmpeg
-matplotlib 
		sudo pip install matplotlib
-tkinter
		sudo apt-get install python-tk

Para crear la animación, ubicarse en la carpeta del repositorio y ejecutar los comandos:
	make .anim    ---> crea los archivos png
 	make		  ---> crea la animación sa.mp4 
