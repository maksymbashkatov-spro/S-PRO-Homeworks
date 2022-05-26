class ReverseIter:
    def __init__(self, my_list):
        """
        el_idx: индекс элемента.
        """
        self.my_list = my_list
        self.el_idx = len(my_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.el_idx >= 0:
            next_el = self.my_list[self.el_idx]
            self.el_idx -= 1
            return next_el
        else:
            raise StopIteration


rev_it = ReverseIter([1, 2, 3, 4, 5])

while True:
    try:
        print(next(rev_it))
    except StopIteration:
        break
