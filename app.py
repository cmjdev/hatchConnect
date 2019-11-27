import babyConnect, hatchBaby, datetime, secrets

bc = babyConnect.Init(secrets.bc['user'], secrets.bc['password'])
hb = hatchBaby.Init(secrets.hb['user'], secrets.hb['password'])

def parseTime(t):

    t = t.split()

    date = t[0].split("-")
    time = t[1].split(":")
    return datetime.datetime(
        int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1])
    )


def getDuration(s, e):

    start = parseTime(s)
    end = parseTime(e)

    delta = end - start

    return delta.total_seconds()


def getTimeString(t):

    return parseTime(t).strftime("%Y-%m-%d %H:%M:%S")


def doBottle(row):

    feeding = {
        "startTime": getTimeString(row[0]),
        "endTime": getTimeString(row[1]),
        "category": "Manual",
        "method": "Bottle",
        "source": "Breastmilk" if (row[5] == "Milk") else "Formula",
        "amount": float(row[4]) * 29.6,
        "durationInSeconds": getDuration(row[0], row[1])
    }

    return hb.PostFeeding(0, feeding)


def doSleep(row):
    sleep = {
        "startTime": getTimeString(row[0]),
        "endTime": getTimeString(row[1]),
        "durationInSeconds": getDuration(row[0], row[1]),
    }

    return hb.PostSleep(0, sleep)


def doDiaper(row):

    d = row[5]

    if d == "BM":
        d = "Dirty"
    elif d == "BM+Wet":
        d = "Both"

    diaper = {"diaperType": d, "diaperDate": getTimeString(row[0])}

    return hb.PostDiaper(0, diaper)


###

today = datetime.date.today().strftime("%m/%d/%Y")

bcdata = bc.GetCsv(0, today)

for row in bcdata:
    activity = row[2]
    if activity == "Bottle":
        print(doBottle(row))
    elif activity == "Sleep":
        print(doSleep(row))
    elif activity == "Diaper":
        print(doDiaper(row))
