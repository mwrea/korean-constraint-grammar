words=['NULL']
writer=open('contexts.ez', 'w')
with open('ko_kaist-ud-dev.conllu', 'r') as f:
    for line in f:
        if (not line.startswith("#")) and (line.strip()):
            data=line.split()
            words.append((data[0], data[1], data[3]))

for x in range(1, len(words)):
    writer.write(words[x][1] + ' ' + words[x][2] + ' ')
    if not int(words[x][0]) == 1:
        writer.write('Prev: ' + words[x-1][2] + ' ')
    if  words[x][2]=='PUNCT':
        writer.write('\n')
    else:
        writer.write('Post: ' + words[x+1][2] + ' \n')
writer.close()
