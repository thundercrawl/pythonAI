from bv.algorithm.w2v import word2vec as word2vec
import jieba
import bv.util.stringUtil as strUtils
#####################################################################

settings = {
    'window_size': 2,  # context window +- center word
    'n':
    10,  # dimensions of word embeddings, also refer to size of hidden layer
    'epochs': 50,  # number of training epochs
    'learning_rate': 0.01  # learning rate
}

text = "natural language processing and machine learning is fun and exciting"
#text = "how much car is"
# Note the .lower() as upper and lowercase does not matter in our implementation
textcn = "欢迎来到北京大学,新鲜的小朋友,奔驰汽车G20"

# [['natural', 'language', 'processing', 'and', 'machine', 'learning', 'is', 'fun', 'and', 'exciting']]
'''
corpus = [[word.lower() for word in text.split()]]

# Initialise object

w2v = word2vec()

# Numpy ndarray with one-hot representation for [target_word, context_words]

training_data = w2v.generate_training_data(settings, corpus)

# Training
print(training_data)
w2v.train(training_data)

# Get vector for word

word = "and"

vec = w2v.word_vec(word)

print(word, vec)

# Find similar words

w2v.vec_sim("machine", 3)
'''