from cinema import Cinema

class City(Cinema):
    @staticmethod
    def get_name():
        return "City"

    @staticmethod
    def get_seating_plan():
        return range(1, 12), "ABCDEGJK"
