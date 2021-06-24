## Archivos de prueba
* *encoder* contiene una serie de programas con los cuales se puede probar el funcionamiento de los encoder, donde solo se deben cambiar los pines de entrada de ser necesario.
* *Motores* contiene codigos para la prueba solo de los motores, donde se deben ajustar los pines en caso de ser necesario.

### Lista de Pines utilizados

> Para el driver l298n :

```cpp	
ENA = 9;
IN1 = 8;
IN2 = 7;
IN3 = 6;
IN4 = 5;
ENB = 4;
```
> Para los encoder y motor :
``` 
Cable verde (GND) = GND arduino
Cable azul (Vcc) = 5v arduino
Cable Amarillo = A0 arduino
Cable Blanco = A1 arduino
```

