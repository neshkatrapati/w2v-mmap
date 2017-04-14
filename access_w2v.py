import sys
from w2vmmap import * 

trie_file = sys.argv[1]
source_file = sys.argv[2]
index_file = sys.argv[3]
token = sys.argv[4]

with W2VMMap(source_file, index_file, trie_file) as w2m:
    print w2m.get_word(token)
