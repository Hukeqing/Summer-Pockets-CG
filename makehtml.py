curid = 1
count = 0
bgmlist = ['1311347835', '1311345874', '1311346849', '1311345853', '1311345855', '1311345856', '1311345859', '1311347847', '1311347848', '1311345861']
sourcefile = open('source.txt', 'r')
htmlfile = open('CGpage/' + str(curid) + '.html', 'w')
htmlfile.write('<!DOCTYPE html>\n<html>\n\n<head>\n\t<meta charset="utf-8">\n\t<title>page ' + str(curid) + '</title>\n\t<link rel="stylesheet" type="text/css" media="screen" href="main.css">\n</head>\n\n<body>\n\t<div>\n\t\t<iframe frameborder="no" id="bgm" class="bgm"\n\t\t\tsrc="https://music.163.com/outchain/player?type=2&id=' + str(bgmlist[curid - 1]) +'&auto=0&height=66">\n\t\t</iframe>\n\t</div>\n\t<div>\n')
for line in sourcefile:
    htmlfile.write('\t\t<a href="' + line + '" target="_blank"><img class="photo" src="' + line + '"> </a>\n')
    count+=1
    if count == 40:
        htmlfile.write('\t</div>\n</body>\n\n</html>')
        htmlfile.close()
        curid += 1
        htmlfile = open('CGpage/' + str(curid) + '.html', 'w')
        htmlfile.write('<!DOCTYPE html>\n<html>\n\n<head>\n\t<meta charset="utf-8">\n\t<title>page ' + str(curid) + '</title>\n\t<link rel="stylesheet" type="text/css" media="screen" href="main.css">\n</head>\n<body>\n\t<div>\n\t\t<iframe frameborder="no" id="bgm" class="bgm" \n\t\t\tsrc="https://music.163.com/outchain/player?type=2&id=' + str(bgmlist[curid - 1]) +'&auto=0&height=66">\n\t\t</iframe>\n\t</div>\n\t<div>\n')
        count = 0
if count != 0:
    htmlfile.write('\t</div>\n</body>\n\n</html>')
    htmlfile.close()
sourcefile.close()