"""
Baby Connect hack to get records... Class
"""

import requests
import re
import json
import csv


class BabyConnect:
    def __init__(self, email: str, password: str):
        """
        Instantiates Baby Connect instance given email and password strings
        """
        url = "https://www.babyconnect.com/Cmd"
        querystring = {"cmd": "UserAuth", "email": email, "pass": password}
        headers = {
            "User-Agent": "hatch-connect",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate",
            "Referer": f"https://www.babyconnect.com/Cmd?cmd=UserAuth&email={email}&pass={password}",
            "Connection": "keep-alive",
        }
        response = requests.request("POST", url, headers=headers, params=querystring)
        rawUser = re.search("var _x.*myKids.*;", response.text).group()
        user = json.loads(re.sub("var _x = |;", "", rawUser))
        user["auth"] = dict(response.cookies).popitem()
        self.user = user

    def get_csv(self, baby_id: int, date):
        """
        Return an array of Baby Connect records

        Given a baby ID and start date will return an array of rows
        that exist between the date and the server time that
        this method was called
        """

        url = "https://www.babyconnect.com/GetCmd"
        querystring = {
            "cmd": "StatusExport",
            "kid": self.user["myKids"][baby_id]["Id"],
            "exportType": "2",
            "dt": date,
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
