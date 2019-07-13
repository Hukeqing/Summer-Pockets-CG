curid = 1
count = 0
sourcefile = open('source.txt', 'r')
htmlfile = open(str(curid) + '.html', 'w')
htmlfile.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<title>page ' + str(curid) + '</title>\n<link rel="stylesheet" type="text/css" media="screen" href="main.css">\n</head>\n<body>\n<div>\n<iframe frameborder="no" id="bgm" class="bgm" src="https://music.163.com/outchain/player?type=2&id=1311347835&auto=0&height=66">\n</iframe>\n</div>\n<div>\n')
for line in sourcefile:
    htmlfile.write('<a href="' + line + '" target="_block"><img class="photo"src="' + line + '"> </a>\n')
    count+=1
    if count == 45:
        htmlfile.write('</div></body></html>')
        htmlfile.close()
        curid += 1
        htmlfile = open(str(curid) + '.html', 'w')
        htmlfile.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<title>page ' + str(curid) + '</title>\n<link rel="stylesheet" type="text/css" media="screen" href="main.css">\n</head>\n<body>\n<div>\n<iframe frameborder="no" id="bgm" class="bgm" src="https://music.163.com/outchain/player?type=2&id=1311347835&auto=0&height=66">\n</iframe>\n</div>\n<div>\n')
        count = 0
if count != 0:
    htmlfile.write('</div></body></html>')
    htmlfile.close()
sourcefile.close()