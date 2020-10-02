from wordcloud import WordCloud

from PIL import Image #mask 이미지
import numpy as np

import matplotlib.font_manager as fm

# 이용 가능한 폰트 중 '고딕'만 선별 , 찾기
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

file_url = "D:/99. STUDY/10. Python/sparta/KakaoTalk_20201002_1304_16_954_group.txt"

text = ''
with open(file_url , "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[2:]:  #2번째 줄부터.. 작업
        if '] [' in line:    #텍스트 메시지만 취함
            #text += line    
            text += line.split('] ')[2].replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('사진\n','').replace('이모티콘\n','').replace('삭제된 메시지입니다','')   
            print("출력 라인"  + line)

font_path = 'C:\Windows\Fonts\malgunbd.ttf'

mask_cloud = np.array(Image.open('mask_cloud.png'))

wc = WordCloud(font_path, background_color="white", mask = mask_cloud )
wc.generate(text)
wc.to_file("cloud_text_result.png")

