files = ['dj38.txt', 'qa194.txt', 'wi29.txt']


allData = {}


for name in files:

    coordinates = []

    file = open(name)

    for line in file:
        if line[0].isdigit():
            temp = line.split()
            coordinates.append((float(temp[1]), float(temp[2])))
    allData.update({name: coordinates})



