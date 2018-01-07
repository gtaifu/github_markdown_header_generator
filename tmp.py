class header():
    def __init__(self, content='', level=-1, is_virtual=False):
        self.is_virtual = is_virtual  # vritual header is used for the section title which directly starts from higher levels.
        self.header_title = content
        self.my_level = level    # level starts from 0.
        self.my_order = 0
        self.child_headers = []

    def assign_order(self):
        order = 1
        for header in child_headers:
            header.my_order = order++
            header.assign_order()

    def add_child_header(self, new_section_header):
        self.child_headers.append(new_section_header)

    def absorb(self, new_header):
#         print("new_header: ", new_header.my_level, new_header.header_title)
        if new_header.my_level <= self.my_level:
            raise ValueError("The new header has a higher level ({}) than the current level({}).".format(new_header.my_level, self.my_level))

        if new_header.my_level == self.my_level + 1:
            self.child_headers.append(new_header)
        else:
            if len(self.child_headers) == 0:
                self.child_headers.append(header('', self.my_level + 1, True))

            self.child_headers[-1].absorb(new_header)

#         print("Print after absorbing.")
#         self.print_headers()

    def get_level_symbol(self, sym):
        if not isinstance(sym, str):
            raise ValueError("Given symbol format ({}) not correct, which must be a string.".format(sym))

        return  sym * self.my_level

    def print_headers(self, print_level=False, order_info=''):
        if self.my_level == -1:
            new_order_info = ''
        elif self.my_level == 0:
            new_order_info = str(self.my_order)
        else:
            new_order_info = order_info + '.' + str(self.my_order)

        if not self.is_virtual and self.my_level != -1:
            print("{} {} {}".format(self.get_level_symbol(' '), new_order_info, self.header_title))

        for child_header in self.child_headers:
            child_header.print_headers(print_level, new_order_info)
