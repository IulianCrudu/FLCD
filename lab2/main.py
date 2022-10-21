from collections import deque


class SymbolTable:
    def __init__(self, m=31):
        self.m = m
        self.index = 0
        self.hash_table = [deque() for _ in range(self.m)]

    def _hash(self, element):
        ascii_sum = 0
        for c in element:
            ascii_sum += ord(c)

        return ascii_sum % self.m

    def add_element(self, element):
        existing_element_position = self.search_element(element)

        if existing_element_position != -1:
            return existing_element_position

        hash_value = self._hash(element)
        self.hash_table[hash_value].append((element, self.index))
        self.index += 1
        return self.index - 1

    def search_element(self, element) -> int:
        hash_value = self._hash(element)

        for el, position in self.hash_table[hash_value]:
            if el == element:
                return position

        return -1


if __name__ == '__main__':
    st = SymbolTable()

    st.add_element("a")
    print(st.add_element("a"))
    st.add_element("qwerty")
    print(st.add_element("qwerty"))

