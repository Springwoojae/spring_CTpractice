def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    ops = int(op_start[:2])*60 + int(op_start[3:])
    ope = int(op_end[:2])*60 + int(op_end[3:])
    now_pos = int(pos[:2])*60 + int(pos[3:])
    vid_len = int(video_len[:2])*60 + int(video_len[3:])
    if ops <= now_pos and now_pos <= ope:
        now_pos = ope
    for command in commands:
        if command == "next":
            now_pos += 10
        else:
            now_pos -= 10
        if now_pos > vid_len:
            now_pos = vid_len
        if now_pos < 0:
            now_pos = 0
        if ops <= now_pos and now_pos <= ope:
            now_pos = ope
    mm = now_pos // 60
    ss = now_pos % 60
    if mm < 10:
        answer = '0' + str(mm)
    else:
        answer = str(mm)
    if ss < 10:
        answer += ':0' + str(ss)
    else:
        answer += ":" + str(ss)
    return answer