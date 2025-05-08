import platform
import sys
#Set operating_system var to the device's OS
operating_system = platform.system()
#Check if the Python version is below 3.11, if so, issues a warning!
if sys.version_info < (3, 11):
    continueWithBadPython = str(input(f"Your Python Version is below 3.11, are you sure you want to continue? Continuing could cause this script to run unexpectedly. Continue? Y/N: "))
    if continueWithBadPython == 'Y' or continueWithBadPython == 'y':
        print('Continuing with Python ' + str(sys.version_info))
    else:
        exit()
#If the version is below 3, the script will not work.
if sys.version_info.major < 3:
    print(f"This script requires Python 3 or higher. Please upgrade your Python version.")
    exit()
else:
    py_version = str(sys.version)
#OS warning for Windows BETA testers
if operating_system == 'Windows':
    print(f"Warning! This script is ment to be run on Pi OS. If you are not a developer, please close this script.")
import subprocess
#Installing Ollama for Linux
def installOllama():
    try:
        subprocess.run(
            ["bash", "-c", "curl -fsSL https://ollama.com/install.sh | sh"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Ollama install failed with error: {e}")
#Installing Ollama Python Pipeline for Linux
def installOllamaPython():
    try:
        subprocess.run(
            ["bash", "-c", "pip install ollama"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Ollama Python Pipeline install failed with error: {e}")
#Test If Ollama is installed
try:
    result = subprocess.run(["ollama", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode == 0:
        ollama = True
        ollama_version = str(result.stdout.strip())
    else:
        ollama = False
except FileNotFoundError:
   ollama = False
if ollama == False:
    print(f'Ollama is not installed! Please go to https://ollama.com/download to download Ollama for your device.')
    if operating_system == "Linux":
        autoInstallOllama = str(input('If you want, Ollama can be automatically installed on your system, Y/N: '))
        if  autoInstallOllama == 'y' or autoInstallOllama == 'Y':
            installOllama()
    else:
        exit()
#Check if Ollama Python Pipeline
try:
    from ollama import chat
except ImportError:
    print(f'Ollama Python Pipeline is not installed! Please install it by running pip install ollama')
    if operating_system == "Linux":
        autoInstallOllamaPython = str(input('If you want, Ollama Python Pipeline can be automatically installed, Y/N: '))
        if autoInstallOllamaPython == 'y' or autoInstallOllamaPython == 'Y':
            installOllamaPython()
    else:
        exit()
#Warn user to install models first
print('Any models you choose to use must first be installed in the terminal using ollama pull [model]')
chatmodel = str(input('Model: '))
prompt = 'user'
#Chatting interface code
while True:
    input = str(input('User: '))
    stream = chat(
        model=chatmodel,
        messages=[{'role': prompt, 'content': input}],
        stream=True,
    )
    print('AI: ', end='', flush=True)
    #Make sure the output updates before it's done generating
    for chunk in stream:
      print(chunk['message']['content'], end='', flush=True)
