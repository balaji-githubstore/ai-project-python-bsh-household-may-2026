"""example to generate sentence vector
 pip install sentence-transformers                                                                                                                                                                       
"""

from sentence_transformers import SentenceTransformer


sentences=["apple is good for health","avoid eating junk foods like fried rice"]

model=SentenceTransformer("all-MiniLM-L6-v2")
embeddings= model.encode(sentences)

print(embeddings)

"""
input sentence --> wordpiece tokenization --> converted to token id --> 
all-MiniLM-L6-v2(contextual embedding for each token) -->
output (sentence embedding - dence vector - 384D)
"""
