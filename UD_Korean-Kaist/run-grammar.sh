# first generate an analyser from all of the treebank.
cat *.conllu | python3 ../../ud-scripts/conllu-analyser.py -t ../korean-analyser.tsv

# take the dev data and run it through the analyser to produce 
# the source file
cat ko_kaist-ud-dev.ref | sed 's/^$/X@X@X/g' | grep -v '^	' | sed 's/"<//g' | sed 's/>"//g' | tr '\n' ' ' | sed 's/X@X@X/\n/g' | sed 's/^ *//g' | python3 ../../ud-scripts/conllu-analyser.py ../korean-analyser.tsv | grep -v '"<>"' | grep -v '"\*"' | sed 's/"." PUNCT/&\n/g' > ko_kaist-ud-dev.src

# run the source file through our CG rules
cat ko_kaist-ud-dev.src | vislcg3 --trace --grammar ko_kaist-ud.cg3 > ko_kaist-ud-dev.tst

# calculate the accuracy of the rules
python3 ~/ud-scripts/vislcg3-evaluate.py ko_kaist-ud-dev.src ko_kaist-ud-dev.ref ko_kaist-ud-dev.tst

