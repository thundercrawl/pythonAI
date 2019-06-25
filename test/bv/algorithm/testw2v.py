from bv.algorithm.w2v import word2vec as word2vec
from bv.algorithm.w2v inmport settings as settings
#####################################################################

text = "where you from china"

# Note the .lower() as upper and lowercase does not matter in our implementation

# [['natural', 'language', 'processing', 'and', 'machine', 'learning', 'is', 'fun', 'and', 'exciting']]

print(word)
corpus = [[word.lower() for word in text.split()]]

# Initialise object

w2v = word2vec()

# Numpy ndarray with one-hot representation for [target_word, context_words]

training_data = w2v.generate_training_data(settings, corpus)

# Training

w2v.train(training_data)

# Get vector for word

word = "china"

vec = w2v.word_vec(word)

print(word, vec)

# Find similar words

w2v.vec_sim("machine", 3)