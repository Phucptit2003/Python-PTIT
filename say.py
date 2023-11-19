from gtts import gTTS
import playsound
import os

text = "Em nhà ở đâu thế" 
t=1
while t<3:
    output = gTTS(text, lang="vi", slow=False)
    output.save('output.mp3')  # Lưu tệp âm thanh với tên 'output.mp3'
    playsound.playsound('output.mp3', True)  # Phát tệp âm thanh 'output.mp3'
    #os.remove('output.mp3')
    t+=1