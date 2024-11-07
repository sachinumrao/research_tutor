from voyager import Index, Space
from sentence_transformers import SentenceTransformer
from typing import List, Dict


EMBEDDING_MODEL = SentenceTransformer("nomic-text-embed-v1", trust_remote_code=True)

def build_index(text_chunks):
    doc_embeddings = EMBEDDING_MODEL.encode(text_chunks)

    # create index
    doc_index = Index()
    doc2idx = None
    return doc_index, doc2idx


def encode_query(text):
    return EMBEDDING_MODEL.encode(text)

def retireve_results(index, idx2doc: Dict[int, str], query:str)->List[str]:
    query_embedding = encode_query(query)

    # extarct ids
    # extract text chunks
    results = ['']
    return results
