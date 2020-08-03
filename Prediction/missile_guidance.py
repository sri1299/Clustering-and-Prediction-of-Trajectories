from vectors import Vector

preds # np array with shape (100, 30, 3)




g = 9.8

max_acc = 30
cur_velocity = Vector.from_list([0, 0 ,0])
cur_pos = Vector.from_list([0, 0, 0])

for i in preds:
  tar_cur_pos = Vector.from_list([i[0][0], i[0][1], i[0][2]])
  dist_from_target = tar_cur_pos.add(cur_pos.multiply(-1))
  if dist_from_target.magnitude < 5:
    print ('(', cur_pos.x, cur_pos.y, cur_pos.z, '),(', tar_cur_pos.x, tar_cur_pos.y, tar_cur_pos.z, ')')
    break

  for ts, j in enumerate(i):
    ts += 1
    tar_new_pos = Vector.from_list([j[0], j[1], j[2]])
    diff = tar_new_pos - cur_pos

    acc_x = 2 * ((diff.x / ts) - (cur_velocity * ts))
    acc_y = 2 * ((diff.y / ts) - (cur_velocity * ts))
    acc_z = g + 2 * ((diff.z / ts) - (cur_velocity * ts))
    req_acc = Vector.from_list([acc_x, acc_y, acc_z])
    if ts == 30 or (acc_x < 30 and acc_y < 30 and acc_z < 30):
      new_velocity = cur_velocity.add(req_acc)
      dx = (new_velocity.x ** 2 - cur_velocity.x ** 2)  / (2 * acc_x)
      dy = (new_velocity.y ** 2 - cur_velocity.y ** 2)  / (2 * acc_y)
      dz = (new_velocity.z ** 2 - cur_velocity.z ** 2)  / (2 * acc_z)
      cur_pos = cur_pos.add(Vector.from_list(dx, dy, dz))
      break

  print ('(', cur_pos.x, cur_pos.y, cur_pos.z, '),(', tar_cur_pos.x, tar_cur_pos.y, tar_cur_pos.z, ')')


  