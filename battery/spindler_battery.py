from battery import Battery
from datetime import datetime

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.date = datetime.fromtimestamp(datetime.timestamp(current_date) - datetime.timestamp(last_service_date), tz=None) #tz = timezone

    def needs_service(self) -> bool:
        return self.date.year >= 2