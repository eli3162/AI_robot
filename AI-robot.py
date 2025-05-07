import sys
if sys.version_info.major < 3:
    print("This script requires Python 3 or higher. Please upgrade your Python version.")
    exit()
else:
    py_version = str(sys.version)
import subprocess
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
    print('Ollama is not installed! Please go to https://ollama.com/download to download Ollama for your device.')
    print('The Script will now exit')
    exit()
try:
    from ollama import chat
except ImportError:
    print('Ollama Python Pipeline is not installed! Please install it by running pip install ollama')
    exit()
chatmodel = str(input('Model: '))
prompt = 'user'
while True:
    input = str(input('User: '))
    stream = chat(
        model=chatmodel,
        messages=[{'role': prompt, 'content': input}],
        stream=True,
    )
    print('AI: ', end='', flush=True)
    for chunk in stream:
      print(chunk['message']['content'], end='', flush=True)
