from datetime import datetime


class Train():
    def __init__(self, data):
        self.destination = data.get('DESTINATION')
        self.direction = data.get('DIRECTION')
        self.event_time = data.get('EVENT_TIME')
        self.line = data.get('LINE')
        self.next_arrival_time = data.get('NEXT_ARR')
        self.station = data.get('STATION').title()
        self.train_id = data.get('TRAIN_ID')
        self.waiting_seconds = data.get('WAITING_SECONDS')
        self.waiting_time = data.get('WAITING_TIME')

        self.direction_dict = {
            'E': 'Eastbound',
            'N': 'Northbound',
            'S': 'Southbound',
            'W': 'Westbound'
        }

        self.str_format_not_arrived = 'The next {} line train headed for {} will arrive to {} in {}'
        self.str_format_arriving = 'The {} line train headed for {} is now arriving to {}'
        self.str_format_boarding = 'The {} line train headed for {} is now boarding at {}'

    def extract_time(self, time_to_extract):
        return datetime.strptime(time_to_extract,
                                 '%I:%M:%S %p').strftime('%I:%M %p')

    def get_event_time(self):
        time_only = self.event_time[self.event_time.index(' ') + 1:]
        return self.extract_time(time_only)

    def get_next_arrival_time(self):
        return self.extract_time(self.next_arrival_time)

    def get_direction(self):
        return self.direction_dict.get(self.direction)

    def __str__(self):
        if self.waiting_time.lower() == 'arriving':
            return self.str_format_arriving.format(self.line, self.destination, self.station)
        elif self.waiting_time.lower() == 'boarding':
            return self.str_format_boarding.format(self.line, self.destination, self.station)
        else:
            return self.str_format_not_arrived.format(self.line, self.destination, self.station, self.waiting_time)
