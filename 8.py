class MorseMsg:
    '''
    class of a message in Morse code
    '''
    def __init__(self, message):
        self.message = message
        self.letters = self.message.split()

    def eng_decode(self):
        '''
        function that decodes message to english
        :return: letters in english
        '''
        eng_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..'}
        message_decoded = ''
        for word in self.letters:
            for key, value in eng_code.items():
                if value == word:
                    message_decoded += key + ' '
        return message_decoded

    def ru_decode(self):
        '''
        function that decodes message to russian
        :return: letters in russian
        '''
        ru_code = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-',
                   'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
                   'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
                   'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
                   'Ю': '..--', 'Я': '.-.-'}
        message_decoded = ''
        for word in self.letters:
            for key, value in ru_code.items():
                if value == word:
                    message_decoded += key + ' '
        return message_decoded

    def get_vowels(self, lang):
        '''
        function that returns vowels from the message
        :param lang: language of the message
        :return: vowels
        '''
        vowels = []
        if lang == 'eng':
            eng_vowels = ['A', 'E', 'I', 'O', 'U']
            message_decoded = self.eng_decode()
            for letter in message_decoded:
                if letter in eng_vowels:
                    vowels.append(letter)
        elif lang == 'ru':
            ru_vowels = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
            message_decoded = self.eng_decode()
            for letter in message_decoded:
                if letter in ru_vowels:
                    vowels.append(letter)
        return vowels

    def get_consonants(self, lang):
        '''
        function that returns consonants from the message
        :param lang: language of the message
        :return: consonants
        '''
        consonants = []
        if lang == 'eng':
            eng_vowels = ['A', 'E', 'I', 'O', 'U']
            message_decoded = self.eng_decode()
            for letter in message_decoded:
                if letter not in eng_vowels:
                    consonants.append(letter)
        elif lang == 'ru':
            ru_not_cns = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я', 'Ь', 'Ъ']
            message_decoded = self.eng_decode()
            for letter in message_decoded:
                if letter not in ru_not_cns:
                    consonants.append(letter)
        return consonants
