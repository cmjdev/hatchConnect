import babyconnect
import hatchbaby
import datetime
import secrets

bc = babyconnect.BabyConnect(secrets.bc["user"], secrets.bc["password"])
hb = hatchbaby.HatchBaby(secrets.hb["user"], secrets.hb["password"])


def parse_bctime(bctime):
    """
    Return a datetime object given Baby Connect timestamp
    """

    bctime = bctime.split()

    date = bctime[0].split("-")
    time = bctime[1].split(":")
    return datetime.datetime(
        int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1])
    )


def get_duration(bcstart, bcend):
    """
    Return duration in seconds given two Baby Connect timestamps
    """

    start = parse_bctime(bcstart)
    end = parse_bctime(bcend)

    delta = end - start

    return delta.total_seconds()


def get_tstring(bctime):
    """
    Return Hatch Baby timestamp given Baby Connect timestamp
    """

    return parse_bctime(bctime).strftime("%Y-%m-%d %H:%M:%S")


def do_bottle(row):
    """
    Returns Hatch Baby Response
    
    Given a bottle record from Baby Connect, build the payload for
    Hatch Baby and POST to the API
    """

    feeding = {
        "startTime": get_tstring(row[0]),
        "endTime": get_tstring(row[1]),
        "category": "Manual",
        "method": "Bottle",
        "source": "Breastmilk" if (row[5] == "Milk") else "Formula",
        "amount": float(row[4]) * 29.6,
        "durationInSeconds": get_duration(row[0], row[1]),
    }

    return hb.post_feeding(0, feeding)


def do_sleep(row):
    """
    Returns Hatch Baby API Response
    
    Given a sleep record from Baby Connect, build the payload for
    Hatch Baby and POST to the API
    """

    sleep = {
        "startTime": get_tstring(row[0]),
        "endTime": get_tstring(row[1]),
        "durationInSeconds": get_duration(row[0], row[1]),
    }

    return hb.post_sleep(0, sleep)


def do_diaper(row):
    """
    Returns Hatch Baby API Response
    
    Given a diaper record from Baby Connect, build the payload for
    Hatch Baby and POST to the API
    """

    diaper_type = row[5]

    if diaper_type == "BM":
        diaper_type = "Dirty"
    elif diaper_type == "BM+Wet":
        diaper_type = "Both"

    diaper = {"diaperType": diaper_type, "diaperDate": get_tstring(row[0])}

    return hb.post_diaper(0, diaper)


###

today = datetime.date.today().strftime("%m/%d/%Y")

bcdata = bc.get_csv(0, today)

for row in bcdata:
    activity = row[2]
    if activity == "Bottle":
        print(do_bottle(row))
    elif activity == "Sleep":
        print(do_sleep(row))
    elif activity == "Diaper":
        print(do_diaper(row))
