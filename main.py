class RabinKarp:
    def __init__(self, base: int = 10, mod: int = 13):
        self.base = base
        self.mod = mod

    def to_hash(self, str_to_hash: str):
        str_len = len(str_to_hash)
        hash_result = 0
        for i in range(str_len):
            # hash_result = (hash_result + ord(str_to_hash[i]) * (self.base ** (str_len - i - 1))) % self.mod
            hash_result = (self.base * hash_result + ord(str_to_hash[i])) % self.mod
        return hash_result

    def shift_substring(self, substring_hash: int, first_char_transformer: int, first_symbol: str, next_symbol: str):
        substring_hash = ((substring_hash - ord(first_symbol) * first_char_transformer) * self.base
                          + ord(next_symbol)) % self.mod
        if substring_hash < 0:
            substring_hash = substring_hash + self.mod
        return substring_hash

    def create_first_char_transformer(self, pattern_len: int):
        transformer = 1
        for i in range(pattern_len - 1):
            transformer = (transformer * self.base) % self.mod
        return transformer

    def find(self, pattern: str, text: str):
        str_len = len(text)
        pattern_len = len(pattern)
        first_char_transformer = self.create_first_char_transformer(pattern_len)
        pattern_hash = self.to_hash(pattern)
        substring_hash = self.to_hash(text[0:pattern_len])
        found_pos = []
        j = 0
        for i in range(str_len - pattern_len + 1):
            if pattern_hash == substring_hash:
                for j in range(pattern_len):
                    if text[i + j] == pattern[j]:
                        j += 1
                    else:
                        break
                if j == pattern_len:
                    found_pos.append(i)
            if i != str_len - pattern_len:
                substring_hash = self.shift_substring(substring_hash, first_char_transformer,
                                                      text[i], text[i + pattern_len])
        return found_pos


if __name__ == '__main__':
    rabin_karp = RabinKarp(256, 1000)
    result = rabin_karp.find("cab", "abccabbcabaccbaacbabc")
    print(result)
