import rospy
from geometry_msgs.msg import Twist

def talker():
    pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    rospy.init_node('talker',anonymous=True)
    rate=rospy.Rate(50)
    msg=Twist()
    while not rospy.is_shutdown():
        msg.linear.x=float(0.2)
        pub.publish(msg)
        rate.sleep()

if __name__ =='__main__':
    talker()
