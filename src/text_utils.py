from nltk import sent_tokenize

MAX_CHUNK_SIZE = 512
OVERLAP_WINDOW = 128

def get_chunks(file_path):
    with open(file_path, "r") as f:
        text_data = f.read()

    sents = sent_tokenize(text_data)

    # organize sentences into chunks
    chunks = []

    curr_chunk = []
    curr_chunk_len = 0
    for s in sents:
        n = len(s.split())
        if curr_chunk_len + n < MAX_CHUNK_SIZE:
            curr_chunk.append(s)
            curr_chunk_len += n

        else:
            joint_str = " ".join(curr_chunk)
            chunks.append(joint_str)
            curr_chunk = []
            curr_chunk_len = 0


# TODO
# fix pytorch issues
# implement overlap window
