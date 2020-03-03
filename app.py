from nltk.tag.stanford import StanfordPOSTagger
from nltk.tokenize import word_tokenize
from pprint import pprint

our_pos_tagger = StanfordPOSTagger('postagger-model-id.tagger', 'stanford-postagger-basic/stanford-postagger.jar')

daftar_kalimat = [
    'Bahasa Indonesia adalah bahasa Melayu yang dijadikan sebagai bahasa resmi Republik Indonesia dan bahasa persatuan bangsa Indonesia.',
    'Bahasa Indonesia diresmikan penggunaannya setelah Proklamasi Kemerdekaan Indonesia, tepatnya sehari sesudahnya, bersamaan dengan mulai berlakunya konstitusi.',
    'Di Timor Leste, bahasa Indonesia berstatus sebagai bahasa kerja.',
    'Kentang (Solanum tuberosum L.) adalah tanaman dari suku Solanaceae yang memiliki umbi batang yang dapat dimakan dan disebut "kentang" pula.',
    'Umbi kentang sekarang telah menjadi salah satu makanan pokok penting di Eropa walaupun pada awalnya didatangkan dari Amerika Selatan.',
    'Penjelajah Spanyol dan Portugis pertama kali membawa ke Eropa dan mengembangbiakkan tanaman ini.'
]

for kalimat in daftar_kalimat:
    our_tagged_word = our_pos_tagger.tag(word_tokenize(kalimat))
    print(kalimat)
    pprint(our_tagged_word)
