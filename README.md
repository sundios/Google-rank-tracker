
# Google Keyword Ranking Check with Python 

You can see another SEO script in action here --> <a href="https://www.kwrds.ai/" rel="follow">[https://www.kwrds.ai/](https://www.kwrds.ai/)</a>


<a href="https://bmc.link/sundios" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

Are you on a tight budget and unable to purchase an enterprise rank tracker? Well, today is your lucky day. With this Python script, you can check your rankings and your competitors' rankings on both mobile and desktop in just a few seconds.

**Update**: The script has been updated to remove Robobrowser and use Beautiful Soup. I've also added a competitor check feature, and now it's easier to run. I will make a fix to include a keyword file in the future, but for now, the script is working again and includes the competitors' feature.

**Update**

## Table of Contents 

- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing & Questions](#contributing-and-questions)

---

## Installation

To use this script, you need to install its dependencies. You can do this by running the following command in your terminal:

```shell
pip install -r requirements.txt
```

Once all the dependencies are installed, you can start using the script immediately.

## Usage

To run the script and retrieve rankings for your site and competitors, you'll need to make some updates in the `rank.py` file. In line 15 of `rank.py`, you will find the following input parameters:

- keyword: Keyword we want to check.
- sitename: Your website URL.
- competitors: The URLs of the competitors you want to check.

For example, if you want to check the keyword **running shoes** and your website is https://www.adidas.com, it should look something like this:

```python
# inputs
keyword = 'running shoes'
sitename = "https://www.adidas.com/"

competitor1 = "https://www.nike.com"
competitor2 = "https://www.reebok.com"
competitor3 = "https://www.ascics.com"
competitor4 = "https://www.hoka.com"
```
Once you've updated these fields, you can run the following command in your terminal to execute the script:

```bash
python rank.py

```
## Results

The script performs two checks: one on mobile and the other on desktop. If everything goes well, you should be able to view your ranking results as well as your competitors' rankings for both mobile and desktop.

![Rankings check](rank.gif)

Additionally, the script generates an Excel (.xlsx) file in the same folder where rank.py is located. The file is named after the keyword and contains two tabs: one for mobile rankings and another for desktop rankings.

For example:
| Keyword       | Rank | URL                                               | Date       | Type         |
|---------------|------|---------------------------------------------------|------------|--------------|
| running shoes | 4    | https://www.adidas.com/us/women-running-shoes    | 09-01-2024 | My Site      |
| running shoes | 2    | https://www.nike.com/w/running-shoes-37v7jzy7ok | 09-01-2024 | Competitor  |
| running shoes | 19   | https://www.reebok.com/c/200000012/men-running-shoes | 09-01-2024 | Competitor  |
| running shoes | 8    | https://www.hoka.com/en/us/                      | 09-01-2024 | Competitor  |

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=sundios/Google-rank-tracker&type=Date)](https://star-history.com/#sundios/Google-rank-tracker&Date)


## Contributing and Questions

If you want to contribute or fix anything, please do so. 

If you have any questions or need help setting this up, please open an issue, and will try to help.












