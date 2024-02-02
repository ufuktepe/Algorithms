class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        """Returns true if the event can be added to the calendar successfully without causing a triple booking.
        Otherwise, return false and do not add the event to the calendar."""
        events = self.events[:]
        events.append([start, 1])
        events.append([end, -1])
        events.sort()

        count = 0
        for time, e_type in events:
            count += e_type
            if count >= 3:
                return False

        self.events = events

        return True


def test():
    sltn = MyCalendarTwo()
    bookings = [[1, 10], [2, 4], [4, 7]]
    for start, end in bookings:
        sltn.book(start, end)

    assert sltn.book(9, 10)
    assert sltn.book(2, 3) is False