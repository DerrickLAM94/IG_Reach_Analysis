import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor

data = pd.read_csv("/Users/derricklam/Desktop/Data analust/Instagram data.csv", encoding = 'latin1')
print(data.head())
print(data.isnull().sum())
print(data.info())

# distribution of impressions From HOME
plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Home")
sns.distplot(data['From Home'])
plt.show()

# Distribution of Impressions From Hashtags
plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Hashtags")
sns.distplot(data['From Hashtags'])
plt.show()

# Impressions From various sources on Instagram:
home = data['From Home'].sum()
hashtags = data['From Hashtags'].sum()
explore = data["From Explore"].sum()
other = data["From Other"].sum()

labels = ['From Home', 'From Hasgtags', 'From Explore', 'From Other']
values = [home, hashtags, explore, other]

fig = px.pie(data, values=values, names=labels, title='Impressions on Instagram Posts From Various Sources, hole=0.5')
fig.show()

# Analyzing Content
text = " ".join(i for i in data.Caption)
stopwords = set(STOPWORDS)
wordCloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure(figsize=(12, 10))
plt.imshow(wordCloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# create a wordcloud of the caption column
text = " ".join(str(i) for i in data.Caption) 
stopwords = set(STOPWORDS)
wordCloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.style.use('classic')
plt.figure(figsize=(12, 10))
plt.imshow(wordCloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# create a wordcloud of the hashtags column
text = " ".join(str(i) for i in data.Hashtags) 
stopwords = set(STOPWORDS)
wordCloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.style.use('classic')
plt.figure(figsize=(12, 10))
plt.imshow(wordCloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Relationship Betweem Likes and Impressions
figure = px.scatter(data_frame = data, x="Impressions",
                    y="Likes", size="Likes", trendline="ols",
                    title = "Relationship Betweem Likes and Impressions")
figure.show()

# Relationship Between comments and Total
figure = px.scatter(data_frame = data, x="Impressions", y="Comments", size="Comments", trendline="ols",
                    title = "Relationship Between comments and Total")
figure.show()

# Relationship Between Shares and Total Impressions
figure = px.scatter(data_frame = data, x = "Impressions", y="Shares", size="Shares", trendline="ols",
                    title="Relationship Between Shares and Total Impressions")
figure.show()

# Relationship Between Post Saves and Total Impressions
figure = px.scatter(data_frame = data, x = "Impressions", y="Saves", size="Saves", trendline="ols",
                    title="Relationship Between Post Saves and Total Impressions")
figure.show()

conversion_rate = (data['Follows'].sum() / data["Profile Visits"].sum()) * 100
print(conversion_rate)

figure = px.scatter(data_frame = data, x="Profile Visits",
                    y="Follows", size="Follows", trendline="ols",
                    title = "Relationship Between Profile Visits and Followers Gained")
figure.show()

# Instagram Reach Prediction Model
x = np.array(data[["Likes", "Saves", "Comments", "Shares", "Profile Visits", "Follows"]])
y = np.array(data["Impressions"])
xtrain, xtest, ytrain, ytest, = train_test_split(x, y, 
                                                 test_size=0.2,
                                                 random_state=42)
model = PassiveAggressiveRegressor()
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print("Model Score on Test Data:", score)

# features = [['Likes', 'Saves', 'Comments', 'Shares', 'Profile Visits', 'Follows']]
features = np.array([[282.0, 233.0, 4.0, 9.0, 165.0, 54.0]])
prediction = model.predict(features)
print(prediction)
