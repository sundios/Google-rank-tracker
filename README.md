
# Google Keyword Ranking Check with Python

Are you poor and dont have money to buy a entepriese rank tracker? Well today is your lucky day, with this python script, 
a shell script and crontab you can automate Google rank checker in a few simple steps.
I will explain step by step how to implement this and leave it running on a daily basis.
One thing to note, currently the script does not use proxies to check for the keyword rankings, so if you are looking to run big sets of keywords google will notice this and will start showing a captcha.

Im planning on adding the use of proxies, I added a timeout in between the queries so Google wont use the captcha.

Prerequisite for this tutorial is Python 3 and terminal. 


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
After all dependecies are installed we can start testing if the script is working fine.

## Running tests
We open the terminal and go to the folder that `rank.py` is saved and give the script executing rights.

```shell
chmod +x rank.py
```
Now we are able to call our script followed by 2 arguments: the webiste we are looking for and the keyword we want to check.

```shell
python3 rank.py [website] [keyword]
```

### For example 
We want to check the website https://www.uselessthingstobuy.com/ against the keyword **nothing package**

```shell
python3 rank.py https://www.uselessthingstobuy.com/ nothing package
```

This will output The keyword, the ranking of the keyword, the URL that is ranking on Google and the date we did this rank check.

```shell 
nothing+package 7 https://www.uselessthingstobuy.com/product/give-nothing-for-the-person-who-has-everything/ 16-05-2019
```
This will also generate a CSV file in the folfer where `rank.py` is located with all the information the terminal is showing.

## Creating a shell script

Now that we tested that `rank.py` works fine, we will go ahead and create a shell script that will check for multiple keywords.

We create a new `.sh` file and add the terminal commands we run before multiple time with different keywords we want to check. We also include a time out ( `sleep` )  in between the command so that it looks like a normal behavior and Google dont ban you. Try to put different sleep time.

```shell
#! /bin/bash

/usr/bin/python3 /path_to_my_script/rank.py [website] [keyword1] 
sleep 30
/usr/bin/python3 /path_to_my_script/rank.py [website] [keyword2] 
sleep 20
/usr/bin/python3 /path_to_my_script/rank.py [website] [keyword3] 
sleep 30
/usr/bin/python3 /path_to_my_script/rank.py [website] [keyword4] 
sleep 25
/usr/bin/python3 /path_to_my_script/rank.py [website] [keyword5] 

```

After we create the shell script we would need to make the script executable

```shell
chmod +x rank.sh
```
and then to test the shell script. We go to the console and run it

```shell
./rank.sh
```
This will output 5 csv files and the output file name is composed by the date + [keyword]


## Cronjob

Now that we have our sh file running fine we will set up a cronjob that will run every day at 5:00pm

In the terminal we type

```shell
crontab -e
```
Then we will press the letter i to star editing and add the following

```
0 17 * * * path_to_my_script/rank.sh
```

after adding this we press esc and add `:wq` to save.

## Contributing and Questions

If you want to contribute or fix anything please feel free to do so. 

If you have any question about setting this up please contact me and I will try to answer back.










