from prettytable import PrettyTable
import math
from pprint import pprint

string = "we the people of the united states"
# string = "to be or not"

frequency = {c : string.count(c) for c in string}

# print(frequency)

sorted_keys = sorted(frequency, key=frequency.get, reverse=True)
# print(sorted_keys)

sorted_frequency = [(k, frequency[k]) for k in sorted_keys]

table = PrettyTable()
table.add_column("Letters", sorted_frequency + ["Total bits:"])


# Calculate the size to store each letter if we use 8 bits (byte) plus the sum of all these totals
bit_8 = [frequency[k]*8 for k in sorted_keys]
table.add_column("8-bit", bit_8 + [sum(bit_8)])


# Calculate the size to store each letter if we use x bits  plus the sum of all these totals
bits_required = math.ceil(math.log2(len(sorted_keys)))
bit_x = [frequency[k]*bits_required for k in sorted_keys]
table.add_column(f"{bits_required}-bit", bit_8 + [sum(bit_x)])

print(table)


# Calculate the Huffman coding
steps = []
this_step = sorted_frequency.copy()
this_step = [{"value":x[0], "cost":x[1], "string":""} for x in this_step]
steps.append(this_step)

sorted_keys_strings = {}


max_steps = 15
step_count = 0
while(step_count < max_steps and len(steps[-1]) > 1):
  print(f"Step {step_count}")
  this_step = steps[step_count].copy()

  this_step = sorted(this_step, key=lambda x: x["cost"], reverse=True)
  last = this_step[-1]
  second_last = this_step[-2]
  last["string"] += "0"
  second_last["string"] += "1"

  for chr in last["value"]:
    if chr in sorted_keys_strings:
      sorted_keys_strings[chr] = "0" + sorted_keys_strings[chr]
    else:
      sorted_keys_strings[chr] = "0"

  for chr in second_last["value"]:
    if chr in sorted_keys_strings:
      sorted_keys_strings[chr] = "1" + sorted_keys_strings[chr]
    else:
      sorted_keys_strings[chr] = "1"

  print(last)
  print(second_last)
  this_step = this_step[:-2] + [{"value":second_last["value"]+last["value"], "cost":second_last["cost"] + last["cost"], "string":""}]
  print(this_step)


  


  steps.append(this_step)
  step_count+=1

print(sorted_keys_strings)



print("Done")



