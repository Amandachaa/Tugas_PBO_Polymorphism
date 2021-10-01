# Nama : Amanda Chairunnisa
# NIM  : 2004625

class celana :
    def model (self):
        print ("Toko Amanda.store menjual berbagai model celana")

    def stok (self):
        print ("Dengan catatan stok sebagai berikut :")

class baggy(celana) :
    def model (self):                
        print (">> Baggy Pants")

    def stok (self):
        print ("234 pcs")

class kulot(celana) :
    def model (self):
        print (">> Kulot Jeans")

    def stok (self):
        print ("100 pcs")

class bf(celana):
    def model (self):
        print (">> Boyfriend Jeans")

    def stok (self):
        print ("54 pcs")

object_celana = celana()
object_baggy  = baggy()
object_kulot  = kulot()
object_bf     = bf()

object_celana.model()
object_celana.stok()

print ("====================")

object_baggy.model() 
object_baggy.stok()


print ("====================")

object_kulot.model()
object_kulot.stok()

print ("====================")

object_bf.model()
object_bf.stok()

print ("====================")