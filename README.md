# scatterbopper

An alternative CW learning method

Basically, I want to experiment with an approach slightly different to the Koch
method. Instead of blasting 20 words or so at the student at once, I want to
subject the student to single words at full speed and proper spacing, having the
student type the full word only at the end of each listen, and then make the
words longer as the accuracy improves.

My idea is that this, unlike conventional Koch, might be better for learning
head copy, as it encourages the student to copy and remember longer and longer
stretches of code as opposed to having them become CW stenographers.

## Usage

* Make and enter a Python 3 virtual environment.
* Install the required dependencies:  `pip install -r requirements.txt`
* Run the thing like so: `./scatterbopper.py koch_level word_length test_length`

## Command line arguments

### koch_level
Basically how many unique symbols will be in the test. Increment when you want
to introduce additional symbols. Currently uses the symbol sequence described in
the 1936 Koch study, which *isn't* considered the best sequence nowadays, but it
was the first one that came to mind. Will add other sequences later.

### word_length
The length of the word you will have to listen to before being given the chance
to type your answer. Set to 1 in order to learn individual letters first; set to
2 to learn to head copy letters in pairs, and so on, working your way up.

### test_length
The amount of words you will be tested on before being presented with your
score.

## TODO

The following features are proposed:

* Make the learning sequence changeable/configurable.
* Incremental mode: continuous testing with the word length auto incrementing or
decrementing based on how well you're doing. New letters to be introduced in
cleartext at first, until the user has gotten them right a couple of times.
* Testing for non-letter symbols and prosigns.
* Callsigns mode: Variable-length words consisting of callsigns as they would
appear in the wild.
* Optional real-life confounders: QRM, QRN, QSB.
* An Android port would be neat, but that'd be a bit out of my wheelhouse.
