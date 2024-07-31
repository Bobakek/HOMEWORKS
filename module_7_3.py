class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().split()  # Разбивка на слова
                all_words[file_name] = words

        return all_words

    def find(self, search_word):
        word_positions = {}
        for file_name, words in self.get_all_words().items():
            positions = [index + 1 for index, word in enumerate(words) if word.lower() == search_word.lower()]
            if positions:
                word_positions[file_name] = positions
        return word_positions

    def count(self, search_word):
        word_count = {}
        for file_name, words in self.get_all_words().items():
            count = sum(1 for word in words if word.lower() == search_word.lower())
            word_count[file_name] = count
        return word_count


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # Позиции слова "TEXT"
print(finder2.count('teXT'))  # Количество слова "teXT" в файле






