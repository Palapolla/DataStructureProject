import datetime
import json
from package import BST

"""
Room data
    Deluxe = D01, D02, D03, D04, D05
    Normal = N01, N02, N03, N04, N05
    Twin = T01, T02, T03, T04, T05
"""


def findAvailableRoom(roomType, checkInDate, checkOutDate):
    # <class 'str'> <class 'datetime.date'> <class 'datetime.date'>
    avarilableroom = []
    handleError = ""
    dif = checkOutDate - checkInDate
    if dif.days < 1:
        handleError = "Wrongs date input!"
        return handleError, avarilableroom

    # trans data to check
    dateTimeCheckin = datetime.datetime.combine(
        checkInDate, datetime.datetime.min.time())

    # example dataOffset = ['2021-12-02', '2021-12-03', '2021-12-04', '2021-12-05']
    dataOffset = []
    for i in range(dif.days):
        dt = dateTimeCheckin+datetime.timedelta(days=i)
        dataOffset.append(str(dt.date()))

    with open("data.json") as f:
        data = json.load(f)

    for room in data:
        if room != "LastID":
            if data[room]["type"] == roomType:

                myTree = BST()

                for item in data[room]["dateBooking"]:
                    myTree.insert(dateToInt(item))

                isAppend = True
                for date in dataOffset:
                    if myTree.search(dateToInt(date)):
                        isAppend = False

                if isAppend:
                    avarilableroom.append(room)

    return handleError, avarilableroom


def writeData(name, surname, tel, roomType, roomID, dateIn, dateOut):
    # handle error
    if name == "":
        return "please Enter Name"
    if surname == "":
        return "please Enter Surname"
    if len(tel) != 10:
        return "Phone number must have 10 digits"
    if roomID == "\"Not selected\"":
        return "please select room ID"
    if roomType[0] != roomID[0]:
        return "Room type and Room ID not match\nPlease select room ID again"

    # prepare data
    dic = {
        "Name": name,
        "Surname": surname,
        "tel": tel,
        "roomType": roomType,
        "roomID": roomID,
        "dateIn": str(dateIn),
        "dateOut": str(dateOut)
    }

    writeDateData = []
    amountDay = dateOut - dateIn
    for i in range(amountDay.days):
        baseDt = datetime.datetime.combine(
            dateIn, datetime.datetime.min.time())
        dt = baseDt+datetime.timedelta(days=i)
        writeDateData.append(str(dt.date()))

    # check avarilableroom before append
    with open("data.json") as f:
        data = json.load(f)
    temp = data[roomID]["dateBooking"]
    for date in writeDateData:
        if date in temp:
            return "This room has been booked in this date\nplease select new date"

    data["LastID"] += 1
    lastID = data["LastID"]
    dic["id"] = lastID
    data[roomID]["bookingData"].append(dic)
    for i in writeDateData:
        data[roomID]["dateBooking"].append(i)

    # write
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

    return "Booking successful"


def dateToInt(dateStr):
    dateStr = dateStr.split("-")
    s = ''.join(dateStr)
    return int(s)


def intToDate(dateInt):
    temp = str(dateInt)
    data = temp[0:4]+"-" + temp[4:6]+"-" + temp[6:]
    return data

# a, b = findAvailableRoom("Deluxe", datetime.date(
#     2021, 12, 2), datetime.date(2021, 12, 6))
