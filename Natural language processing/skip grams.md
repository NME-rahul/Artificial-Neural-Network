# Skip Grams

Skip grams is a model falls under the word2vec framework. It's primary goal is to learn distributed representations of words in a way that captutres semantic relationship between words.

Simply, The model is trained to predict context words given a target word.

**Tensorflow syntax**

    embedding_layer = tf.keras.layers.Embedding(input_dim, output_dim, input_length)
    dense_layer = tf.keras.layers.Dense(vocab_size, activation='softmax')(embedding_layer)

* **input_dim**: dimension of vocabulary.
* **output_dim**: the dimension you want to apply on vocabulary, eg. 1D. [0.5], 2D [0.5, 0.3], 3D [0.1, 0.3, 0.6], 4D [0.7, 0.3, 0.6, 0.5], nD. [0.2, 0.5, 0.2, 0.5,......,](you can apply any size of embedding, the more you increase the dimnesion the more information it captures).
* **input_length**: length of single input sequence.


## Mathematics

$$text = \begin{bmatrix}
\text{"In the quiet hush of twilight's embrace"} \\
\text{"Where the stars twinkle with gentle grace"} \\
\text{"A world of dreams comes to life at night"} \\
\text{"In the soft glow of the pale moonlight."}
\end{bmatrix}
$$
