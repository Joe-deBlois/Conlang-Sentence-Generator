from itertools import chain
from collections import Counter, defaultdict
import tempfile

#-----------------------------------------------------------
#Code for option 2; generated sentences from input strings 
#-----------------------------------------------------------

print("Text input rules: \n "
"-Text must be inputted as one string\n "
"-Text must be in the IPA, with periods as syllable markers and spaces as word boundaries\n "
"-Affricates and diphthongs must have a tie-bar above them\n "
"-This version does not support diacritics or tones\n "
"-The model will learn best with >100 words as input\n "
"-At this stage, the program will only use phonemes found in your string (it will not extrapolate and use likely novel phonemes)")

input_string = input("Please input your text here: \n")
print(input_string)

input_max_word_length = input("Please input the maximum number of syllables a word can have: \n")

input_number_words = input("Please input how many words you want: \n")



#  PART 1: PHONOTACTIC SYLLABIFIER--------------------------------------------------------------------------------------

#region ==PREPARE INPUT STRING ==

#for flattening lists later
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

#map complex symbols so they can be read as characters
affricate_and_diphthong_mapping = {
    "d͡ʒ": "0",
    "t͡ʃ": "1", 
    "t͡s": "2",
    "d͡z": "3", 
    "p͡f" : "4", 
    "k͡x": "5", 
    "a͡ɪ":"6", 
    "e͡ɪ":"7", 
    "a͡ʊ": "8", 
    "o͡ʊ" :"9", 
    "ɔ͡ɪ": "@",
    "e͡ə": "#", 
    "ʊ͡ə": "$", 
    "u͡ɪ" : "%", 
    "i͡ʊ" : "^", 
    "ə͡ɪ" : "&", 
    "ɪ͡ə" : "*", 
    "œ͡ɪ" : "(", 
    "ʏ͡ə" : ")", 
    "œ͡ʊ" : "-", 
    "i͡ə": "+", 
    "u͡ə" : "=", 
    "y͡ə" : "`", 
    "e͡i": "[", 
    "ø͡i" :"]", 
    "ɛ͡ɪ": "<", 
    "a͡ɛ": ">", 
    "ɔ͡ə": "?"
}

def map_affricates_and_diphthongs(text):
    for aff_or_diph, replacement in affricate_and_diphthong_mapping.items():
        text = text.replace(aff_or_diph, replacement)
    return text

#map input data
input_string = map_affricates_and_diphthongs(input_string)
#endregion

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
    if char in ["0", "1", "2","3", "4", "5"]:
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
    if char in ["6", "7", "8", "9", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "[", "]", "<", ">", "?", "`"]:
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

#PART 2: MORPHEME SEGMENTOR-------------------------------------------------------------------------------------

#region == MORPHOLOGICAL SEGMENTATION ==

#look for repeated syllables
#are they at the start, end, or middle?
#repeated ones in the middle are probably nouns, start/end are probably affixes
#given these, do the saved segments appear anywhere else in any other words?
#for each word add the first syllable to "prefixes", last syllable to , etc..

morpheme_segmentation = []
for word in words:
    morpheme_segmentation.append(word.split("."))

prefix_candidates = defaultdict(int)
suffix_candidates = defaultdict(int)
root_candidates = defaultdict(int)
prefix_or_suffix_candidates = dict()
prefix_or_root_candidates = dict()
root_or_suffix_candidates = dict()
anywhere_candidates = dict()
stand_alone = []


for word in morpheme_segmentation:
    if len(word) < 2: 
        stand_alone.append(word)
        continue
    prefix = word[0]
    suffix = word[-1]

    prefix_candidates[prefix] += 1
    suffix_candidates[suffix] += 1
    #root(s): anything between prefix and suffix
    if len(word) > 2:
        roots = word[1:-1]
    else:
        roots = word[1:-1]  # Will be empty if only 2 morphemes

    for root in roots:
        root_candidates[root] += 1

# Make a list to avoid RuntimeError due to dict size change during iteration
for key in list(prefix_candidates):
    
    if key in suffix_candidates and root_candidates:
        anywhere_candidates[key] = prefix_candidates[key] + suffix_candidates[key] + root_candidates[key]
        del prefix_candidates[key]
        del suffix_candidates[key]
        del root_candidates[key]
    
    if key in suffix_candidates:
        prefix_or_suffix_candidates[key] = prefix_candidates[key] + suffix_candidates[key]
        del prefix_candidates[key]
        del suffix_candidates[key]
    
    elif key in root_candidates:
        prefix_or_root_candidates[key] = prefix_candidates[key] + root_candidates[key]
        del prefix_candidates[key]
        del root_candidates[key]

# Now check root vs suffix
for key in list(root_candidates):
    
    if key in suffix_candidates:
        root_or_suffix_candidates[key] = root_candidates[key] + suffix_candidates[key]
        del root_candidates[key]
        del suffix_candidates[key]
    

#endregion

#region ==MORPHEME RULES ===

# r = root, p = prefix, s = suffix, rs = root/suffix, pr = prefix/root, ps = prefix/suffix, sa = stand alone, aw = anywhere

morphological_typology = input("Is your language Isolating (1), Agglutinative (2), Fusional (3), or Polysynthetic(4)? \n")

if morphological_typology == "1": #isolating
    word_structures = ["sa", "aw", "r"]
elif morphological_typology =="2":    #agglutinative
    word_structures = ["p+r", "r+s", "p+r+s", "r+rs", "p+rs", "rs+s","p+aw", "aw+s", "p+aw+s"]
elif morphological_typology =="3": #fusional
    word_structures = ["sa", "r", "aw","p+r", "r+s", "p+r+s","p+rs", "r+rs", "rs+s","p+pr", "pr+s","r+ps", "ps", "pr", "rs"]
elif morphological_typology == "4": #polysynthetic
    word_structures = ["sa", "r", "aw","p+r", "r+s", "p+r+s","p+aw", "aw+s", "p+aw+s", "aw+aw","p+pr", "pr+s", "p+rs", "rs+s", "p+p+r", "r+r","p+r+r","p+r+s+s","p+p+r+s","p+r+s+s+s", "p+aw+r+aw+s","p+r+aw+aw+s","p+pr+r+s","p+r+rs+s","p+n+r+s", "p+n+v+s","p+aw+n+v+s+s","aw+p+r+s+aw"]
        

#endregion

#PART 3: WORD GENERATOR--------------------------------------------------------------------------------------------
#What do we have to consider?
#User specs: max word length in input_max_word_length, words required in input_number_words
#Phonology data: all consonants/vowels, their frequency, 
#Syllable data: all valid syllable structures in unique_syllables
#Morphology: morphological_typology, as well as what morphemes can fit into that structure. 
#Extrapolations: valid syllables based on phoneme frequency and unique_syllables, valid morphemes based on valid syllables. Use a mix of pre-defined and generated sounds for new words? Weights for more probable sounds/syllables



#Add stress patterns and phonotactics design later

