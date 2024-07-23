import random

Sentence_starter = ['About 100 years ago', 'In the 20 BC', 'Once upon a time']
character = ['There lived a king.', 'There was a man named Jack.', 'There lived a farmer.']
time = ['One day', 'One full-moon night']
story_plot = ['He was passing by', 'He was going for a picnic to']
place = ['the mountains', 'the garden']
second_character = ['He saw a man', 'He saw a young lady']
age = ['who seemed to be in late 20s', 'who seemed very old and feeble']
work = ['searching something.', 'digging a well on the roadside.']


random_sentence = (
    random.choice(Sentence_starter) +
    random.choice(character) +
    random.choice(time) +
    random.choice(story_plot) +
    random.choice(place) +
    random.choice(second_character) +
    random.choice(age) +
    random.choice(work)
)
print(random_sentence)
