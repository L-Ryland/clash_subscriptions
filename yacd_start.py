
from IPython import get_ipython
get_ipython().system('pip3 install pyyaml requests yaml')

# %%
import subprocess
import requests
import yaml
from inquirer import Confirm, List, Text, prompt

print("Do you wannt to start clash? (y/n)")
questions = [
    Confirm("start_clash_flag", message="Do you wannt to start claysh? ")
]
answer = prompt(questions)
if (answer["start_clash_flag"]):
    questions = [List("clash_subscription", message="Which database? ", choices=[
                      "cordCloud", "speeder"]),
                 Text('clash_directory',
                      message="Clash directory? ", default="/home/ryland/Documents/clash")]
    answer = prompt(questions)
    clash_subscription = answer["clash_subscription"]
    clash_directory = answer["clash_directory"] + '/'
    filename = clash_directory + clash_subscription + '.yaml'
    subprocess.run(['killall', 'clash'], shell=False)
    with open(clash_directory + 'subscriptions.yaml', 'r') as stream:
        try: 
            url = yaml.safe_load(stream)["subscriptions"][clash_subscription]
        except yaml.YAMLError as error:
            print(error)
    print("Updating database ", clash_subscription, " ...")
    file = open(file=filename, mode='w')
    file.write(requests.get(url).text)
    file.close()
    subprocess.run(['nohup clash -f ' + filename + ' > /dev/null 2>&1 &'], cwd=clash_directory, shell=True)
print('Killing yacd panel process previously started ...')
subprocess.run(["sudo kill -9 $(sudo netstat -nlp | grep 3000 | awk '{print $7}' | awk -F'/' '{print $1}') "], shell=True, stderr=open("/dev/null", 'w'))
subprocess.run(['nohup yarn start --host > /dev/null 2>&1 &'], shell=True)
print("\nSuccess!")
