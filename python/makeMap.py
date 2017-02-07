from clean import skills

labelToTokens = {}

for skill in skills:
    label = raw_input("Please enter the appropriate label for %s: " % skill)
    labelToTokens[label] = labelToTokens.get(label,[]) + [skill]


tokensToLabel = {}

for label, tokens in labelToTokens.items():
    for token in tokens:
        tokensToLabel[token] = label


print "labelToTokens: " + str(labelToTokens)
print "===================================="
print "tokensToLabel: " + str(tokensToLabel)

with open("./skills.txt","wb") as f:
    f.write("skills = %s" % str(tokensToLabel))
