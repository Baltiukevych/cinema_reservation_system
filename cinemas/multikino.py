from cinema import Cinema

class Multikino(Cinema):
    @staticmethod
    def get_name():
        return "Multikino"

    @staticmethod
    def get_seating_plan():
        return range(1, 24), "ABCDEG"
