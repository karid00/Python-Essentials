class ciudadanoec():
    #con los parentesis se pueden dar más cosas a los atributos, se pueden poner o no
    #se necesita definir un método init
    def __init__(self, cedula,nombre,apellido,edad):
    #define e inivia o valida algo para poner majerar atributos, herencias,etc
    #siempre se usa def __init__ para los atributos
    #se usa self por que se respeta el lenguage pero si se puede usar otra palabra
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=edad
        self.edad=edad
        #puede tener atributos o no
    #ahora podemos definir funciones
    def genlista(self):
        try:
            return [self.nombre,self.apellido,self.edad,self.cedula]
            print("lista construida")
        except:
            print("error")
    #se puede dar mas de una def
    def gendic(self,trabajo):
        self.trabajo=trabajo
        return {"cedula":self.cedula,"profesión":self.trabajo}
     
    