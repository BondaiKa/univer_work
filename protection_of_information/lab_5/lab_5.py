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


class EncodeText(OpenTextHadnler):
    """
    work with encode text, works woth same responsibilities
    and decode encoding text using open text
    """

    def __init__(self, path):
        super().__init__(path)
        self._dict_translate = {}
        self._list_char = list(self._text)

    def translate(self, open_instance):
        self._dict_translate = {}
        for open_list, encode_list in zip(open_instance._list_percentage, self._list_percentage):
            self._dict_translate[encode_list[0]] = open_list[0]
        # print(self._list_percentage)
        # print('---------------------')
        # print(open_instance._list_percentage)

    def save(self):
        for index in range(self._len_text):
            self._list_char[index] = self._dict_translate[self._text[index]]

    def __str__(self):
        return ''.join(self._list_char)


if __name__ == "__main__":
    open_instance = OpenTextHadnler('protection_of_information/lab_5/Open_text_utf_8.txt')
    encode_instance = EncodeText('protection_of_information/lab_5/encrypt7_utf_8.txt')
    encode_instance.translate(open_instance)
    encode_instance.save()
    # print(encode_instance)
