
# Google Keyword Ranking Check with Python 

Are you poor and don’t have money to buy an enterprise rank tracker? Well today is your lucky day, with this python script, 
a shell script and crontab you can automate Google rank checker in a few simple steps.
I will explain step by step how to implement this and leave it running on a daily basis.
One thing to note, currently the script does not use proxies to check for the keyword rankings, so if you are looking to run big sets of keywords google will notice this and will start showing a captcha.


**Update**: I have updated the script by adding the possibility of choosing what device you want to make the rank check. The 2 options are Mobile and Desktop. I will still leave the old script here but will change the name to rank_legacy.py.

Prerequisite for this tutorial is Python 3.



## Table of Contents 

- [Installation](#installation)
- [Running Tests](#running-tests)
- [Creating a Shell Script](#creating-a-shell-script)
- [Cronjob](#cronjob)
- [Contributing & Questions](#cintributing-and-questions)


---

## Installation

Installation of Python robobrowser

```shell
pip install robobrowser
```
After all dependencies are installed, we can start testing if the script is working fine.

## Running tests
We open the terminal and go to the folder that `rank.py` is saved and give the script executing rights.

```shell
chmod +x rank.py
```
Now we are able to call our script followed by 3 arguments: the website we are looking for, the device we want to check on this can be mobile or desktop and the keyword we want to check.

```shell
python3 rank.py [website] [device] [keyword]
```

### For example 
We want to check the website https://www.uselessthingstobuy.com/ on mobile against the keyword **nothing package**

```shell
python3 rank.py https://www.uselessthingstobuy.com/ mobile nothing package
```

This will output the keyword, the ranking of the keyword, the URL that is ranking on Google, the device you chose and the date we did this rank check.

*Make sure that the device is lower case. If you misspell the device or add capital the script will run using mobile device as default*

```shell 
nothing+package 1 https://www.uselessthingstobuy.com/product/give-nothing-for-the-person-who-has-everything/ mobile 01-07-2020
```
This will also generate a CSV file in the folder where `rank.py` is located. This will include all the information the terminal is showing.

For example:

| Keyword         	| Rank 	| URL                                                                                        	| Device 	| Date       	|
|-----------------	|------	|--------------------------------------------------------------------------------------------	|--------	|------------	|
| nothing+package 	| 1    	| https://www.uselessthingstobuy.com/product/give-nothing-for-the-person-who-has-everything/ 	| mobile 	| 01-07-2020 	|

## Creating a shell script

Now that we tested that `rank.py` works fine, we will go ahead and create a shell script that will check for multiple keywords.

We create a new `.sh` file and add the terminal commands we ran before. We add them multiple time with different keywords we want to check. We also include a time out ( `sleep` ) in between the command so that it looks like a normal behavior and Google don’t ban you. Try to put different sleep time.

```shell
#! /bin/bash

/usr/bin/python3 /path_to_my_script/rank.py [website] [device] [keyword1] 
sleep 30
/usr/bin/python3 /path_to_my_script/rank.py [website] [device] [keyword2]  
sleep 20
/usr/bin/python3 /path_to_my_script/rank.py [website] [device] [keyword3]  
sleep 30
/usr/bin/python3 /path_to_my_script/rank.py [website] [device] [keyword4]  
sleep 25
/usr/bin/python3 /path_to_my_script/rank.py [website] [device] [keyword5] 

```

After we create the shell script we would need to make the script executable

```shell
chmod +x rank.sh
```
and then to test the shell script. We go to the console and run it

```shell
./rank.sh
```
This will output 5 csv files and the output file name is composed by the date + `[keyword]` + `[device]`

## Cronjob

Now that we have our `.sh` file running fine we will set up a cronjob that will run every day at 5:00pm

In the terminal we type

```shell
crontab -e
```
Then we will press the letter i to star editing and we will add the following:

```
0 17 * * * path_to_my_script/rank.sh
```

after adding this we press esc and add `:wq` to save.

## Contributing and Questions

If you want to contribute or fix anything please feel free to do so. 

If you have any question or need help setting this up please open an issue and will try to help.












