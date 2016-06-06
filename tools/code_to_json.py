# Script to convert the template source code for AzureFunctions to json format

print "Get json_output.txt together..."
target_file = open("json_output.txt", 'w')
target_file.truncate()
target_file.write("#This is the output of code_to_json.py\n")
target_file.write("#This function simply converts code into json format\n\n")

print "For each line in source_code.txt, write a json line..."
with open("source_code.txt", 'r') as sc_file:
   for line in sc_file:
       print line
       target_file.write("\"" + line.split("\n")[0] + "\",\n")
