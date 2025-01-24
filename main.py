import json
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Require one argument defining the key and another defining the value to build a key:value pair file."
              " Require file name. Example: JSONToKVPair name value C:/path/to/file.json")
        exit()

    SCOPE_NODE = 'Scope'
    ENVIRONMENT_NODE = 'Environment'

    keyArg = sys.argv[1]
    valueArg = sys.argv[2]
    fileNameArg = sys.argv[3]
    envToProcessArg = sys.argv[4]

    fileToProcess = open(fileNameArg)
    jsonFileToProcess = json.load(fileToProcess)
    fileToProcess.close()

    fileToWrite = ""

    for key in jsonFileToProcess['Variables']:
        # If environment present check it against the users sysarg, else if environment present and empty.
        # Value to be processed under both conditions.
        isProcessJSONValue = ((SCOPE_NODE in key and ENVIRONMENT_NODE in key[SCOPE_NODE]
                              and key[SCOPE_NODE][ENVIRONMENT_NODE][0] == envToProcessArg)
                              or (SCOPE_NODE in key and len(key[SCOPE_NODE]) == 0))

        if isProcessJSONValue:
            if keyArg in key and valueArg in key:
                if key[keyArg] is not None:
                    fileToWrite += key[keyArg] + ":"
                else:
                    fileToWrite += "Null:"

                if key[valueArg] is not None:
                    fileToWrite += key[valueArg] + "," + "\n"
                else:
                    fileToWrite += "Null" + "," + "\n"

    if fileToWrite[-2:] == ',\n':
        fileToWrite = fileToWrite[:-2]
        fileToWrite += '\n'

    savedFilePath = os.path.splitext(os.path.basename(fileNameArg))[0] + ".txt"

    savedFile = open(savedFilePath, 'w')
    savedFile.write(fileToWrite)
    savedFile.close()
