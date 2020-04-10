from collections import Counter


class OpenTextHadnler:
    """
    work text (analyze ,get statistic of char and etc...
    """

    def __init__(self, path):
        self._path = path
        self._text = open(path).read()
        self._len_text = len(self._text)
        self._list_count = Counter(self._text)
        self._list_percentage = [(x, y/self._len_text)
                                 for x, y in self._list_count.most_common()]
        # self._array_percent = np.asarray([x[1] for x in self._list_percentage])

    def find_nearest_char(self, percent):
        nearest_index = 0
        for index, _tuple in enumerate(self._list_percentage):
            current = abs(_tuple[1]-percent)
            less = abs(self._list_percentage[nearest_index][1]-percent)
            if current < less:
                nearest_index = index
        return self._list_percentage.pop(nearest_index)[0]


class DecodeText(OpenTextHadnler):
    """
    work with encode text, works woth same responsibilities
    and decode encoding text using open text
    """

    def __init__(self, path):
        super().__init__(path)
        self._dict_translate = {}
        self._list_char = list(self._text)

    def decode(self, open_instance):
        self._dict_translate = {}
        for _tuple in self._list_percentage:
            char = open_instance.find_nearest_char(_tuple[1])
            self._dict_translate[_tuple[0]] = char

    def save(self):
        for index in range(self._len_text):
            self._list_char[index] = self._dict_translate[self._text[index]]

    def __str__(self):
        return ''.join(self._list_char)


if __name__ == "__main__":
    open_instance = OpenTextHadnler(
        'protection_of_information/lab_5/Open_text_utf_8.txt')
    encode_instance = DecodeText(
        'protection_of_information/lab_5/encrypt7_utf_8.txt')
    encode_instance.decode(open_instance)
    encode_instance.save()
    print(encode_instance)
