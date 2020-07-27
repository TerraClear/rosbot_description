rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: "base_link"}, pose: {position: {x: 1.1, y: 2.1, z: 0.0}, orientation: {w: 1.0}}}'
