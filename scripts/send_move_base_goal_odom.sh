rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: "odom"}, pose: {position: {x: 1.1, y: 1.1, z: 0}, orientation: {x: 0.0, y: 0.0, z: 0.94, w: 0.33}}}'
