import json
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Require one argument defining the key and another defining the value to build a key:value pair file."
              " Require file name. Example: JSONToKVPair name value C:/path/to/file.json")
        exit()

    key_arg = sys.argv[1]
    value_arg = sys.argv[2]
    file_name = sys.argv[3]

    fileToProcess = open(file_name)
    jsonFileToProcess = json.load(fileToProcess)
    fileToProcess.close()

    fileToWrite = ""

    for key in jsonFileToProcess['Variables']:
        if key_arg in key and value_arg in key:
            if key[key_arg] is not None:
                fileToWrite += key[key_arg] + ":"
            else:
                fileToWrite += "Null:"

            if key[value_arg] is not None:
                fileToWrite += key[value_arg] + "," + "\n"
            else:
                fileToWrite += "Null" + "," + "\n"
        else:
            raise ValueError("key and/or value argument was not found in JSON file.")

    if fileToWrite[-2:] == ',\n':
        fileToWrite = fileToWrite[:-2]
        fileToWrite += '\n'

    savedFilePath = os.path.splitext(os.path.basename(file_name))[0] + ".txt"

    savedFile = open(savedFilePath, 'w')
    savedFile.write(fileToWrite)
    savedFile.close()
