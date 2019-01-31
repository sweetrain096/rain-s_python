def fee(minute, distance):
    result = 0

    result += (minute // 10) * 1200
    if minute % 30:
        result += ((minute // 30) + 1) * 525
    else:
        result += (minute // 30) * 525

    if distance > 100:
        result += 100 * 170 + (distance - 100) * 85
    else:
        result += distance * 170

    return result




print(fee(600, 50))
print(fee(600, 110))
