### **clases y objetos**

Python es un lenguaje orientado a objetos.

un objeto es una representación de una entidad de la vida en nuestro programa.

para crear un objeto primero necesitamos crear una clase o plantilla

una clase representa las características en común de nuestros objetos. es una abstracción.

##### **Elementos de una clase**

Una clase se compone de atributos y métodos.

* Los atributos son las características de nuestros objetos.
* Los métodos son las acciones que pueden realizar nuestros objetos. en si, estas acciones son funciones, pero cuando se le asocian con una clase se les llama métodos.



Una vez que hemos definido nuestra clase, podemos crear objetos, a esto se le llama instanciar una clase.



ejemplo:

***clase:persona***

**atributos:**

* nombre
* apellido
* email
* celular

**métodos:**

* agregarpersona()
* mostrarpersona()



de la clase se desprenden o se crean objetos por ejemplo



*objeto 1*				*objeto 2*

nombre=Layla				nombre=Ian

apellido=acosta				apellido=Sanchez

 	.					.

 	.					.

 	.					.







### Constructores en Python



Un constructor es un método especial y se utiliza para crear un objeto, o instanciar una clase

Ademas nos puede servir para crear e inicializar los atributos de un nuevo objeto





\#sintaxis de un constructor

class NombreDeClase:

 	def \_\_init\_\_(self,parametro1,parametro2):

 		self.parametro1 = parametro1

 		self.parametro2 = parametro2

