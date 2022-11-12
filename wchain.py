class WChain:
    def __init__(self, file):
        self.file = file

    def _read_data(self):
        words = []
        with open(self.file, "r") as file:
            number_of_words = int(file.readline())
            for line in range(number_of_words):
                words.append(file.readline().strip())
        return words

    def count_chains(self):
        words = sorted(self._read_data(), key=len)
        word_chains = {word: 1 for word in words}
        word_chains_list = {word: [word] for word in words}
        for word in word_chains.keys():
            if len(word) == 1:
                continue
            for iterator in range(len(word)):
                word_to_check = word.replace(word[iterator], '', 1)
                if word_to_check in word_chains:
                    if word_chains[word_to_check] + 1 > word_chains[word]:
                        word_chains[word] = word_chains[word_to_check] + 1
                        word_chains_list[word] += word_chains_list[word_to_check]

        result_word_chain = max(word_chains.values())
        result_word_chain_list = list(word_chains.keys())[list(word_chains.values()).index(result_word_chain)]
        print(word_chains_list[result_word_chain_list])
        WChain._write_data(result_word_chain)
        return result_word_chain

    def _write_data(answer):
        with open("wchain.out", "w") as file:
            file.write(str(answer))


