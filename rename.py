import os
import numpy as np
from PIL import Image
from glob import glob

files = ['bathroom','lavender','kitchen','fall','kitchen1','seaside','barn','sd_bedroom','sd_livingroom',
         'sd_readingroom','sd_garden','anstronaut','living_room','victorian','steampunk','bedroom1','bedroom3','bathroom1',
         'computer','piano','dragon','sd_babyroom','tunnel','sd_garage',
         'conference','car','sd_classroom','wukong','bear','ocean','bust']

# files.sort()
# indexs = [1,3,2,1,1,1,1,3,2,2,1,3,3,1,1,2,1,1,1,1,1,3,1,3,2,1,2,2,1,3,1]
# for i, file in enumerate(files):
#     source_rgb = f'visual_time{indexs[i]}/rgb/{file}.mp4'
#     source_dpt = f'visual_time{indexs[i]}/dpt/{file}.mp4'
#     source_coarse_rgb = f'visual_time{indexs[i]}/rgb/coarse/{file}.mp4'
#     os.system(f'cp {source_rgb} visual/rgb')
#     os.system(f'cp {source_dpt} visual/dpt')
#     os.system(f'cp {source_coarse_rgb} visual/rgb/coarse')
    
# for file in files:
#     fn = str.split(file,'/')[-1]
#     fn = str.split(fn,'.')[0]
#     image = np.array(Image.open(f'visual/thumbnails/{fn}.png'))
#     H,W = image.shape[0:2]
#     W = int(W*72/H)
#     format1 = f'<span class="pill scene-pill" data-value="{fn}" onclick="selectCompVideo(activeMethodPill, this, 3)">'
#     format2 = f'    <img class="thumbnail-img" src="visual/thumbnails/{fn}.png" alt="{fn}" width="{W}">'
#     format3 = f'</span>'
#     print(format1)
#     print(format2)
#     print(format3)

# for file in files:
#     fn = str.split(file,'/')[-1]
#     fn = str.split(fn,'.')[0]
#     image = np.array(Image.open(f'visual/thumbnails/{fn}.png'))
#     H,W = image.shape[0:2]
#     W = int(W*72/H)
#     format1 = f'<span class="pill scene-pill" data-value="{fn}" onclick="selectC2Fvideos(activeMethodPill, this, 3)">'
#     format2 = f'    <img class="thumbnail-img" src="visual/thumbnails/{fn}.png" alt=fn width="{W}">'
#     format3 = f'</span>'
#     print(format1)
#     print(format2)
#     print(format3)   

for file in files:
    fn = str.split(file,'/')[-1]
    fn = str.split(fn,'.')[0]
    # image = np.array(Image.open(f'visual/thumbnails/{fn}.png'))
    # H,W = image.shape[0:2]
    # W = int(W*72/H)
    # format1 = f'<span class="pill scene-pill" data-value="{fn}" onclick="selectSDSvideos(activeMethodPill, this, 3)">'
    # format2 = f'    <img class="thumbnail-img" src="visual/thumbnails/{fn}.png" alt=fn width="{W}">'
    # format3 = f'</span>'
    # print(format1)
    # print(format2)
    # print(format3)   
    os.system(f'rm -rf visual/sds/{fn}/*dpt.mp4')