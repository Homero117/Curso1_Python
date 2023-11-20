"""
Operador Nombre Descripción
a + b   Adición Suma de a y b
a - b   Resta Diferencia de a y b
a * b   Producto de multiplicación de a y b
a / b   División verdadera Cociente de a y b
a // b  División de piso Cociente de a y b, eliminando partes fraccionarias
a % b   Módulo Resto entero después de la división de a por b
a ** b  Exponenciación a elevada a la potencia de b
-a      Negación El negativo de a
"""

# Minimos y Maximos
print(min(1, 2, 3)) #1
print(max(1, 2, 3)) #3

# abs devuelve el valor absoluto de un argumento
print(abs(32)) #32
print(abs(-32)) #32

#podemos especificar un valor para sep para poner una cadena especial entre nuestros argumentos impresos
print(1, 2, 3, sep=' < ')



#Agregar argumentos opcionales con valores predeterminados a las funciones que definimos
def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (En este caso, no necesitamos especificar el nombre del argumento, porque no es ambiguo).
greet("world")
"""
Hello, Colin
Hello, Kaggle
Hello, world
"""
#el siguiente truco para intercambiar dos variables en una línea:
a = [1, 2, 3]
b = [3, 2, 1]

a, b = b, a
#La solución más directa es usar una tercera variable para almacenar temporalmente uno de los valores antiguos
tmp = a
a = b
b = tmp

#redondiar un numero 
num= 3.14159
round(num, 2) #3.14

u = -57.07997890
round (u,4) #-57.08 

#Estos son operadores que responden preguntas de sí/no
"""
Operación.      Descripción.                 Operación.      Descripción.
a == b          a igual a b.                  a != b         a no es igual a b.
a < b           a menor que b.                 a > b          a mayor que b.
a <= b          a menor o igual que b.        a >= b         a mayor o igual que b.
"""


#los amigos Alice, Bob y Carol, que compartían dulces, intentaron dividir los dulces en partes iguales. Por el bien de su amistad,
# los dulces sobrantes serían aplastados. Por ejemplo, si en conjunto traen a casa 91 dulces, tomarán 30 cada uno y aplastarán 1.
#A continuación se muestra una función simple que calculará la cantidad de dulces para aplastar para cualquier cantidad de 
# dulces en total.

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % 3
#Modifíquelo para que, opcionalmente, tome un segundo argumento que represente la cantidad de amigos entre los que se dividen los dulces. Si no se proporciona un segundo argumento, debe suponer 3 amigos, como antes.

def to_smash(total_candies, numerosAmigos=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % numerosAmigos


"""
Recuerde usar == en lugar de = al hacer comparaciones. Si escribes n == 2 estás preguntando por el valor de n. 
Cuando escribes n = 2 estás cambiando el valor de n.
"""

"""
Las declaraciones condicionales, a menudo denominadas declaraciones si-entonces, le permiten controlar qué 
 fragmentos de código se ejecutan en función del valor de alguna condición booleana. Aquí hay un ejemplo:
"""
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0) #0 is zero
inspect(-15) #-15 is negative



"""
Hemos visto int(), que convierte las cosas en ints, y float(), que convierte las cosas en flotantes, 
por lo que no te sorprenderá saber que Python tiene una función bool() que convierte las cosas en bools.
"""
print(bool(1)) # todos los números se tratan como verdaderos, excepto 0
print(bool(0))
print(bool("asf")) # todas las cadenas se tratan como verdaderas, excepto la cadena vacía ""
print(bool(""))
# Secuencias generalmente vacías (cadenas, listas y otros tipos, como listas y tuplas)
# son "falsedad" y el resto son "veraces"

"""
En la celda a continuación, defina una función llamada signo que tome un argumento numérico y devuelva -1 si es negativo, 
1 si es positivo y 0 si es 0.
"""
def f(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0




#lista
#Las listas en Python representan secuencias ordenadas de valores.
primes = [2, 3, 5, 7]

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (La coma después del último elemento es opcional)
]
# (También podría haber escrito esto en una línea, pero puede ser difícil de leer)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

#Una lista puede contener una combinación de diferentes tipos de variables
my_favourite_things = [32, 'raindrops on roses', help]

#Python usa indexación basada en cero, por lo que el primer elemento tiene índice 0.
planets[0] #Mercury

#Se puede acceder a los elementos al final de la lista con números negativos, comenzando desde -1
planets[-1] #Neptune

planets[-2] #Uranus

#¿Cuáles son los tres primeros planetas? Podemos responder a esta pregunta usando el corte:
planets[0:3] #['Mercury', 'Venus', 'Earth']

#Los índices inicial y final son opcionales. Si omito el índice de inicio, se supone que es 0. Así que podría reescribir 
# la expresión anterior como:
planets[:3] # #['Mercury', 'Venus', 'Earth']

#Si omito el índice final, se supone que es la longitud de la lista.
planets[3:] #['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Todos los planetas excepto el primero y el último.
planets[1:-1] #['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']

# Los ultimos 3 planetas
planets[-3:] #['Saturn', 'Uranus', 'Neptune']

#digamos que queremos cambiar el nombre de Mars:
planets[3] = 'Malacandra' #['Mercury','Venus','Earth','Malacandra','Jupiter','Saturn','Uranus','Neptune']

planets[:3] = ['Mur', 'Vee', 'Ur'] #['Mur', 'Vee', 'Ur', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#"len" da la longitud de una lista:
# ¿Cuántos planetas hay?
len(planets) #8

#"sorted" devuelve una versión ordenada de una lista:
sorted(planets) #['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']

#"sum" hace lo que cabría esperar: Suma
primes = [2, 3, 5, 7]
sum(primes) #17

#Maximos y minimos
max(primes) #7
min(primes) #2

"""
En Python, la parte imaginaria de un número complejo se puede especificar utilizando el sufijo "j" o "J". Por ejemplo, 
el número complejo 3 + 4j representa un número con una parte real de 3 y una parte imaginaria de 4.

Sin embargo, si necesitas acceder o manipular específicamente la parte imaginaria de un número complejo en Python, puedes utilizar 
el atributo imag. Este atributo devuelve la parte imaginaria del número complejo como un valor de punto flotante.

Aquí hay un ejemplo para demostrar cómo usar el atributo imag:

numero_complejo = 3 + 4j
parte_imaginaria = numero_complejo.imag
print(parte_imaginaria)  # imprime 4.0

En este ejemplo, se crea un número complejo 3 + 4j, y luego se accede a la parte imaginaria utilizando el atributo imag. 
La variable parte_imaginaria almacenará el valor 4.0.
"""

"""

En Python, el sufijo "j" o "J" se utiliza para denotar la parte imaginaria de un número complejo. 
La parte real se escribe normalmente y la parte imaginaria se escribe como un número real multiplicado por "j" o "J".

Por ejemplo, el número complejo 3 + 4j se puede interpretar como 3 en la parte real y 4 en la parte imaginaria. 
Este número se puede crear en Python como 3 + 4j.

Es importante tener en cuenta que al utilizar números complejos en Python, el sufijo "j" o "J" debe agregarse después de 
la parte imaginaria, sin espacios en blanco. De lo contrario, se generaría un error de sintaxis.

Aquí hay un ejemplo que muestra cómo crear un número complejo en Python utilizando el sufijo "j":

numero_complejo = 2 + 3j
print(numero_complejo)  # imprime (2+3j)

En este ejemplo, se crea un número complejo 2 + 3j y se imprime en la consola utilizando 
la función print(). La salida del programa sería (2+3j).

"""

#los números en Python llevan una variable asociada llamada imag que representa su parte imaginaria.
x = 12
# x es un número real, por lo que su parte imaginaria es 0.
print(x.imag) #0
# A continuación, le mostramos cómo hacer un número complejo, en caso de que alguna vez haya sentido curiosidad:
c = 12 + 3j
print(c.imag) #3.0


"""
La función bit_length() es un método integrado en Python que se utiliza para encontrar la cantidad de bits necesarios para representar 
un número entero en binario. Esta función devuelve un entero que representa la cantidad de bits necesarios para representar el número.

Por ejemplo, si tenemos el número 10, que se puede representar como 1010 en binario, la función bit_length() nos devolverá 4, 
ya que 4 bits son necesarios para representar el número 10 en binario.

Aquí hay un ejemplo de código que muestra cómo usar la función bit_length():

numero = 10
print(numero.bit_length()) # imprime 4

Esta función puede ser útil en situaciones donde necesitas determinar la cantidad de bits necesarios para almacenar un número entero 
en un determinado sistema o plataforma.
"""

# list.append() es un método que se utiliza para agregar un elemento al final de una lista existente. 
# Este método modifica la lista original y no devuelve ningún valor.
mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)  # imprime [1, 2, 3, 4]

#Es importante tener en cuenta que list.append() agrega solo un elemento a la lista. Si necesitas agregar varios elementos a la lista, 
#puedes usar el método extend() o la concatenación de listas.




#ist.pop() es un método que se utiliza para eliminar el último elemento de una lista y devolver ese elemento eliminado. 
# La sintaxis del método pop():
mi_lista.pop([indice])

#Donde lista es la lista de la que deseas eliminar el último elemento, y indice es un valor opcional que especifica 
# el índice del elemento que deseas eliminar. Si no se especifica el índice, se elimina el último elemento de la lista.
mi_lista = [1, 2, 3, 4]
elemento_eliminado = mi_lista.pop()
print(mi_lista)            # imprime [1, 2, 3]
print(elemento_eliminado)  # imprime 4




#list.extend() es un método que se utiliza para agregar los elementos de una lista (u otro objeto iterable) 
# al final de otra lista existente. Este método modifica la lista original y no devuelve ningún valor.
#  La sintaxis del método extend() es la siguiente:
mi_lista.extend(iterable)

#Donde lista es la lista a la que deseas agregar elementos, y iterable es cualquier objeto iterable que contenga 
# los elementos que deseas agregar.

#Aquí hay un ejemplo que muestra cómo utilizar el método extend() para agregar elementos de una lista a otra lista:
mi_lista1 = [1, 2, 3]
mi_lista2 = [4, 5, 6]
mi_lista1.extend(mi_lista2)
print(mi_lista1)  # imprime [1, 2, 3, 4, 5, 6]




 #"del" es una palabra clave que se utiliza para eliminar un objeto de la memoria, lo que incluye variables, listas,
 #  diccionarios y otros objetos. La sintaxis de del es la siguiente:
del objeto  #Donde objeto es el objeto que deseas eliminar de la memoria.

# Eliminar una variable
mi_variable = 10
del mi_variable

# Eliminar un elemento de una lista
mi_lista = [1, 2, 3]
del mi_lista[0] # para eliminar el primer elemento de la lista.

# Eliminar una clave de un diccionario
mi_diccionario = {"a": 1, "b": 2, "c": 3}
del mi_diccionario["a"] 



#¿Dónde cae la Tierra en el orden de los planetas? Podemos obtener su índice usando el método list.index.
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets.index('Earth') #2

#podemos usar el operador in para determinar si una lista contiene un valor en particular:
# Is Earth a planet?
"Earth" in planets #True

# Is Calbefraques a planet?
"Calbefraques" in planets #False



#tuplas
#Las tuplas son casi exactamente lo mismo que las listas. Se diferencian en sólo dos formas.

#1: La sintaxis para crearlos usa paréntesis en lugar de corchetes

t = (1, 2, 3)
t = 1, 2, 3 # equivalente al anterior
t #(1, 2, 3)

#2: No se pueden modificar (son inmutables).




# as_integer_ratio() es un método que se utiliza para convertir un número de punto flotante en una tupla de dos enteros 
# que representan su fracción equivalente en forma de fracción reducida. La sintaxis del método as_integer_ratio() es la siguiente:

numero.as_integer_ratio() #Donde "numero" es el número de punto flotante que deseas convertir.

#Aquí hay un ejemplo que muestra cómo utilizar el método as_integer_ratio() para convertir 
# un número de punto flotante en una fracción reducida:

numero = 2.75
fraccion = numero.as_integer_ratio()
print(fraccion)  # imprime (11, 4)

#En este ejemplo, se crea un número de punto flotante numero con el valor 2.75. Luego, se utiliza el método as_integer_ratio() 
# para convertir este número en una fracción reducida representada como una tupla de dos enteros. El resultado se almacena en 
# la variable fraccion y se imprime en la consola.

#Es importante tener en cuenta que el método as_integer_ratio() siempre devuelve una fracción en su forma reducida, 
# lo que significa que los dos enteros de la tupla están en su forma más simple. Además, si el número de punto flotante es negativo, 
# la tupla devuelta por el método as_integer_ratio() también contendrá un número negativo.




#bucles

#for
"""
Este código de Python crea una tupla llamada "multiplicands" que contiene seis números: tres 2's, dos 3's y un 5. Luego, el código calcula el producto de todos los números en la tupla usando un bucle "for" y una variable llamada "product".

Aquí está el paso a paso del código:

Primero, se define la tupla "multiplicands" con los números (2, 2, 2, 3, 3, 5).
Luego, se inicializa la variable "product" en 1. Esto es importante para asegurarse de que el primer número de la tupla se multiplique por 1.
A continuación, se inicia un bucle "for" que recorre cada elemento en la tupla "multiplicands". En cada iteración del bucle, el código multiplica el valor de "product" por el valor actual de "mult" (que es el valor actual de la tupla "multiplicands").
Después de que el bucle se ha completado, el valor de "product" será igual al producto de todos los números en la tupla "multiplicands".

En resumen, el código calcula el producto de los valores en la tupla "multiplicands" y devuelve el resultado en la variable "product". En este caso, el valor de "product" será 360, que es el resultado de multiplicar todos los números en la tupla.
"""


multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
product #2 x 2 x 2 x 3 x 3 x 5 = 360



"""
".isupper()" es un método en Python que se puede aplicar a una cadena (string) y devuelve un valor booleano (True o False) que 
indica si todos los caracteres en la cadena son mayúsculas (upper case) o no.

Por ejemplo, si tenemos una cadena llamada "texto" que contiene solo letras mayúsculas, entonces "texto.isupper()" devolverá True. 
Por otro lado, si la cadena "texto" contiene letras en minúscula o caracteres que no son letras, entonces "texto.isupper()" devolverá False.

Aquí hay un ejemplo:

cadena1 = "HOLA MUNDO"
cadena2 = "hola mundo"
cadena3 = "Hola Mundo"
cadena4 = "H0LA MUND0"

print(cadena1.isupper())   # True
print(cadena2.isupper())   # False
print(cadena3.isupper())   # False
print(cadena4.isupper())   # True
"""
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# imprime todas las letras mayúsculas en s, una a la vez
for char in s:
    if char.isupper():
        print(char, end='') #HELLO

#range()
#range() es una función que devuelve una secuencia de números. Resulta muy útil para escribir bucles.

#Por ejemplo, si queremos repetir alguna acción 5 veces:
for i in range(5):
    print("Doing important work. i =", i)

    """
    Doing important work. i = 0
    Doing important work. i = 1
    Doing important work. i = 2
    Doing important work. i = 3
    Doing important work. i = 4
    """




#while
i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # aumentar el valor de i en 1
    #0 1 2 3 4 5 6 7 8 9 

#El argumento del ciclo while se evalúa como una declaración booleana y el ciclo se ejecuta hasta que la declaración 
# se evalúa como Falsa.




#Lista de comprensiones
squares = [n**2 for n in range(10)]
squares # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Así es como haríamos lo mismo sin una lista de comprensión:
squares = []
for n in range(10):
    squares.append(n**2)
squares # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



short_planets = [planet for planet in planets if len(planet) < 6]
short_planets #['Venus', 'Earth', 'Mars']
"""
        Se define una nueva lista llamada "short_planets" usando la sintaxis de comprensión de listas. Esta línea de código crea una nueva lista a partir de los elementos de otra lista (en este caso, la lista "planets").
        
        El primer elemento en la comprensión de lista es "planet", que es una variable que representa cada elemento individual en la lista "planets".
        
        La condición "if len(planet) < 6" se evalúa para cada elemento en "planets". Esta condición verifica si la longitud de la cadena de caracteres "planet" es menor a 6. Si la condición es verdadera para un planeta, se agrega a la lista "short_planets". Si la condición es falsa, el planeta no se agrega a la lista.
        
        Después de que se completa la comprensión de la lista, el código devuelve la nueva lista "short_planets" que contiene solo los planetas cuyos nombres tienen una longitud menor a 6 caracteres.

        Por ejemplo, si la variable "planets" contiene los nombres de los planetas "Mercurio", "Venus", "Tierra", "Marte", "Júpiter", 
        "Saturno", "Urano" y "Neptuno", entonces la variable "short_planets" contendrá solo los nombres de los planetas "Venus" y "Marte", 
        ya que son los únicos planetas que cumplen con la condición de tener una longitud menor a 6 caracteres.
"""



loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6] #el código aplica la función "upper()" a cada planeta, lo que convierte todas las letras en mayúsculas.
loud_short_planets     #['VENUS!', 'EARTH!', 'MARS!']                                #Finalmente, se agrega un signo de exclamación al final de cada planeta en mayúsculas. 
#La comprensión de lista completa devuelve la nueva lista "loud_short_planets" que contiene los nombres de los planetas que tienen una longitud menor a 6 caracteres, en letras mayúsculas y con un signo de exclamación al final.



[32 for planet in planets] # El código crea una nueva lista que contiene el número 32 para cada planeta en la lista "planets".
                           #[32, 32, 32, 32, 32, 32, 32, 32]



#sintaxis de cadena
# las cadenas en Python se pueden definir usando comillas simples o dobles. Son funcionalmente equivalentes.
x = 'Pluto is a planet'
y = "Pluto is a planet"
x == y #True

print("Pluto's a planet!")          #Pluto's a planet!
print('My dog is named "Pluto"')    #My dog is named "Pluto"



"""
La siguiente tabla resume algunos usos importantes del carácter de barra invertida...

Lo que escribes...	Lo que obtienes 	ejemplo	                        print(ejemplo)
\'	                      '	            'What\'s up?'	                What's up?

\"	                      "	            "That's \"cool\""	            That's "cool"

\\	                      \	            "Look, a mountain: /\\"	        Look, a mountain: /\

\n	                                        "1\n2 3"	                        1
                                                                                2 3
"""



#La última secuencia, \n, representa el carácter de nueva línea. Hace que Python comience una nueva línea.
hello = "hello\nworld"
print(hello)
# hello
# wórld

#Además, la sintaxis de comillas triples de Python para cadenas nos permite incluir saltos de línea literalmente 
# (es decir, simplemente presionando 'Enter' en nuestro teclado, en lugar de usar la secuencia especial '\n').
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
# hello
# wórld
triplequoted_hello == hello  #True


# La función print() agrega automáticamente un carácter de nueva línea a menos que especifiquemos un valor para 
# el final del argumento de la palabra clave que no sea el valor predeterminado de '\n':
print("hello")  #hello
print("world")  #world
print("hello", end='')
print("pluto", end='')  #hellopluto



# Las cadenas son secuencias.
# Las cadenas se pueden considerar como secuencias de caracteres. Casi todo lo que hemos visto que podemos hacer 
# con una lista, también podemos hacerlo con una cadena.

planet = 'Pluto'
planet[0] #P    

planet[-3:] #uto

len(planet) #5 

[char+'! ' for char in planet] #['P! ', 'l! ', 'u! ', 't! ', 'o! ']

#Pero una forma importante en la que se diferencian de las listas es que son inmutables. No podemos modificarlos.


#métodos de cadena:
# TODO MAYÚSCULAS
claim = "Pluto is a planet!"
claim.upper()

# todo en minúsculas
claim.lower()

# Buscando el primer índice de una subcadena
claim.index('plan') #11

#startswith() es un método que se utiliza para comprobar si una cadena comienza con un prefijo especificado. 
cadena = "Hola, ¿cómo estás?"
resultado = cadena.startswith("Hola")
print(resultado)  # imprime True

# endswith() es un método que se utiliza para comprobar si una cadena termina con un sufijo especificado.
cadena = "Hola, ¿cómo estás?"
resultado = cadena.endswith("estás?")
print(resultado)  # imprime True



#Ir entre cadenas y listas: .split() y .join()
# str.split() convierte una cadena en una lista de cadenas más pequeñas, rompiendo en espacios en blanco de forma predeterminada. 
# Esto es muy útil para pasar de una cadena grande a una lista de palabras.
words = claim.split()
words # ['Pluto', 'is', 'a', 'planet!']

# Ocasionalmente, querrá dividirse en algo que no sea un espacio en blanco:
datestr = '1956-01-31'
year, month, day = datestr.split('-') 

 #str.join() nos lleva en la otra dirección, cosiendo una lista de cadenas en una cadena larga, 
 # usando la cadena a la que se llamó como separador.
'/'.join([month, day, year]) # '01/31/1956'

# Sí, podemos poner caracteres Unicode directamente en nuestras cadenas literales :)
'👏 '.join([word.upper() for word in words]) # 'PLUTO 👏 IS 👏 A 👏 PLANET!'



#Construyendo cadenas con .format()
#Python nos permite concatenar cadenas con el operador +.
planet + ', we miss you.' # 'Pluto, we miss you.'

# Si queremos incluir objetos que no sean cadenas, debemos tener cuidado de llamar a .str() primero.
position = 9
planet + ", you'll always be the " + position + "th planet to me." # Asi no es correcto

planet + ", you'll always be the " + str(position) + "th planet to me." # Asi si es correcto
#"Pluto, you'll always be the 9th planet to me."


# Ahora con str.format().
"{}, you'll always be the {}th planet to me.".format(planet, position)  # "Pluto, you'll always be the 9th planet to me."



#otro ejemplo del uso de format()
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)
#"Pluto weighs about 1.3e+22 kilograms (0.218% of Earth's mass). It is home to 52,910,390 Plutonians."




# Diccionarios
# Los diccionarios son una estructura de datos integrada de Python para asignar claves a valores.
numbers = {'one':1, 'two':2, 'three':3}

numbers['one'] # 1

#Podemos usar la misma sintaxis para agregar otra clave, par de valores
numbers['eleven'] = 11
numbers # {'one': 1, 'two': 2, 'three': 3, 'eleven': 11}


# O para cambiar el valor asociado con una clave existente
numbers['one'] = 'Pluto'
numbers # {'one': 'Pluto', 'two': 2, 'three': 3, 'eleven': 11}

#Python tiene comprensiones de diccionario con una sintaxis similar a las comprensiones de lista que vimos en el tutorial anterior.
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial
"""
        {'Mercury': 'M',
        'Venus': 'V',
        'Earth': 'E',
        'Mars': 'M',
        'Jupiter': 'J',
        'Saturn': 'S',
        'Uranus': 'U',
        'Neptune': 'N'}
"""

#El operador in nos dice si algo es una clave en el diccionario
'Saturn' in planet_to_initial #True

#Un bucle for sobre un diccionario hará un bucle sobre sus claves
for k in numbers:
    print("{} = {}".format(k, numbers[k]))

    """
    one = Pluto
    two = 2
    three = 3
    eleven = 11
    """

#Podemos acceder a una colección de todas las claves o todos los valores con dict.keys() y dict.values(), respectivamente.
## Obtenga todas las iniciales, ordénelas alfabéticamente y colóquelas en una cadena separada por espacios.
' '.join(sorted(planet_to_initial.values())) # 'E J M M N S U V'



#El muy útil método dict.items() nos permite iterar sobre las claves y valores de un diccionario simultáneamente. (En la jerga de Python, un elemento se refiere a un par clave-valor)

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
"""
   Mercury begins with "M"
     Venus begins with "V"
     Earth begins with "E"
      Mars begins with "M"
   Jupiter begins with "J"
    Saturn begins with "S"
    Uranus begins with "U"
   Neptune begins with "N"   
"""




#import
#math es un módulo. Un módulo es solo una colección de variables (un espacio de nombres, si lo desea) definida por otra persona. 
# Podemos ver todos los nombres en matemáticas usando la función integrada dir().
import math
"""
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod',
   'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 
   'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
"""

print("pi to 4 significant digits = {:.4}".format(math.pi)) #pi to 4 significant digits = 3.142

math.log(32, 2) # 5.0

#una forma de cortar el nombre del modulo
import math as mt

mt.pi #3.141592653589793

#¿No sería genial si pudiéramos referirnos a todas las variables en el módulo matemático por sí mismas? es decir, 
# ¿si pudiéramos referirnos a pi en lugar de math.pi o mt.pi? Buenas noticias: podemos hacer eso.
from math import *
print(pi, log(32, 2)) # 3.141592653589793  5.0
#Este tipo de "importaciones de estrellas" ocasionalmente pueden conducir a situaciones extrañas y difíciles de depurar.(Puede dar ERROR)


#Submódulos
#Hemos visto que los módulos contienen variables que pueden referirse a funciones o valores. 
# Algo a tener en cuenta es que también pueden tener variables que se refieran a otros módulos.
import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )
"""
        numpy.random is a <class 'module'>

        it contains names such as... ['seed', 'set_state', 'shuffle', 'standard_cauchy', 'standard_exponential', 
        'standard_gamma', 'standard_normal', 'standard_t', 'test', 'triangular', 'uniform', 'vonmises', 'wald', 
        'weibull', 'zipf']
"""

#Entonces, si importamos numpy como arriba, entonces llamar a una función en el "submódulo" 
# random requerirá dos puntos.
rolls = numpy.random.randint(low=1, high=6, size=10) #Tira 10 dados
rolls   # array([4, 2, 4, 5, 3, 1, 4, 2, 5, 1])



#Tres herramientas para entender objetos extraños
#1: type() (what is this thing?) (¿que es esta cosa?)
type(rolls) # numpy.ndarray

# 2: dir() (what can I do with it?) (¿Qué puedo hacer con él?)
print(dir(rolls))
"""
['T', '__abs__', '__add__', '__and__', '__array__', '__array_finalize__', '__array_function__', '__array_interface__', 
'__array_prepare__', '__array_priority__', '__array_struct__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', 
'__complex__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__divmod__', '__doc__', '__eq__', 
'__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', 
'__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__', '__init__', '__init_subclass__', '__int__', 
'__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', 
'__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', 
'__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmatmul__', 
'__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', 
'__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__xor__', 'all', 'any', 
'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base', 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 
'ctypes', 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill', 'flags', 'flat', 'flatten', 'getfield', 
'imag', 'item', 'itemset', 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 
'put', 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield', 'setflags', 'shape', 'size', 'sort', 
'squeeze', 'std', 'strides', 'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view']
"""

# Si quiero el rollo promedio, el método "promedio" parece prometedor...
rolls.mean() #3.1

## O tal vez solo quiero convertir la matriz en una lista, en cuyo caso puedo usar "tolist"
rolls.tolist() # [4, 2, 4, 5, 3, 1, 4, 2, 5, 1]

#3: help() (tell me more)
help(rolls)


#Sobrecarga de operadores
#¿Cuál es el valor de la siguiente expresión?
[3, 4, 1, 2, 2, 1] + 10 # ERROR
rolls + 10 # Asi si y da, array([14, 12, 14, 15, 13, 11, 14, 12, 15, 11])

# ¿En qué índices los dados son menores o iguales a 3?
rolls <= 3 # array([False,  True, False, False,  True,  True, False,  True, False, True])



xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array  ## Crear una matriz bidimensional
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))
"""
xlist = [[1, 2, 3], [2, 4, 6]]

x =
[[1 2 3]
 [2 4 6]]
"""

## Obtener el último elemento de la segunda fila de nuestra matriz numpy
x[1,-1] #6

# ¿Obtener el último elemento de la segunda sublista de nuestra lista anidada?
xlist[1,-1] #ERROR 


