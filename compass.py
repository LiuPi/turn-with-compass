def direction(facing, turn):
    points = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    
    if facing not in points:
        return 'Invalid direction parameter!'
    if turn % 45 > 0:
        return 'Invalid turn parameter!'

    index = points.index(facing)
    position = (index + int(turn / 45)) % len(points)

    return points[position]
