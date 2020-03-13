# algorithm simple monoalphabet replacing

class Cipher:

    def __init__(self, A, K):
        self.A = A
        self.K = K

    def coding(self, string):
        result = []
        for x in string:
            item = ord(x)
            result.append(chr(65 + self.A * (item - 65) + self.K))

        return ''.join(result)

    def decoding(self, string):
        result = []
        for x in string:
            item = ord(x)
            result.append(chr(int(65 + self.A ** (-1) * (item - 65 - self.K))))
        return ''.join(result)


if __name__ == "__main__":
    A = 7
    K = 3
    cipher = Cipher(A, K)
    string = input("Enter string to encrypt")

    after_coding = cipher.coding(string)
    print('After coding string: '+ after_coding)
    adter_decoding = cipher.decoding(after_coding)
    print('After decoding string: '+ adter_decoding)
