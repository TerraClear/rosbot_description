#!/usr/bin/env python

import rospy
# Because of transformations
import tf_conversions
import tf2_ros
import tf2_msgs.msg
import geometry_msgs.msg

class TFRebroadcaster:

    def __init__(self):
        self.broadcaster = tf2_ros.TransformBroadcaster()
        self.t_fl = geometry_msgs.msg.TransformStamped()
        self.t_fr = geometry_msgs.msg.TransformStamped()
        self.t_rl = geometry_msgs.msg.TransformStamped()
        self.t_rr = geometry_msgs.msg.TransformStamped()

        self.tfmsg = tf2_msgs.msg.TFMessage()
        self.sub = rospy.Subscriber('/tf_gazebo', tf2_msgs.msg.TFMessage, self.cb)
        self.pub_tf = rospy.Publisher("/tf", tf2_msgs.msg.TFMessage, queue_size=1)
    """
    def cb(self, msg):
        for tf in msg.transforms:
            if tf.child_frame_id =="front_left_wheel" or tf.child_frame_id =="front_right_wheel" or tf.child_frame_id=="rear_left_wheel" or tf.child_frame_id=="rear_right_wheel":
                self.t.header.stamp = rospy.Time.now()
                self.t.header.frame_id = msg.header.frame_id
                self.t.child_frame_id = msg.child_frame_id
                self.t.transform = msg.transform




                self.broadcaster.sendTransform(self.t)
    """

    def cb(self, msg):
        for tf in msg.transforms:
            if tf.child_frame_id =="front_left_wheel":
                self.t_fl.header.stamp = rospy.Time.now()
                self.t_fl.header.frame_id = tf.header.frame_id
                self.t_fl.child_frame_id = tf.child_frame_id
                self.t_fl.transform = tf.transform

            if tf.child_frame_id =="front_right_wheel":
                self.t_fr.header.stamp = rospy.Time.now()
                self.t_fr.header.frame_id = tf.header.frame_id
                self.t_fr.child_frame_id = tf.child_frame_id
                self.t_fr.transform = tf.transform

            if tf.child_frame_id=="rear_left_wheel":
                self.t_rl.header.stamp = rospy.Time.now()
                self.t_rl.header.frame_id = tf.header.frame_id
                self.t_rl.child_frame_id = tf.child_frame_id
                self.t_rl.transform = tf.transform

            if tf.child_frame_id=="rear_right_wheel":
                self.t_rr.header.stamp = rospy.Time.now()
                self.t_rr.header.frame_id = tf.header.frame_id
                self.t_rr.child_frame_id = tf.child_frame_id
                self.t_rr.transform = tf.transform


        tfmsg = tf2_msgs.msg.TFMessage([self.t_fl, self.t_fr, self.t_rl, self.t_rr])
        self.pub_tf.publish(tfmsg)

    def run(self):
        rospy.init_node('tf_rebroadcaster')
        rospy.spin()
if __name__ =='__main__':
     tfr = TFRebroadcaster()
     tfr.run()
