import marisa_trie
from indexer import Indexer

class W2VMMap(object):
    def __init__(self,
                 source_file,
                 index_file,
                 trie_file):
        self.source_file = source_file
        self.index_file = index_file
        trie = marisa_trie.Trie().mmap(trie_file)

    def token_to_line(self, token):
        items = self.trie.items(unicode(token+';'))
        if len(items) == 1:
            item = items[0][0]
            line_num = item.split(';')[1]
        return int(line_num)
        

    def get_line(self, line_num):
        idxr = Indexer(self.source_file, self.index_file)
        line = None
        with idxr as i:
            line =  i.read(line_num)
        return line

    def get_word(self, word):
        return self.get_line(self.token_to_line(word))

        
