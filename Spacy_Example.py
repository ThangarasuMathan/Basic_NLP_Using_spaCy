import spacy,en_core_web_sm
from spacy.matcher import Matcher
SpacyPath = r'E:\en_core_web_sm\en_core_web_sm-2.2.0'
nlp = en_core_web_sm.load() 
matcher = Matcher(nlp.vocab)
doc = nlp("A.P.J. Abdul Kalam was an Indian aerospace scientist and politician who served as the 11th President of India from 2002 to 2007.")

#*******************************************************************************************************
# Tokenization
#*******************************************************************************************************
doc.text.split()


sample_token=doc.text.split()

for token in sample_token:
    print (token)
    
for token in sample_token:
    if 'scientist' in token:
        print (token)    

#*******************************************************************************************************
# Part-of-speech tagging (POS-Tagging)
#*******************************************************************************************************        

for token in doc:
    print(token.text,token.pos_, '\n')
    
    if 'NUM' in  token.pos_:
        print(token.pos_,':',token.text)   
        
        
#*******************************************************************************************************
# Named Entity Recognition(NER)
#*******************************************************************************************************         
        
for ent in doc.ents:
    print(ent.text,ent.label_)        
    if 'DATE' in ent.label_:
        print(ent.label_,':',ent.text)
        
#*******************************************************************************************************
# Spacy Pharse Matcher
#*******************************************************************************************************             
matcher = Matcher(nlp.vocab)
# Add match ID "HelloWorld" with no callback and one pattern
pattern = [{"LOWER": "from"},{"SHAPE": "dddd"}, {"LOWER": "to"},{"SHAPE": "dddd"}]
matcher.add("FROM", None, pattern)
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(span.text)   
 