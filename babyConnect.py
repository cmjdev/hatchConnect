import requests, re, json, csv

class Init:

    def __init__(self, u, p):
        url = "https://www.babyconnect.com/Cmd"
        querystring = {"cmd": "UserAuth", "email": u, "pass": p}
        headers = {
            "User-Agent": "hatch-connect",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate",
            "Referer": f"https://www.babyconnect.com/Cmd?cmd=UserAuth&email={u}&pass={p}",
            "Connection": "keep-alive",
        }
        response = requests.request("POST", url, headers=headers, params=querystring)
        rawUser = re.search("var _x.*myKids.*;", response.text).group()
        user = json.loads(re.sub("var _x = |;", "", rawUser))
        user["auth"] = dict(response.cookies).popitem()
        self.user = user

    def GetCsv(self, b, d):

        url = "https://www.babyconnect.com/GetCmd"
        querystring = {
            "cmd": "StatusExport",
            "kid": self.user["myKids"][b]["Id"],
            "exportType": "2",
                   "dt": d,
        }       
        headers = {
            "User-Agent": "hatch-connect",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Host": "www.babyconnect.com",
            "Accept-Encoding": "gzip, deflate",
            "Cookie": f"{self.user['auth'][0]}={self.user['auth'][1]}",
            "Connection": "keep-alive",
        }       
        response = requests.request("GET", url, headers=headers, params=querystring) 

        return [row for row in csv.reader(response.text.splitlines(), delimiter=",")]
