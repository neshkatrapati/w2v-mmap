import sys
import marisa_trie
from indexer import Indexer


marisa_file = sys.argv[1]
source_file = sys.argv[2]
index_file = sys.argv[3]
token = sys.argv[4]

trie = marisa_trie.Trie().mmap(marisa_file)



def token_to_line(trie, token):
#    token = token.encode('UTF-8')
#    print token
    items = trie.items(unicode(token+';'))
    if len(items) == 1:
        item = items[0][0]
        line_num = item.split(';')[1]
        return int(line_num)
        

def get_line(source_file, index_file, line_num):
    idxr = Indexer(source_file, index_file)
    line = None
    with idxr as i:
        line =  i.read(line_num)
    return line


        
line_num = token_to_line(trie, token)    
print get_line(source_file, index_file, line_num)
