import math


def trans(x):
    x = math.fabs(x)
    degrees = int(x)
    minutes = int((x - degrees) * 60)
    seconds = int((x - degrees) * 3600 - minutes * 60)
    return '%s°%.5s′%.5s″' % (degrees, minutes, seconds)


def trans2(x, y):
    return trans(x) + ',' + trans(y)


if __name__ == '__main__':
    print(trans2(41.880994471, -87.632746489))
