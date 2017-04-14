import sys
from w2vmmap import * 


source_file = sys.argv[1]
w2m = W2VMMap(source_file)
    
w2m.make_index()            
            
