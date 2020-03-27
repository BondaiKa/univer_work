# algorithm simple monoalphabet replacing

class Cipher:

    def __init__(self, A, K):
        self.A = A
        self.K = K
        self.alp = list(map(chr, range(97, 123)))
        self.might = 26

    def coding(self, string):
        result = []
        for x in string:
            item = self.alp.index(x)
            result.append(self.alp[(self.A * item + self.K) % self.might])
        return ''.join(result)

    def decoding(self, string):
        result = []
        for x in string:
            item = self.alp.index(x)
            result.append(self.alp[int(((self.A ** (-1))*(item - self.K))% self.might)])
        return ''.join(result)


if __name__ == "__main__":
    A = 7
    K = 3
    cipher = Cipher(A, K)
    string = input("Enter string to encrypt: ")

    after_coding = cipher.coding(string)
    print('After coding string: '+ after_coding)
    adter_decoding = cipher.decoding(after_coding)
    print('After decoding string: '+ adter_decoding)
