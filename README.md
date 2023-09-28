Here is a Github README for the Instagram Reach Analysis using Python article:

# Instagram Reach Analysis using Python

This repository contains code and data for analyzing and predicting Instagram reach using Python.

## Case Study Tasks

The case study asks to analyze and predict the reach of the Instagram account based on the data provided. Some key tasks include:

Exploratory data analysis of impressions, likes, comments, etc.
Visualizing impressions by source
Analyzing post captions and hashtags
Examining relationships between metrics
Building a model to predict post reach

## The Dataset

The instagram_data.csv file contains data on 99 Instagram posts, with the following features:

Impressions: Number of impressions (reach)
From_Home: Reach from home feed
From_Hashtags: Reach from hashtags
From_Explore: Reach from explore
From_Other: Reach from other sources
Saves: Number of saves
Comments: Number of comments
Shares: Number of shares
Likes: Number of likes
Profile_Visits: Number of profile visits
Follows: Number of new followers
Caption: Post caption text
Hashtags: Hashtags used

## Usage

The `Instagram.csv` file contains the dataset. The Jupyter notebook `instagram_reach.ipynb` contains the full code and analysis from the article.

To use:

1. Clone this repository
2. Install dependencies: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `scikit-learn` 
3. Run the notebook and follow along!

## Contributing

Contributions to expand or improve this analysis are welcome! Feel free to open issues and submit pull requests.

## Reference

The original case study: https://statso.io/instagram-reach-analysis-case-study/
Kharwal, Aman. "Instagram Reach Analysis using Python." *The Clever Programmer*, 22 Mar 2022. https://thecleverprogrammer.com/2022/03/22/instagram-reach-analysis-using-python/

## The Analysis Result

distribution of impressions received from Hashtags

<img width="996" alt="Distribution of Impressions From Hashtags" src="https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/13fedbab-d867-4fd6-a124-d0f782d29388">

Hashtags help categorize posts on Instagram so more people see them. Looking at the hashtag impressions shows that hashtags don't reach all posts. But hashtags do help reach many new users.

distribution of impressions received from Homes
<img width="993" alt="distribution of impressions From Home" src="https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/64490514-f9d1-4a38-b586-4d04cdcddc01">


The number of impressions I get from the followers shows how many of  posts are reaching by the followers. Looking at these home impressions, I can see that it's difficult to reach all of my followers with each post.

percentage of impressions from various sources

![Impressions From various sources on Instagram](https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/0300b5c0-0c89-497d-9a6f-318d6668035b)

So the above donut plot shows that almost 44.1 per cent of the reach is from my followers, 33.6 per cent is from hashtags, 19.2 per cent is from the explore section, and 3.05 per cent is from other sources.

analyze the content of the Instagram posts

The dataset has two columns: caption and hashtags. These columns show what post on Instagram.

Let's make a wordcloud of the captions. This shows the words who use most in Instagram captions.

<img width="747" alt=" create a wordcloud of the caption column" src="https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/4e7ccf68-95a5-4490-93df-42f798cb5bb0">

<img width="747" alt=" create a wordcloud of the hashtags column" src="https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/ed115c7e-860e-4233-a519-650ead2fab4a">

The result showing the most used words in the caption of ig posts is data science and machine learning 

Analyzing Relationships
Now let’s analyze relationships to find the most important factors of our Instagram reach. It will also help us in understanding how the Instagram algorithm works.

The relationshp between Likes and impressions

![Relationship Betweem Likes and Impressions](https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/9b995e06-9e96-41bf-84ee-4bceb33a487b)

There is a linear relationship between the number of likes and the reach I got on Instagram.

The relationship between comments and total impressions

![Relationship Between comments and Total](https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/ffad9813-7133-41ff-9402-45eb1c49a73a)

it looks like the number of comments we get on a post doesn't affect its reach.

The relationship between Shares and impressions

![Relationship Between Shares and Total Impressions](https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/665bff6e-d318-41d4-9497-715401da2a45)

A more number of shares will result in a higher reach, but shares don’t affect the reach of a post as much as likes do

Convenrsion Rate

<img width="615" alt="螢幕截圖 2023-09-28 下午5 55 23" src="https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/50219eea-88de-449c-b96e-fc2649e03cc9">
<img width="136" alt="螢幕截圖 2023-09-28 下午5 56 43" src="https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/9b812e90-f80c-4d2f-b525-10b041486649">

the conversation rate of the ig account is 41% which is a pretty good conversion rate. 

IG reach prediction model 

<img width="653" alt="螢幕截圖 2023-09-28 下午5 59 09" src="https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/95408c51-5440-410c-a37d-d806eb5bce16">
<img width="329" alt="螢幕截圖 2023-09-28 下午6 00 05" src="https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/3e8e2689-4e40-45f3-965d-39d8096a016f">

predict the reach of an Instagram post by giving inputs to the machine learning model:
<img width="615" alt="螢幕截圖 2023-09-28 下午5 59 26" src="https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/e911c76c-ce26-470f-8f3e-c52e6e9e2b89">
<img width="122" alt="螢幕截圖 2023-09-28 下午6 00 15" src="https://github.com/DerrickLAM94/IG_Reach_Analysis/assets/140989898/bd73c332-252d-457d-8ec9-4691e144b775">

