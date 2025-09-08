from itertools import chain
from collections import Counter
import morfessor

#-----------------------------------------------------------
#Code for option 2; generated sentences from input strings (AI)
#-----------------------------------------------------------

print("Text input rules: \n -Text must be inputted as one string\n -Text must be in the IPA, with periods as syllable markers and spaces as word boundaries\n -Affricates and diphthongs must have a tie-bar above them\n -This version does not support diacritics or tones\n -The model will learn best with >100 words as input")
input_string = input("Please input your text here: \n")
print(input_string)


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

#  PART 1: PHONOTACTIC SYLLABIFIER 

#region ==DATA COLLECTION ITEMS==

words = input_string.split(" ")
word_counts = Counter(words)
phonemes = list(input_string)
syllables = []
for word in words:
    word = word.split(".")
    syllables.append(word)
syllables = flatten_list(syllables)
syllable_structures = syllables.copy()
morfessor_corpus = []

unique_syllables = list(set(syllables))

consonant_counts = dict()
vowel_counts = dict()
syllable_counts = dict()
syllable_structure_counts = dict()


stops = []
nasals = []
trills = []
flaps = []
fricatives = []
lateral_fricatives = []
approximants = []
lateral_approximants = []
bilabials = []
labiodentals = []
dentals = []
alveolars =[] 
postalveolars = []
retroflexives = []
palatals = []
velars = []
uvulars = []
pharyngeals = [] 
glottal = []
affricates = []
clicks = []
voiced = []
voiceless = []
front = []
central = []
back = []
high = []
high_mid = []
mid = []
low = []
rounded = []
unrounded = []
diphthongs = []
consonants = []
vowels = []
#endregion

#region ==DETERMINE ALL GIVEN PHONEMES==

#determine all phonemes in the input string
for char in phonemes: 
    if char in ["p", "b", "t", "d", "ʈ", "ɖ", "c", "ɟ", "k", "g", "q", "ɢ", "ʔ","pʼ", "tʼ", "kʼ" ]:
        stops.append(char)
    if char in ["m", "ɱ", "n", "ɳ", "ɲ", "ŋ", "ɴ"]:
        nasals.append(char)
    if char in ["ʙ", "r", "ʀ"]:
        trills.append(char)
    if char in ["ⱱ", "ɾ", "ɽ", "ɺ"]:
        flaps.append(char)
    if char in ["ɸ", "β", "f", "v", "θ", "ð", "s", "z", "ʃ", "ʒ", "ʂ", "ʐ", "ç", "ʝ", "x", "ɣ", "χ", "ʁ", "ħ", "ʕ", "h", "ɦ", "ɕ", "ʑ", "ʍ", "ʜ", 'sʼ']:
        fricatives.append(char)
    if char in ["ɬ", "ɮ"]:
        lateral_fricatives.append(char)
    if char in ["ʋ", "ɹ", "ɻ", "j", "ɰ"]:
        approximants.append(char)
    if char in ["l", "ɭ", "ʎ", "ʟ"]:
        lateral_approximants.append(char)
    if char in ["p", "b", "m", "ʙ", "β", "ɸ", "ʘ", "ɓ", "pʼ"]:
        bilabials.append(char)
    if char in ["ɱ", "ⱱ", "f", "v", "ʋ"]:
        labiodentals.append(char)
    if char in ["t", "d", "n", "r", "ɾ", "ð", "θ", "ɬ", "ɮ", "ɹ", "l", "ǀ", "ɗ", "tʼ"]:
        dentals.append(char)
    if char in ["t", "d", "n", "r", "ɾ", "s", "z", "ɬ", "ɮ", "ɹ", "l", "ǃ", "ɗ", "tʼ", "ɺ", "sʼ"]:
        alveolars.append(char)
    if char in ["t", "d", "n", "r", "ɾ", "ʃ", "ʒ", "ɮ", "ɬ", "ɹ", "l", "ǃ"]:
        postalveolars.append(char)
    if char in ["ʈ", "ɖ", "ɳ", "ɽ", "ʂ", "ʐ", "ɻ", "ɭ"]:
        retroflexives.append(char)
    if char in ["c", "ɟ", "ɲ", "ç", "ʝ", "j", "ʎ", "ǂ", "ʄ"]:
        palatals.append(char)
    if char in ["k", "ɡ", "ŋ", "x", "ɣ", "ɰ", "ʟ", "kʼ", "ɠ"]:
        velars.append(char)
    if char in ["q", "ɢ", "ɴ", "ʀ", "χ", "ʁ", "ʛ"]:
        uvulars.append(char)
    if char in ["ħ", "ʕ"] :
        pharyngeals.append(char)
    if char in ["ʔ"]:
        glottal.append(char)
    if char in ["d͡ʒ", "t͡ʃ", "t͡s","d͡z", "p͡f", "k͡x"]:
        affricates.append(char)
    if char in ["ʘ", "ǀ", "ǃ", "ǂ", "ǁ"]:
        clicks.append(char)
    if char in ["b", "m", "ʙ", "β", "v", "ⱱ", "ɱ", "ʋ", "d", "n", "r", "ɾ", "ð", "z", "ʒ", "ɮ", "ɹ", "l", "ɖ", "ɳ", "ɽ", "ʐ", "ɻ", "ɭ", "ɟ", "ɲ", "ʝ", "j", "ʎ", "ɡ", "ŋ", "ɣ", "ɰ", "ʟ", "ɢ", "ɴ", "ʀ", "ʁ", "ʕ", "ɦ", "ɓ", "ɗ", "ʄ", "ɠ", "ʛ"]:
        voiced.append(char)
    if char in ["p", "ɸ", "f", "θ", "s", "ʃ", "ʂ", "ʈ", "c", "ç", "x", "k", "q", "χ", "ħ", "ʔ", "h", "pʼ", "tʼ", "kʼ", "sʼ", "ɧ"]:
        voiceless.append(char)
    if char in ["i", "y", "ɪ", "ʏ", "ø", "e", "ɛ", "œ", "æ", "a", "ɶ"]:
        front.append(char)
    if char in ["ɨ", "ʉ", "ɘ", "ɵ", "ə", "ɜ", "ɞ", "ɐ"]:
        central.append(char)
    if char in ["ɯ", "u", "ʊ", "ɤ", "o", "ʌ", "ɔ", "ɑ", "ɒ"]:
        back.append(char)
    if char in ["i", "y", "ɪ", "ʏ", "ɨ", "ʉ", "ʊ", "ɯ", "u"]:
        high.append(char)
    if char in ["e", "ø", "ɘ", "ɵ", "ɤ", "o"]:
        high_mid.append(char)
    if char in ["ɛ", "œ", "ə", "ɜ", "ɞ", "ʌ", "ɔ", "æ", "ɐ"]:
        mid.append(char)
    if char in ["a", "ɶ", "ɑ", "ɒ"]:
        low.append(char)
    if char in ["y", "ʏ", "ø", "œ", "ɶ", "ʉ", "ɵ", "ɞ", "ɒ", "ɔ", "o", "u"]:
        rounded.append(char)
    if char in ["i", "e", "ɪ", "ɨ", "ɘ", "ʊ", "ɯ", "ɤ", "ə", "ɛ", "ɜ", "ʌ", "ɐ", "æ", "a", "ɑ"]:
        unrounded.append(char)
    if char in ["a͡ɪ", "e͡ɪ", "a͡ʊ", "o͡ʊ", "ɔ͡ɪ", "e͡ə", "ʊ͡ə", "u͡ɪ", "i͡ʊ", "ə͡ɪ", "ɪ͡ə", "œ͡ɪ", "ʏ͡ə", "œ͡ʊ", "i͡ə", "u͡ə", "y͡ə", "e͡i", "ø͡i", "ɛ͡ɪ", "a͡ɛ", "ɔ͡ə"]:
        diphthongs.append(char)

#create seperate lists of all consonants, all vowels, and all phonemes
consonants = list(set(stops + nasals + trills + flaps + fricatives + lateral_fricatives + approximants + lateral_approximants + bilabials + labiodentals + dentals + alveolars + postalveolars + retroflexives + palatals + velars + uvulars + pharyngeals + glottal + affricates + clicks + voiced + voiceless))
vowels = list(set(front+ central + back + diphthongs))
phonemes = list(set(consonants + vowels))

#Map number of vowels and consonants to those consonants
for char in input_string:
    if char in vowels:
        if char not in vowel_counts:
            vowel_counts[char] = 1
        else:
            vowel_counts[char]+= 1
    if char in consonants:
        if char not in consonant_counts:
            consonant_counts[char] = 1
        else:
            consonant_counts[char]+= 1

#endregion 

#region ==DETERMINE ALL GIVEN SYLLABLES==

#Determine all syllables in C/V form
for i, syllable in enumerate(syllable_structures):
    structure = ""
    for char in syllable:
        if char in consonants:
            structure += "C"
        else:
            structure += "V"
    syllable_structures[i] = structure

#Map syllables to their counts
for syllable in syllables:
    if syllable not in syllable_counts:
        syllable_counts[syllable] = 1
    else:
        syllable_counts[syllable]+= 1

#Map syllable structures (i.e. C/V form syllables) to their counts
for structure in syllable_structures:
    if structure not in syllable_structure_counts:
        syllable_structure_counts[structure] = 1
    else:
        syllable_structure_counts[structure] +=1
    
#endregion

#region ==MORFESSOR MORPHOLOGICAL SEGMENTATION==

morfessor_corpus = [(int(freq), word) for word, freq in word_counts.items()]

#initialize and train model
model = morfessor.BaselineModel()
model.load_data(morfessor_corpus)
model.train_batch()

#Use the model on the data it was trained on, since this section is just gathering patterns
for word in words:
    segments, _ = model.viterbi_segment(word)
    print(" + ".join(segments))
