string = "we the people of the united states"

frequencies = [{"values":[{"char":x,"bits":""}],"score":string.count(x)/len(string)} for x in set(string)]

tree = sorted(frequencies, key=lambda x:x["score"], reverse=True)

while len(tree) > 1:
  last = tree.pop()
  second_last = tree.pop()

  for value in last["values"]:
    value["bits"] = "1" + value["bits"] 

  for value in second_last["values"]:
    value["bits"] = "0" + value["bits"] 

  to_add = {"values":last["values"] + second_last["values"], "score":last["score"] + second_last["score"]}

  tree.append(to_add)
  tree = sorted(tree, key=lambda x:x["score"], reverse=True)

print()
print(tree)
