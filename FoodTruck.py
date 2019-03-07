import requests
from datetime import datetime

from ApplicationConfiguration import Configuration
from QueryBuilder import QueryBuilder


class FoodTruck:
    '''Simple Class to hold Foodtruck Object'''

    def __init__(self, name, address):
        self.name = name
        self.address = address

    @classmethod
    def createFromJson(cls, jsonObj):
        if not jsonObj:
            return None
        return cls(jsonObj['applicant'], jsonObj['location'])

    def __str__(self):
        return f'Name: {self.name} Address: {self.address}'


class FoodTruckController:
    '''Class defines Simple service layer which exposes API 
    to get open food trucks'''

    def __init__(self):
        self._queryBuilder = QueryBuilder()
        self.config = Configuration()

    def getCurrentOpenFoodTrucks(self, pageNum=0):
        """API for fetching currently open foodtrucks

        @param pageNum: Page number (int)
        @returns: List of open foodtrucks (list)

        """
        date = datetime.now()
        return self.getOpenFoodTrucks(date, pageNum)

    def getOpenFoodTrucks(self, date, pageNum=0):
        """API for fetching foodtrucks open at given date

        @param date: date (datetime.date)
        @param pageNum: Page number (int)
        @returns: List of open foodtrucks (list)
        """
        clauses = []
        time24 = date.strftime("%H:%M")
        dayofweek = date.isoweekday()
        clauses.append(self._queryBuilder.buildSelectClause(
            ['applicant', 'location']))
        clauses.append(self._queryBuilder.buildWhereClause(
            [f'start24<"{time24}"', f'end24>"{time24}"', f'dayorder={dayofweek}']))
        clauses.append(self._queryBuilder.buildOrderByClause('applicant'))
        clauses.append(self._queryBuilder.buildLimitClause(
            self.config.getRecordsPerPage()))
        clauses.append(self._queryBuilder.buildOffsetClause(
            pageNum * self.config.getRecordsPerPage()))

        queryUrl = f'{self.config.getApiServer()}?{"&".join(clauses)}'
        data = self._executeQuery(queryUrl)
        foodtrucks = self._parseFoodTruckData(data)
        return foodtrucks

    # Utility Functions
    def _executeQuery(self, query):
        """Executes query and return the data

        @param query: String representing the query to be executed (str)
        @returns: List of Json Objects (list)

        """
        res = requests.get(query)

        if(res.status_code == 200):
            data = res.json()
        else:
            data = None
        return data

    def _parseFoodTruckData(self, data):
        """Parse Json data from API request to Foodtruck objects

        @param data: List of Json data from API request(list)
        @returns: List of Foodtrucks (list)

        """
        foodtrucks = []
        for foodtruck in data:
            foodtrucks.append(FoodTruck.createFromJson(foodtruck))
        return foodtrucks
