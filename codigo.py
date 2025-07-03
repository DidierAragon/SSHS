#  Sistema de Seguimiento de Hábitos Saludables
# lo primero que va aparecer sera un mensaje que le da la bienvenidad a la pagina
# creo tres variables donde le pido al usuario el nombre la edad y el numero de identificacion

nombre = input("ingrese su nombre completo: ")

edad = int(input("ingrse su edad: "))

id = int(input("ingrese su numero de identificacion: "))

# guardo esta informacion en una tupla que sera el usuario
# y tambien creo una lista vacia que se llama seguimient

usuario = (nombre,edad,id)

seguimiento = []

# muestro el menu con un while true para que siempre aparezca hasta que el usuario le de a la 
# opcion de salir

while True:
    print("\nMENU: \n 1: Registrar dia y Habito \n 2: Ver Historial \n 3: Calcular promedio semanal \n 4: mostrar porcentaje de cumplimiento por habito \n 5: Salir ")
    
    # creo una variable donde le digo al usuario que escoja una opcion
    # tambien comienzo las condiciones 
    
    opcion = input("ingrease una opcion 1-5: ")
    
    # si el usuario escoje la opcion 5 es decir la de salir simplemete le aparecera un mensaje que salio del programa y se termina con un break
    
    if opcion == "5":
        print("ha salido del programa ")
        break
    
    # si el usuario elije la opcion 1 le va apedir que ingrese el dia de la semana luego creo creo un contador para los dias de la semana dentro de la lista de seguimiento  
    
    elif opcion == "1":
        dia = input("ingrese el dia de la semana: ")
        i = 0
    
    # luego creo una variable que se llama dia duplicado para identificar si hay dias duplicado dentro de  la lista de seguimiento
    
        dia_duplicado = False
    
    # en este while verifica si el dia ya esta registrado luego accede al primer campo de nombre del dia en cada tupla 
    
        while i < len(seguimiento):
            if seguimiento [i][0] == dia:
                dia_duplicado = True
                break
            i += 1
        if dia_duplicado:
            print("este dia ya esta registrado")
   
   # luego solicito los dato al usuario como el agua consumida,  los minutos de ejercicio, las horas de sueño y si se alimento bien
      
        else:
            a = input("litros de agua consumido: ")
            e = input("minutos de ejercicio: ")
            s = input("horas de sueño: ")
            c = input("alimentacion saludable? (si/no): ").lower()
            error = False
   
    # convierto los datos que me dio el usuario a float e int
            
            try:
                agua=float(a)
                ejercicio=int(e)
                sueño=float(s)
  
    # luego miro que los datos que me dio el usuario sean positivos y que haya escrito en alimentacion la opciones correctas
                
                if agua < 0 or ejercicio < 0 or sueño < 0:
                    print("los valores deben ser positivos: ")
                elif c != "si" and c != "no":
                    print("la opcion de alimentacion debe ser (si o no): ")
    
    # ingreso los datos correctas a la lista de seguiomiento para luego decirle al usuario que se guardo exitosamente si los datos son incorrectos le digo al usuario que los ingrese bien
               
                else:
                    seguimiento.append((dia,agua, ejercicio, sueño, c))
                    print("registro exitoso")
            except:
                print("datos incorrecto, ingresar datos correctos.")

    elif opcion == "2":
  
    # creo un print donde le doy la bienvenida al historial, luego creo un contador vacio 
    #abro un while para contar los datos de la lista de seguimiento donde guardamos las atualizaciones que el #usuario escribe 
       
        print("historial de habitos")
        i = 0
        while i < len(seguimiento):
   
    # creo una variable que toma los valores que conto la variable "i" y que muestra cada elemento de la lista #que el usuario ingreso luego muestro el historial en un print
   
            reg = seguimiento[i]
            print(f"{reg[0]},\n agua= {(reg[1])},\n ejercicio= {(reg[2])} \nminutos sueño= {(reg[3])},\n alimentacion saludable= {(reg[4])}")
            i += 1
    elif opcion == "3":

    #creo un if que cuenta los elemento de la lista y si la lista esta vacia entonces muestro un mensaje que dice que no hay registro y por lo tanto no se puede calcular
        
        if len(seguimiento) == 0:
            print("no hay registro para calcular")
    # pero si en la lista hay elementos entoces creo 4 contadores con para cada elemento de la lista
        else:
            total_agua = 0
            total_ejercicio = 0
            total_sueño = 0
            i = 0
   
    # luego abro un while que mira si el contador "i" es menor a los valores de la lista si esto es asi a los #otros tres contadores se le suma de a uno de acuerdo al orden que esta guardado en la lista y el contador #"i" va sumando en uno en uno hasta que se mas grande que los valores de la lista
           
            while i < len(seguimiento):
                total_agua  += seguimiento[i][1]
                total_ejercicio += seguimiento[i][2]
                total_sueño += seguimiento[i][3]
                i += 1
    #creo una variable de dias el cual cuenta los valores que hay dentro de la lista para luego dividirlo por #cada elemento y asi obtener el promedio por ultimo solo imprimo el promedio de cada area
                dias = len(seguimiento)
            print("----promedio semanal------- ")
            print(f"agua: {total_agua / dias} l")
            print(f"ejercicio: {total_ejercicio / dias} M")
            print(f"sueño: {total_agua / dias} H")
