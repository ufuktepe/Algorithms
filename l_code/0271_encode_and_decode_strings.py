class Codec:
    # Let n be the number of strings in strs and k be the max length of the strings
    # Time: O(n*k)  Space: O(n*k)
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        lengths = []
        for str in strs:
            lengths.append(len(str))

        res = []

        for str_len, str in zip(lengths, strs):
            res.append(self.get_formatted_str_len(str_len))
            res.append(str)

        return ''.join(res)

    def get_formatted_str_len(self, str_len):
        if str_len < 10:
            return f'00{str_len}'
        elif str_len < 100:
            return f'0{str_len}'
        return f'{str_len}'

    def get_str_len(self, s, i):
        return int(s[i:i + 3])

    # Time: O(n*k)  Space: O(n*k)
    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0

        while i < len(s):
            str_len = self.get_str_len(s, i)
            i += 3
            res.append(s[i:i + str_len])
            i += str_len

        return res


def test():
    codec = Codec()
    strs = ['abc', 'def', 'xyz']
    encoded_str = codec.encode(strs)
    assert codec.decode(encoded_str) == strs