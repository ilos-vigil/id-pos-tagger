# source : https://stanfordnlp.github.io/stanfordnlp/pos.html
import stanfordnlp

nlp = stanfordnlp.Pipeline(processors='tokenize,mwt,pos', lang='id')
doc = nlp('Bahasa Indonesia adalah bahasa Melayu yang dijadikan sebagai bahasa resmi Republik Indonesia dan bahasa persatuan bangsa Indonesia. '
    'Bahasa Indonesia diresmikan penggunaannya setelah Proklamasi Kemerdekaan Indonesia, tepatnya sehari sesudahnya, bersamaan dengan mulai berlakunya konstitusi. '
    'Di Timor Leste, bahasa Indonesia berstatus sebagai bahasa kerja. '
    'Kentang (Solanum tuberosum L.) adalah tanaman dari suku Solanaceae yang memiliki umbi batang yang dapat dimakan dan disebut "kentang" pula. '
    'Umbi kentang sekarang telah menjadi salah satu makanan pokok penting di Eropa walaupun pada awalnya didatangkan dari Amerika Selatan. '
    'Penjelajah Spanyol dan Portugis pertama kali membawa ke Eropa dan mengembangbiakkan tanaman ini.')
print(*[f'(\'{word.text}\', \'{word.pos}\')' for sent in doc.sentences for word in sent.words], sep='\n')
