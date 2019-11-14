class Tokenizer:
    "tokenizer text"

    def __init__(self,text):
        print("Tokenizer class __init__() methid is called")
        self.tokens = text.split()
        print("end of tokenizer __init__ method ")


class WordCount(Tokenizer):
    """ count the wordin text  """

    def __init__(self,text):
        print("start word count .__init__() method ")
        super().__init__(text)
        self.word_count = len(self.tokens)

        print("end ofword count __init__() method ")

class Vocabulary(Tokenizer):
    """find unique word in word count  """

    def __init__(self,text):
        print("start init of vocabulary.__init__()")
        super().__init__(text)
        self.vocab = set(self.tokens)
        print("end init vocabulary.__init__()")




class TextDescriber(Vocabulary,WordCount):
    def __init__(self,text):
        print("start of TextDescriber.__init__method")
        super().__init__(text)
        print("end init TextDescriber.__init__()")

td = TextDescriber('row row row your boat')
print('--------')
# print(td.tokens)
# print(td.vocab)
# print(td.word_count)
