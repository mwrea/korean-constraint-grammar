import sys

"""
Find sentences in a CoNLL-U file that have at least
one ambiguous token.
"""

#jį	jis	PRON	Case=Acc|Gender=Masc|Number=Sing|Person=3

lookup = {} # dict keyed on the wordform value = list of analyses

for line in open(sys.argv[1]).readlines():
	row = line.strip().split('\t')
	if row[0] not in lookup:
		lookup[row[0]] = []
	lookup[row[0]].append((row[1], row[2], row[3]))

last_seen_sent_id = ''
ambiguous = False
ambiguous_wordforms = []
for line in sys.stdin.readlines():

	if line[0] == '#':
		if line.find('sent_id') > 0:
			last_seen_sent_id = line.strip()
		continue		

	if line.strip() == '':
		print(last_seen_sent_id, '/',ambiguous_wordforms)
		last_seen_sent_id = ''
		ambiguous = False
		ambiguous_wordforms = []
		continue

	row = line.split('\t')

	wordform = row[1]
	if wordform in lookup:
		if len(lookup[wordform]) > 1:
			ambiguous = True
			ambiguous_wordforms.append(wordform)

