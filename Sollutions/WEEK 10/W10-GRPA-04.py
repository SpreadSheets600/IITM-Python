class Time:
    def __init__(self, time: int):
        self.time = time

    def seconds_to_minutes(self) -> str:
        minutes = self.time // 60
        seconds = self.time % 60
        return f"{minutes} min {seconds} sec"

    def seconds_to_hours(self) -> str:
        hours = self.time // 3600
        remaining_seconds = self.time % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{hours} hrs {minutes} min {seconds} sec"

    def seconds_to_days(self) -> str:
        days = self.time // 86400
        remaining_seconds = self.time % 86400
        hours = remaining_seconds // 3600
        remaining_seconds %= 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{days} days {hours} hrs {minutes} min {seconds} sec"