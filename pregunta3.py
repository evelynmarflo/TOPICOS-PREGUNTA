Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> blogs, palabras, datos=readfile('blogdata1.txt')
>>> clust=hcluster(datos,majatahan)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    clust=hcluster(datos,majatahan)
NameError: name 'majatahan' is not defined
>>> clust=hcluster(datos,manjatahan)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    clust=hcluster(datos,manjatahan)
NameError: name 'manjatahan' is not defined
>>> clust=hcluster(datos,manjathan)
>>> printclust(clust,blogs)
-
  Mitos y Timos
  -
    -
      -
        -
          Cholonymous: Blog Peruano de Actualidad y Tecnolog�a
          Xataka Ciencia
        -
          Genbeta Dev
          -
            Astrof�sica    y    F�sica
            -
              Curistoria - Curiosidades y an�cdotas hist�ricas
              Experimentos caseros
      -
        Hipertextual
        -
          -
            PC World Per�
            Tecnolog�a 7
          -
            -
              Imagen astronom�a diaria - Observatorio
              -
                Naukas
                Historias de la Historia
            -
              -
                Eureka
                -
                  La mentira esta ahi fuera
                  PC World en Espa�ol
              -
                EspacioCiencia.com
                -
                  -
                    Tecnolog�a Obsoleta
                    FayerWayer
                  -
                    La Ciencia y sus Demonios
                    -
                      C�rculo Esc�ptico Argentino
                      La Ciencia para todos
    -
      El retorno de los charlatanes
      Hispasec @unaaldia
>>> drawdendrogram(clust,blogs,'blogs5.jpg')
>>> 
