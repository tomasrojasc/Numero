El objeto ``Numero`` permite una manera fácil de calcular errores después de las 4 principales operaciones básicas:
* suma
* resta
* multiplicación
* división

Para crear un número se tiene que inicializar un objeto como sigue:

```python
n = Numero(valor, error)
```
las instancias de ``Numero`` pueden operarse de manera sencilla como sigue

```python
a = Numero(10, 0.001)
b = Numero(5, 0.05)

print(a + b)
print(a - b)
print(a / b)
print(a * b)


>>> 15 ± 0.05000999900019996
>>> 5 ± 0.05000999900019996
>>> 2.0 ± 0.02000099997500125
>>> 50 ± 0.5000249993750312
```

también es posible operar instanias de ``Numero`` con instancias de ``int`` y de ``float``, en cuyo caso se asumirá que ese número tiene error 0

Además los objetos ``Numero`` tienen un parámetro llamado ``decimals`` que por defecto es ``None`` dejando así imprimir tantos decimales como haya disponibles al llamar a su representación. Este parámetro tiene que ser entero y puede setearse luego de la creación del objeto seteando un valor entero al atributo en cuestión.
