# clash_subscriptions

This is a clash subscription script base on linux. 
This script starts clash with yacd panel, you may put this file inside yacd project, `python3 yacd_start` to start both yacd panel and a new clash instance. 

To configure your subscriptons, navigate into your clash working directory, and create a new YAML file called `subscriptions.yaml`. 
```sh
touch subscriptions.yaml
```
and then add your subscriptions like this: 

```yaml
subscriptions: 
  sub1: url1
  sub2: url2
```

now your clash directory would look like this: 

```sh
./
├── config.yaml
├── sub1.yaml
├── Country.mmdb
├── sub2.yaml
└── subscriptions.yaml
```
finally, configure your subscriptons in the `yacd_start.py`: 

```py
17    questions = [List("clash_subscription", message="Which database? ", choices=[
18                      "cordCloud", "speeder"]), # change the subscriptions to your own ones
19                 Text('clash_directory',
20                      message="Clash directory? ", default="/home/ryland/Documents/clash")]  # change your directory to your own
```

Now you can run script with: 

```sh
ipython3 yacd_start.py
```

