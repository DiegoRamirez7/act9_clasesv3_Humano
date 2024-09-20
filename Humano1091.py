print("act 9 clase humano")
print("Diego Ramirez mat: 22308051281091")
# zona de clases 
class Humano1091:
    #zona de atributos dentro de la clase
    edad=0
    peso=0
    estatura=0
    colordepelo=0
    colordeojos=0
    numerodealzado=0
    #zona de funciones dentro de la clase
    def correr1091(self,n):
        print(f"{n} esta corriendo")
    def sonrie1091(self,n):
        print(f"{n} esta sonriendo")
    def come1091(self,n):
        print(f"{n} esta comiendo")  
    def estudia1091(self,n):
        print(f"{n} esta estudiando")  
    def juega1091(self,n):
        print(f"{n} esta jugando")  
            
#zona de creacion de objetos
diego=Humano1091()
Miranda=Humano1091()
#zona de usando objetos
print("Resultados para Diego")
diego.edad=17
diego.peso=45
diego.estatura=168
diego.colordepelo="negro"
diego.colordeojos="cafes"
diego.numerodealzado=27

print(f"edad: {diego.edad}")
print(f"peso: {diego.peso}")
print(f"estatura: {diego.estatura}")
print(f"color de pelo: {diego.colordepelo}")
print(f"color de ojos: {diego.colordeojos}")
print(f"numero de calzado: {diego.numerodealzado}")
diego.correr1091("Diego")
diego.sonrie1091("Diego")
diego.come1091("Diego")
diego.estudia1091("Diego")
diego.juega1091("Diego")

print("Resultados para Miranda")    
Miranda.edad=18
Miranda.peso=52
Miranda.estatura=155
Miranda.colordepelo="cafe"
Miranda.colordeojos="cafes"
Miranda.numerodealzado=23
print(f"edad: {Miranda.edad}")
print(f"peso: {Miranda.peso}")
print(f"estatura: {Miranda.estatura}")
print(f"color de pelo: {Miranda.colordepelo}")
print(f"color de ojos: {Miranda.colordeojos}")
print(f"numero de calzado: {Miranda.numerodealzado}")
Miranda.correr1091("Miranda")
Miranda.sonrie1091("Miranda")
Miranda.come1091("Miranda")
Miranda.estudia1091("Miranda")
Miranda.juega1091("Miranda")