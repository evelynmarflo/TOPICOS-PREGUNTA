Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> blogs, palabras, datos =readfile('blogdata1.txt')
>>> clust=hcluster(datos,euclidean)
>>> printclust(clust,blogs)
-
  Hispasec @unaaldia
  -
    Mitos y Timos
    -
      El retorno de los charlatanes
      -
        Astrof�sica    y    F�sica
        -
          Experimentos caseros
          -
            Curistoria - Curiosidades y an�cdotas hist�ricas
            -
              Genbeta Dev
              -
                Cholonymous: Blog Peruano de Actualidad y Tecnolog�a
                -
                  Xataka Ciencia
                  -
                    Hipertextual
                    -
                      Eureka
                      -
                        Tecnolog�a 7
                        -
                          PC World en Espa�ol
                          -
                            PC World Per�
                            -
                              EspacioCiencia.com
                              -
                                Historias de la Historia
                                -
                                  La mentira esta ahi fuera
                                  -
                                    La Ciencia para todos
                                    -
                                      Naukas
                                      -
                                        Tecnolog�a Obsoleta
                                        -
                                          La Ciencia y sus Demonios
                                          -
                                            C�rculo Esc�ptico Argentino
                                            -
                                              FayerWayer
                                              Imagen astronom�a diaria - Observatorio
>>> drawdendrogram(clust,blogs,'blogs.jpg')
>>> 
