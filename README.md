# Repositorio de proyecto Robot-Autonomo
### Desarrollo del proyecto
### Paso 1: 
#### Instalar ROS en raspberry :
> Actualmente el sistema operativo de Raspberry es Raspbian, que esta basado en la ultima versión de Debian (en este caso Debian 10), por lo que trabaje con este para que fuera mas sencillo todo.
> la version de ROS que corresponde a Debian 10 y a ubuntu 18.04 es ROS melodic.
>>*para la instalación segui los pasos del siguiente link :https://www.instructables.com/ROS-Melodic-on-Raspberry-Pi-4-RPLIDAR/ *
>> ahi fue donde tuve mis primeras imagenes con ROS y el sensor Lidar.

### Paso 2:
#### Instalar Arduino en Raspi :
> Puesto que para este proyecto Arduino sera el encargado de controlar los motores y Raspberry solo será el cerebro, debemos instalar el IDE de Arduino en Raspberry, para esto debemos primero saber que propiedades cumple nuestra raspi.
>Instalamos el comando :
``` bash
$ sudo apt install lshw
```
y luego ejecutamos 
``` bash
$ lshw
```
> con esto sabremos si necesitamos la version ARM o no, y si necesitaremos la version de 32 o 64 bits. 
> > *En mi caso tengo la version de 32 bits ARM*
#### Instalar rosserial en raspberry :
> Debemos entrar al directorio de ros, en mi caso: 
``` bash
$ cd catkin_ws
```
Luego debemos clonar el directorio de rosserial en la carpeta src :
``` bash
$ cd src
```
``` bash
$ git clone https://github.com/ros-drivers/rosserial.git
```
Finalmente instalar todo :
``` bash
$ cd ..
```
``` bash
$ catkin_make
```
``` bash
$ catkin_make install
```
#### Probar la conexion de Raspberry con Arduino :

Para probar la conexion debemos correr en la terminal :
``` bash
$ roscore
```
En otra terminal correr :
``` bash
$ rosrun rosserial_python serial_node.py /dev/ttyACM0
```
Finalmente, para ver la informacion que envia Arduino a raspberry :
``` bash
$ rostopic echo chatter
```
>>> *En caso de tener algun error relacionado a " import queue ", la solucion esta en este link https://answers.ros.org/question/362043/importerror-no-module-named-queue/ *

## Compartir informacion para visualizar desde Computador externo :
#### En Ubuntu 18.04 :
>> correr :
 ``` bash
 $ roscore
 ```
 ``` bash
 $ export ROS_MASTER_URI=http://[your-desktop-machine-ip]:11311
 ```
  >> y en la raspi correr de manera paralela :
 ``` bash
 $ export ROS_MASTER_URI=http://[your-desktop-machine-ip]:11311
 ```
 ``` bash
 $ export ROS_IP=[la ip de la raspi]
 ```
 >>*Esto lo debemos hacer cata vez que vamos a correr algun programa de ros que queramos visualizar en la computadora externa*

## Paso 4 : 
#### Integrar SLAM :
>> Yo segui el siguiente tutorial : https://github.com/NickL77/RPLidar_Hector_SLAM

## Paso 5 :
#### Movimiento remoto + Arduino :

> Utilizando el sistema de ROS , haremos que la raspberry (Master) , se conecte con el nodo de Arduino (/cmd_vel), y asi la raspi funcione como un cerebor, mientras que Arduino solo se utilizara como controlador de motores y en un futuro de los diferentes sensores.
> > por ahora solo utilizaremos los motores.
> > * Para comenzar debemos subir el programa a Arduino, en mi caso el programa se llama `cmd_vel_01.ino`, en este se encuentra la conexion a los motores y encoders.
> > * Luego debemos hacer que la raspi se conecte con estos para poder hacer que los motores se muevan bajo nuestro control. Para esto utilizaremos el comando 
> > `rosrun rosserial_python serial_node.py /dev/ttyACM0`, *con el cual nos conectamos al nodo de arduino que esta conectado a travez de la entrada USB, (/dev/ttyACM0).*
> > En otra terminal debemos correr el comando 
> > `rosrun teleop_twist_keyboard teleop_twist_keyboard.py` *para habilitar el control del robot por teclado.*
> > * Con esto ya podremos controlar nuestro robot con los comandos que apareceran por consola.
> > > *Para esto no se utilizo codigo propio, solo las siguientes librerias:*
> > > * **








