"""
Hatch Baby API Class

Get and Post data to Hatch Baby API
"""

import requests, json


class HatchBaby:
    def __init__(self, email, password):
        """
        Instantiates Hatch Baby instance given email and password strings
        """

        path = "/public/v1/login"
        payload = {"email": email, "password": password}

        self.user = self._post(path, payload)

    def _get(self, path):

        url = f"https://data.hatchbaby.com{path}"

        headers = {
            "x-redhen-auth": self.user["token"],
            "User-Agent": "hatch-connect",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Host": "data.hatchbaby.com",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        }

        response = requests.request("GET", url, headers=headers)

        return json.loads(response.text)

    def _post(self, path, payload):

        url = f"https://data.hatchbaby.com{path}"

        payload = json.dumps(payload)

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "hatch-connect",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Host": "data.hatchbaby.com",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        }

        if hasattr(self, "user"):
            headers["x-redhen-auth"] = self.user["token"]

        response = requests.request("POST", url, data=payload, headers=headers)

        return json.loads(response.text)

    def get_user_info(self):
        """
        Return an extra bit of user information not stored in the
        authentication response
        """

        path = "/service/app/refresh/v1/extendedMemberData"

        return self._get(path)

    def get_lengths(self, baby_id):
        """
        Returns Hatch Baby API response with all lengths given baby_id
        """

        path = f"/service/app/length/v1/fetch/{self.user['payload']['babies'][baby_id]['id']}"

        return self._get(path)

    def get_feedings(self, baby_id):
        """
        Returns Hatch Baby API response with all feedings given baby_id
        """

        path = f"/service/app/feeding/v1/fetch/{self.user['payload']['babies'][baby_id]['id']}"

        return self._get(path)

    def get_weights(self, baby_id):
        """
        Returns Hatch Baby API response with all weights given baby_id
        """

        path = f"/service/app/weight/v1/fetch/{self.user['payload']['babies'][baby_id]['id']}"

        return self._get(path)

    def get_diapers(self, baby_id):
        """
        Returns Hatch Baby API response with all diapers given baby_id
        """

        path = f"/service/app/diaper/v1/fetch/{self.user['payload']['babies'][baby_id]['id']}"

        return self._get(path)

    def get_sleep(self, baby_id):
        """
        Returns Hatch Baby API response with all sleeps given baby_id
        """

        path = f"/service/app/sleep/v1/fetch/{self.user['payload']['babies'][baby_id]['id']}"

        return self._get(path)

    def get_stats(self, baby_id):
        """
        Returns Hatch Baby API response with stats given baby_id
        """

        path = f"/service/app/stats/v1/fetch/{self.user['payload']['babies'][baby_id]['id']}"

        return self._get(path)

    def get_advice(self, baby_id):
        """
        Returns Hatch Baby API Response.. No idea what this actually is
        """

        path = f"/service/app/advice/v1/fetch/{self.user['payload']['babies'][baby_id]['id']}"

        return self._get(path)

    def get_pumpings(self):
        """
        Returns Hatch Baby API response with all pumpings given baby_id
        """

        path = "/service/app/pumping/v2/fetch/"

        return self._get(path)

    def get_all(self, baby_id):
        """
        Returns Hatch Baby API response with all records given baby_id
        """

        # TODO: This can and should be limited by datetime in the endpoint..

        path = f"/service/app/refresh/v1/fetch/{self.user['payload']['babies'][baby_id]['id']}"

        return self._get(path)

    def get_questions(self, baby_id):
        """
        Returns Hatch Baby API Response.. No idea what this actually is
        """

        path = f"/service/app/question/v1/fetch/{self.user['payload']['babies'][baby_id]['id']}"

        return self._get(path)

    def post_length(self, baby_id, payload):
        """
        Returns Hatch Baby API Response

        Example payload:
        {
            "length": 61.000, # cm
            "measurementDate": "2019-11-25",
            "details": None # string
        }
        """

        path = "/service/app/length/v1/create/"

        payload["babyId"] = self.user["payload"]["babies"][baby_id]["id"]

        return self._post(path, payload)

    def post_feeding(self, baby_id, payload):
        """
        Returns Hatch Baby API Response

        Example payload:
        {
        "manualEntry": True,
        "amount": 388.000, # mL
        "startTime": "2019-11-24 09:30:00",
        "endTime": "2019-11-24 10:00:00",
        "details": None, # string
        "durationInSeconds": 1800,
        "category": "Manual",
        "method": "Bottle",
        "source": "Formula", # or Breastmilk
        }

        For nursing:
        "method": "Nursing"
        "source": "Both" # or Left, Right, Both_Ending_Left/Right
        "durationLeft": 600, # seconds
        "durationRight": 600, # seconds
        """

        path = "/service/app/feeding/v1/create/"

        payload["babyId"] = self.user["payload"]["babies"][baby_id]["id"]

        return self._post(path, payload)

    def post_weight(self, baby_id, payload):
        """
        Returns Hatch Baby API Response

        Example payload:
        {
        "manualEntry": True,
        "weight": 3000, # g
        "measurementTime": "2019-11-25 09:00:00",
        "details": None, # or string
        "category": "Manual",
      }
        """

        path = "/service/app/weight/v1/create/"

        payload["babyId"] = self.user["payload"]["babies"][baby_id]["id"]

        return self._post(path, payload)

    def post_diaper(self, baby_id, payload):
        """
        Returns Hatch Baby API Response

        Example Payload:
        {
        "diaperType": "Wet", # Dirty or Both
        "diaperDate": "2019-11-25 10:00:00",
        "category": "Manual",
        "details": None, # string
        }
        """

        path = "/service/app/diaper/v1/create/"

        payload["babyId"] = self.user["payload"]["babies"][baby_id]["id"]

        return self._post(path, payload)

    def post_sleep(self, baby_id, payload):
        """
        Returns Hatch Baby API Response

        Example Payload:
        {
        "startTime": "2019-11-25 14:00:00",
        "endTime": "2019-11-25 15:00:00",
        "durationInSeconds": 3600,
        "details": None, # string
        }
        """

        path = "/service/app/sleep/v1/create/"

        payload["babyId"] = self.user["payload"]["babies"][baby_id]["id"]

        return self._post(path, payload)
