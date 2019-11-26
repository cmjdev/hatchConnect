import requests, json


class Init:
    def __init__(self, u, p):

        path = '/public/v1/login'
        payload = {'email': u, 'password': p}

        self.user = self.Post(path, payload)

    def Get(self, e):

        url = f"https://data.hatchbaby.com{e}"

        headers = {
            'x-redhen-auth': self.user['token'],
            'User-Agent': 'hatch-connect',
            'Accept': '*/*',
            'Cache-Control': 'no-cache',
            'Host': 'data.hatchbaby.com',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

        response = requests.request('GET', url, headers=headers)

        return json.loads(response.text)

    def Post(self, e, p):

        url = f"https://data.hatchbaby.com{e}"

        payload = json.dumps(p)

        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'hatch-connect',
            'Accept': '*/*',
            'Cache-Control': 'no-cache',
            'Host': 'data.hatchbaby.com',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

        if hasattr(self, 'user'):
            headers['x-redhen-auth'] = self.user['token']

        response = requests.request('POST', url, data=payload, headers=headers)

        return json.loads(response.text)

    def GetUserInfo(self):

        path = '/service/app/refresh/v1/extendedMemberData'

        return self.Get(path)

    def GetLengths(self, b):

        path = f"/service/app/length/v1/fetch/{self.user['payload']['babies'][b]['id']}"

        return self.Get(path)

    def GetFeedings(self, b):

        path = f"/service/app/feeding/v1/fetch/{self.user['payload']['babies'][b]['id']}"

        return self.Get(path)

    def GetWeights(self, b):

        path = f"/service/app/weight/v1/fetch/{self.user['payload']['babies'][b]['id']}"

        return self.Get(path)

    def GetDiapers(self, b):

        path = f"/service/app/diaper/v1/fetch/{self.user['payload']['babies'][b]['id']}"

        return self.Get(path)

    def GetSleep(self, b):

        path = f"/service/app/sleep/v1/fetch/{self.user['payload']['babies'][b]['id']}"

        return self.Get(path)

    def GetStats(self, b):

        path = f"/service/app/stats/v1/fetch/{self.user['payload']['babies'][b]['id']}"

        return self.Get(path)

    def GetAdvice(self, b):

        path = f"/service/app/advice/v1/fetch/{self.user['payload']['babies'][b]['id']}"

        return self.Get(path)

    def GetPumpings(self):

        path = "/service/app/pumping/v2/fetch/"

        return self.Get(path)

    def GetAll(self, b):
        # TODO: This can and should be limited by datetime in the URL..
        path = f"/service/app/refresh/v1/fetch/{self.user['payload']['babies'][b]['id']}"

        return self.Get(path)

    def GetQuestions(self, b):

        path = f"/service/app/question/v1/fetch/{self.user['payload']['babies'][b]['id']}"

        return self.Get(path)

    def PostLength(self, b, p):

        path = "/service/app/length/v1/create/"

        p['babyId'] = self.user['payload']['babies'][b]['id']

        return self.Post(path, p)

    def PostFeeding(self, b, p):

        path = "/service/app/feeding/v1/create/"
        
        p['babyId'] = self.user['payload']['babies'][b]['id']

        return self.Post(path, p)

    def PostWeight(self, b, p):

        path = "/service/app/weight/v1/create/"

        p['babyId'] = self.user['payload']['babies'][b]['id']

        return self.Post(path, p)

    def PostDiaper(self, b, p):

        path = "/service/app/diaper/v1/create/"

        p['babyId'] = self.user['payload']['babies'][b]['id']

        return self.Post(path, p)

    def PostSleep(self, b, p):

        path = "/service/app/sleep/v1/create/"

        p['babyId'] = self.user['payload']['babies'][b]['id']

        return self.Post(path, p)
