#! /usr/bin/env python 

import rospy

from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    
    # 720 / 5 = 144
    regiones = {
        'frente_izquierda': min(min(msg.ranges[0:44]),3),
        'izquierda_frente': min(min(msg.ranges[45:89]),3),
        'izquierda_atras': min(min(msg.ranges[90:134],3)),
        'atras_izquierda': min(min(msg.ranges[135:179]),3),
        'atras_derecha': min(min(msg.ranges[180:224]),3),
        'derecha_atras': min(min(msg.ranges[225:269]),3),
        'derecha_frente': min(min(msg.ranges[270:314]),3),
        'frente_derecha': min(min(msg.ranges[315:360]),3),
    }
    rospy.loginfo(regiones)

def movimientos(regiones):
    msg = Twist()
    linear_x = 0
    angular_z = 0

    if (regiones['frente_izquierda']) and (regiones['izquierda_frente']) and (regiones['izquierda_atras']) and (regiones['atras_izquierda']) and (regiones['atras_derecha']) and (regiones['derecha_atras']) and (regiones['derecha_frente']) and (regiones['frente_derecha']) :
        #mandar instruccion 


    elif (regiones['frente_izquierda']) and (regiones['izquierda_frente']) and (regiones['izquierda_atras']) and (regiones['atras_izquierda']) and (regiones['atras_derecha']) and (regiones['derecha_atras']) and (regiones['derecha_frente']) and (regiones['frente_derecha']) :
        #mandar instruccion 


    elif (regiones['frente_izquierda']) and (regiones['izquierda_frente']) and (regiones['izquierda_atras']) and (regiones['atras_izquierda']) and (regiones['atras_derecha']) and (regiones['derecha_atras']) and (regiones['derecha_frente']) and (regiones['frente_derecha']) :
        #mandar instruccion


    elif (regiones['frente_izquierda']) and (regiones['izquierda_frente']) and (regiones['izquierda_atras']) and (regiones['atras_izquierda']) and (regiones['atras_derecha']) and (regiones['derecha_atras']) and (regiones['derecha_frente']) and (regiones['frente_derecha']) :
        #mandar instruccion 


    elif (regiones['frente_izquierda']) and (regiones['izquierda_frente']) and (regiones['izquierda_atras']) and (regiones['atras_izquierda']) and (regiones['atras_derecha']) and (regiones['derecha_atras']) and (regiones['derecha_frente']) and (regiones['frente_derecha']) :
        #mandar instruccion 
            

def main():
    rospy.init_node('reading_laser')

    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)
    rospy.spin()

if __name__ == '__main__':
    main()
