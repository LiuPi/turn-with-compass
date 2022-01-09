def direction(facing, turn):
    points = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    
    if not (facing in points):
        return 'Irrelevant facing parameter!'
    if (turn % 45 > 0):
        return 'Irrelevant turn parameter!'

    index = points.index(facing)
    position = (index + int(turn / 45)) % len(points)

    return points[position]
