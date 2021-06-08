def loadMap(mapPath):
    mapFile = open(mapPath + ".txt","r")
    data = mapFile.read()
    dataArray = data.split("\n")
    mapArray = []
    for item in dataArray:
        itemarray = []
        for piece in item:
            piece = int(piece)
            itemarray.append(piece)
        mapArray.append(itemarray)

    return mapArray



