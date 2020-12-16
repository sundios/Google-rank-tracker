
# Google Keyword Ranking Check with Python 

Are you poor and don’t have money to buy an enterprise rank tracker? Well, today is your lucky day. With this python script, 
a shell script and crontab, you can automate Google rank checker in a few simple steps.
I will explain step by step how to implement this and leave it running daily.
One thing to note, currently the script does not use proxies to check for the keyword rankings, so if you are looking to run big sets of keywords, Google will notice this and will start showing a captcha.


**Update**: I have updated the script by adding the possibility of choosing what device you want to make the rank check. The two options are Mobile and Desktop. I will still leave the old script here but will change the name to rank_legacy.py.

**Update2**: Included a keyword.xls file that will run all your keywords from there. No need to add each one of those on the `.sh` file anymore. I also added a random sleep between queries so that Google won't catch us. The script now is more simple and easy to use.

## Table of Contents 

- [Installation](#installation)
- [Running Tests](#running-tests)
- [Creating a Shell Script](#creating-a-shell-script)
- [Cronjob](#cronjob)
- [Contributing & Questions](#contributing-and-questions)

---

## Installation

Installation of Python robobrowser

```shell
pip install robobrowser
```
After all, dependencies are installed, we can start testing if the script is working fine.

## Running tests
Before running any test, we want to go into the `keywords.xls` file and add the keywords we want to check the ranks. We can add as many as we wish to, but the more keywords, the higher the chances Google will block you. (I will soon include the option of using proxies.)

After that, we open the terminal and go to the folder that `rank.py` is saved and give the script executing rights.

```shell
chmod +x rank.py
```
Now we can call our script followed by two arguments: the website we are looking for and the device we want to check on this can be mobile or desktop.

```shell
python3 rank.py [website] [device] 
```

### For example 
We want to check the website https://www.uselessthingstobuy.com/ on mobile against the keyword **nothing package** we need to include the keyword on keywords.xls file and run:

```shell
python3 rank.py https://www.uselessthingstobuy.com/ mobile
```

This will output the keyword, the ranking of the keyword, the URL that is ranking on Google, the device you chose, and the date we did this rank check.

*Make sure that the device is lower case. If you misspell the device or add capital, the script will run using mobile device as default*

```shell 
nothing+package 1 https://www.uselessthingstobuy.com/product/give-nothing-for-the-person-who-has-everything/ mobile 01-07-2020
```
This will also generate a CSV file in the folder where `rank.py` is located. This will include all the information the terminal is showing.

For example:

| Keyword         	| Rank 	| URL                                                                                        	| Device 	| Date       	|
|-----------------	|------	|--------------------------------------------------------------------------------------------	|--------	|------------	|
| nothing+package 	| 1    	| https://www.uselessthingstobuy.com/product/give-nothing-for-the-person-who-has-everything/ 	| mobile 	| 01-07-2020 	|

## Creating a shell script

Now that we tested that `rank.py` works fine, we will create a shell script that will run our python script.

We create a new `.sh` file and add the terminal commands we ran before. Since we are running everything out of a keyword.xls file to make everything easier, we can call the script with the URL we want and the device we want to check in our `rank.sh` file. 
So forget about adding multiple lines and sleep times. I included the sleep times on the script and they do random number between 1,10 so that Google wont catch us. So the only thing we need to have is the following:

```shell
#! /bin/bash

/usr/bin/python3 /path_to_my_script/rank.py [website] [device] 


```

After we create the shell script we would need to make the script executable

```shell
chmod +x rank.sh
```
and then to test the shell script. We go to the console and run it using

```shell
./rank.sh
```
This will output 5 csv files and the output file name is composed by the date + `[keyword]` + `[device]`

## Cronjob

Now that we have our `.sh` file running fine, we will set up a cronjob that will run every day at 5:00 pm

In the terminal, we type:

```shell
crontab -e
```
Then we will press the letter `i` to star editing and we will add the following:

```
0 17 * * * path_to_my_script/rank.sh
```

after adding this we press esc and add `:wq` to save.

## Contributing and Questions

If you want to contribute or fix anything please feel free to do so. 

If you have any question or need help setting this up please open an issue and will try to help.


**If you have a werkzeug Error Read this** As of February 2020 `werkzug` upgraded to 1.0.0 and RoboBrowser lazy developers havent fixed. To fix this you need to go to your Robobrowser folder on your computer something like (/Users/yourusername/opt/anaconda3/lib/python3.7/site-packages/robobrowser/) and open `browser.py` and add change ```from werkzeug import cached_property  ``` to ```from werkzeug.utils import cached_property```

Please take a look at this url for more info: [Link to issue](https://github.com/jmcarp/robobrowser/issues/93)









