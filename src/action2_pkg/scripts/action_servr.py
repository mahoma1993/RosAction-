#! /usr/bin/env python3
# EL objetivo de este nodo es recibir un contador inicial que es provisto por el nodo en el archivo action actual,
# sumar de a uno  hasta llegar a un objeitvo que es provisto por el action client
# y luego terminar el proceso

import rospy
import actionlib
from action2_pkg.msg import demoAction,demoFeedback,demoResult
from  std_msgs.msg import Int32
# defino la clase que vuelve del main
class actionserver():
    def __init__(self) -> None:
        self.a_server=actionlib.SimpleActionServer("demo_as",demoAction, self.execute_cb) # creo mi server, nombre mensaje y callback
        self.robot_point_sub = rospy.Subscriber("contador_inicial", Int32, self.actualizar_estado_inicial)  #  me subscribo al nodo del cual traere los valores iniciales

        self.contador_actual=0 # contador actual el que se va a ir sumando igual a 0 

        self.bandera=0 # bandera que sirve para subscrimirme una sola vez 
        
        self.feedback_rate = rospy.Rate(1) ## el rate del servidor
        


    def execute_cb (self,goal):

        contador_objetivo=goal.count

        
        # mientras no tengo mis valores iniciales espero 
        while self.contador_actual == 0:
                print("no se inicio aun el contador")
                rospy.sleep(5)


        print ("se detecto el contador") # inicio una vez que ya estan mis vlaores iniciales 

        while self.contador_actual < contador_objetivo:
            self.a_server.publish_feedback(demoFeedback(current_number = self.contador_actual)) # le doy un feedback al client para que vea en que estado estoy
            self.feedback_rate.sleep() # espero con el rate para seguir sumando 
            print ("el contador actual es" + str (self.contador_actual)) 
            self.contador_actual = self.contador_actual+1 


        final_count=self.contador_actual  

        rospy.loginfo("Navigation Successful, llego al objetivo")

        self.a_server.set_succeeded(demoResult(final_count))  # finalizo mi programa

    def actualizar_estado_inicial(self, point):
       
        #print ("actualizando")
        if (self.bandera == 0):
            print ("entre")
            self.contador_actual = point.data
            self.bandera=1
        else:
            pass
        



if __name__ == "__main__":
    rospy.init_node("action_server_node")
    s=actionserver()
    rospy.spin()


