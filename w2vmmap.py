import marisa_trie
from indexer import Indexer
import os

class W2VMMap(object):
    def __init__(self,
                 source_file,
                 index_file = None,
                 trie_file = None):
        self.source_file = source_file
        if not index_file:
            index_file = self.source_file + ".idx"
        if not trie_file:
            trie_file = self.source_file + ".trie"
                
        self.index_file = index_file
        self.trie_file = trie_file



        
    def make_index(self):
        idxr = Indexer(self.source_file, self.index_file)
        idxr.make_index()

        self.make_trie()

    def make_trie(self):
        key_file = self.source_file + '.kidx'
        trie_file = self.trie_file
    
        if os.path.exists(self.trie_file):
            os.remove(self.trie_file)


        if os.path.exists(key_file):
            os.remove(key_file)
        
        with open(self.source_file) as f ,open(key_file,'a') as t:
            for index, line in enumerate(f):
                token = line.split('\t')
                t.write(token[0] + ';' + str(index) + "\n")
            
        os.system('marisa-build {key_file} > {trie_file}'.format(**locals()))



        
        
    def __enter__(self):
        self.trie = marisa_trie.Trie().mmap(self.trie_file)
        return self
    
    def __exit__(self, type, value, traceback):
        pass

        
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

        
