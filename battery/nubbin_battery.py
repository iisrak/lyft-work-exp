from battery import Battery
from datetime import datetime

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        last_time_stamp = datetime.timestamp(last_service_date)
        current_time_stamp = datetime.timestamp(current_date)

        self.date = datetime.fromtimestamp(current_time_stamp - last_time_stamp, tz=None) #tz = timezone

    def needs_service(self) -> bool:
        return self.date.year >= 4