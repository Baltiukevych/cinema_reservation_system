class Movie:
    def __init__(self, movie_number, cinema):
        self.movie_number = movie_number
        self.cinema = cinema

        rows, letter = self.cinema.get_seating_plan()
        self.seats = [None] + [{seat: None for seat in letter} for _ in rows]

    def get_number(self):
        return self.movie_number[2:]

    def get_cinema_plan(self):
        return self.cinema.get_name()

    def _parse_seat(self, seat="7D"):
        rows, letters = self.cinema.get_seating_plan()

        letter = seat[-1]

        if letter not in letters:
            raise ValueError(f"Invalid seat letter {letter}")
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat number {row_text}")
        if row not in rows:
            raise ValueError(f"Row {row} is out of range")

        return row, letter

    def allocate_client(self, client="Arek S.", seat="7D"):
        row, letter = self._parse_seat(seat)

        if self.seats[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already occupied.")

        self.seats[row][letter] = client

    def relocate_client(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)
        row_to, letter_to = self._parse_seat(seat_to)

        if self.seats[row_to][letter_to] is not None:
            raise ValueError(f'Seat {seat_to} is already occupied.')

        self.seats[row_to][letter_to] = self.seats[row_from][letter_from]
        self.seats[row_from][letter_from] = None

    def count_empty_seats(self):
        return sum([sum([1 for seat in row.values() if seat is None])
                    for row in self.seats
                    if row is not None])

    def print_card(self, printer):
        clients = self.get_clients()

        for client, seat in clients:
            printer(client, seat, self.movie_number, self.get_cinema_plan())

    def get_clients(self):
        clients = []

        rows, seats = self.cinema.get_seating_plan()
        for row in rows:
            for seat in seats:
                client = self.seats[row][seat]
                if client is not None:
                    clients.append((client, f"{row}{seat}"))
        return clients
