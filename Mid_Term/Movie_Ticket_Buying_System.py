class Star_Cinema:

    hall_list = []

    def entry_hall(self, h):
        self.hall_list.append(h)


class Hall(Star_Cinema):

    def __init__(self, __rows, __cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.__rows = __rows
        self.__cols = __cols
        self.hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, __id, movie_name, _time):
        self.show_list.append(tuple([__id, movie_name, _time]))
        lst = [[0] * self.__cols for _ in range(self.__rows + 1)]
        self.seats[__id] = lst

    def book_seat(self, __id, seat_no):
        if __id < len(self.show_list):
            print(self.show_list[__id])
        if seat_no[0] < 0 or seat_no[0] >= self.__rows or seat_no[1] < 0 or seat_no[1] >= self.__cols:
            print('Invalid seat')
            return
        if __id in self.seats:
            if self.seats[__id][seat_no[0]][seat_no[1]] == 0:
                self.seats[__id][seat_no[0]][seat_no[1]] = 1
                print(f'Successfully booked seat at : {seat_no[0] + 1, seat_no[1] + 1}')
            else:
                print('This seat has already booked !')
        else:
            print('Sorry this movie not available !')

    def view_show_list(self):
        for show in self.show_list:
            print(show)

    def view_available_seats(self, __id):
        if __id < len(self.show_list):
            print(self.show_list[__id])
        if __id in self.seats:
            for i in range(self.__rows):
                for j in range(self.__cols):
                    print(self.seats[__id][i][j], end=' ')
                print()
        else:
            print('Sorry this movie not available !')


h1 = Hall(10, 5, 111)
h1.entry_show(len(h1.show_list), 'Hubba', 'DATE : 25/02/24 TIME : 12:30 PM')
h1.entry_show(len(h1.show_list), 'Shurongo', 'DATE : 25/02/24 TIME : 8:30 PM')
'''h2 = Hall(10, 5, 112)
h2.entry_show(1, 'Vikigs', 'DATE : 25/02/24 TIME : 12:30 PM')
h2.entry_show(2, 'Pk', 'DATE : 25/02/24 TIME : 8:30 PM')'''

while True:
    typ = int(input('1. VIEW ALL SHOW TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. EXIT\n'))
    if typ == 1:
        h1.view_show_list()
    elif typ == 2:
        s = int(input('Provide Movie ID Please : '))
        h1.view_available_seats(s)
    elif typ == 3:
        m_id, x, y = map(int, input('Provide Movie ID and Seat No : ').split())
        x -= 1
        y -= 1
        h1.book_seat(m_id, tuple([x, y]))
    else:
        break




