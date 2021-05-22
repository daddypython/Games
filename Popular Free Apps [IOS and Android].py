#!/usr/bin/env python
# coding: utf-8

# ## FREE APPS IN ENGLISH LANGUAGE THAT ATTRACT USERS

# ### Apps
# Android and iOS mobile apps. 
# 
# ### Goal: 
# To find out what type of apps are likely to attract more users on both the Apple Store and Google Play.
# 
# ### End Goal:
# To develop profitable app(s) for Apple Store and Google Play.

# In[233]:


class Data:
#-------------------------------------------------------------------#
    def header(dataset):
        header = dataset[0]
        return header
#-------------------------------------------------------------------#
    def data_without_header(dataset):
        dataset = dataset[1:]
        return dataset
#-------------------------------------------------------------------#
    def explore_data(dataset):
        dataset_slice = dataset[0:3]
        print("Number of rows (without header):", len(dataset))
        print("Number of columns(without header):", len(dataset[0]))
        print('\n')
        print("First 3 rows:")
        print('\n')
        for row in dataset_slice:
            print(row)
            print('\n')
#-------------------------------------------------------------------#
    def missing_value(dataset):
        len_row = 0
        header = Data.header(dataset)
        print("Row with missing value:")
        print('\n')
        for row in dataset:
            if len(header) != len(row):
                len_row += 1
                print(row)
                print("Row Index Number:", dataset.index(row))
        print("Number of rows with missing value:", len_row)
        print('\n')
#-------------------------------------------------------------------#
    def duplicate_row(dataset, integer):
        duplicate_entry = []
        unique_entry = []
        for row in dataset:
            value = row[integer]
            if value in unique_entry:
                duplicate_entry.append(value)
            else:
                unique_entry.append(value)  
        print("Duplicate Entries:")
        print('\n')
        print("{num} duplicate entries".format(num=len(duplicate_entry), data=dataset))   
#-------------------------------------------------------------------#
    def is_english(string):
        app_not_eng = 0           
    
        for character in string:
            if ord(character) > 127:
                app_not_eng += 1
       
        if app_not_eng > 3:
            return False
        else:
            return True
#-------------------------------------------------------------------#
    def free(price):
        if price == '0.0' or price == '0':
            return True
        else:
            return False


# In[1]:


from csv import reader

file = open('googleplaystore.csv', encoding="utf8")
read = reader(file)
android = list(read)
android_header = Data.header(android)
android = Data.data_without_header(android)

file = open('AppleStore.csv', encoding="utf8")
read = reader(file)
ios = list(read)
ios_header = Data.header(ios)
ios = Data.data_without_header(ios)


# ### IOS Data

# In[235]:


print("Header:")
print('\n')
print(ios_header)
print('\n')
Data.explore_data(ios)
Data.missing_value(ios)
Data.duplicate_row(ios, 0)


# ### Android Data

# In[236]:


print("Header:")
print('\n')
print(android_header)
print('\n')
Data.explore_data(android)
Data.missing_value(android)
Data.duplicate_row(android, 0)


# #### 1. Deleting row with missing value [index number 10472].

# In[237]:


del(android[10472])
print("Number of rows after deletion:", len(android))


# #### 2. Removing duplicate entries.

# In[238]:


reviews_max = {}
for row in android:
    name = row[0]
    n_reviews = float(row[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

android_clean = []
already_added = []

for row in android:
    name = row[0]
    n_reviews = float(row[3])
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        android_clean.append(row)
        already_added.append(name)
print("Number of rows after removing duplicate entries:", len(android_clean))


# ### Extracting apps that are in English language. 

# In[239]:


ios_english = []
android_english = []

for row in ios:
    name = row[1]
    if Data.is_english(name):
        ios_english.append(row)

for row in android_clean:
    name = row[0]
    if Data.is_english(name):
        android_english.append(row)   


# In[240]:


print("English apps in IOS Data:", len(ios_english))
print('\n')
print("English apps in Android Data:", len(android_english))


# ### Extracting English apps that are free. 

# In[241]:


ios_final = []
android_final = []

for row in ios_english:
    price = row[4]
    if Data.free(price):
        ios_final.append(row)
        
for row in android_english:
    price = row[7]
    if Data.free(price):
        android_final.append(row)
        
print("Free English apps in IOS Data:", len(ios_final))
print('\n')
print("Free English apps in Android Data:", len(android_final))
    
    


# ### Each genre/ category as % of the total apps. 

# In[242]:


def freq_table(dataset, index):
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    
    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[key] = percentage 
    
    return table_percentages


def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
        
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


# In[245]:


print('\n')
print("IOS apps in % of total apps:")
print('\n')
display_table(ios_final, -5)


# In[246]:


print("Android apps in % of total apps:")
print('\n')
display_table(android_final, 1)
print('\n')


# ### PRELIMINARY OBSERVATION
# 
# ##### Most common genre:
# Android Apps: Family (18.90%)
# IOS Apps: Games (58.16%)
# 
# ##### Runner-up
# Android Apps: Games (9.72%)
# IOS Apps: Entertainment (7.88%)
# 
# ##### General impression
# 1. Gaming apps accounts for mostalrge number of  of the apps.
# 2. Most of the apps desifned are not for practical purpose.
# 3. Large number of Gaming apps seems to suggest that there is more demand for gamings apps. This gives the general impression that gaming apps have large number of users (but this may not be necessarily accurate and data needs to be analysed).
# 
# ##### Preliminary Recommendation
# 1. If the end goal is to develop and add profitable app on both the Apple Store and Google Play, then more resources should be spent on developing gaming / fun apps. 

# ###  Average number of user ratings for each genre

# In[247]:


print("IOS:")
print('\n')
genres_ios = freq_table(ios_final, -5)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios_final:
        genre_app = app[-5]
        if genre_app == genre:            
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)
    
### standalone code ###
### def avg_rating(dataset, index):
###    prime_genre = {}
###    prime_total = {}
###    for row in dataset:
###        genre = row[index]

###        rating = float(row[5])
###        if genre in prime_genre:
###            prime_genre[genre] += rating
###            prime_total[genre] += 1
###        else:
###            prime_genre[genre] = rating
###            prime_total[genre] = 1

###    so_avg = {}
###    for genre in prime_genre and prime_total:
###        average_rating = prime_genre[genre] / prime_total[genre]
###        so_avg[genre] = average_rating
    
###    return so_avg


# ##### Most Popular Apps by Genre on the App Store (IOS Apps)
# On average, navigation apps have the highest number of user reviews, but this figure is heavily influenced by Waze and Google Maps.
# 
# The same pattern applies to social networking apps, where the average number is heavily influenced by a few giants like Facebook, Pinterest, Skype, etc. 
# 
# Same applies to music apps, where a few big players like Pandora, Spotify, and Shazam heavily influence the average number.
# 
# The average number of ratings seem to be skewed by very few apps which have hundreds of thousands of user ratings, while the other apps may struggle to get past the 10,000 threshold. 
# 
# We could get a better picture by removing these extremely popular apps for each genre and then rework the averages.
# 
# Reference apps have 74,942 user ratings on average, but it's actually the Bible and Dictionary.com which skew up the average rating.However, this niche seems to show some potential. One thing we could do is take another popular book and turn it into an app where we could add different features besides the raw version of the book. This might include daily quotes from the book, an audio version of the book, quizzes about the book, etc. On top of that, we could also embed a dictionary within the app, so users don't need to exit our app to look up words in an external app.
# 
# This idea seems to fit well with the fact that the App Store is dominated by for-fun apps. This suggests the market might be a bit saturated with for-fun apps, which means a practical app might have more of a chance to stand out among the huge number of apps on the App Store.
# 
# Other genres that seem popular include weather, book, food and drink, or finance. The book genre seem to overlap a bit with the app idea we described above, but the other genres don't seem too interesting to us:
# 
# Weather apps — people generally don't spend too much time in-app, and the chances of making profit from in-app adds are low. Also, getting reliable live weather data may require us to connect our apps to non-free APIs.
# 
# Food and drink — examples here include Starbucks, Dunkin' Donuts, McDonald's, etc. So making a popular food and drink app requires actual cooking and a delivery service, which is outside the scope of our company.
# 
# Finance apps — these apps involve banking, paying bills, money transfer, etc. Building a finance app requires domain knowledge, and we don't want to hire a finance expert just to build an app.

# In[251]:


print("Android:")
print('\n')

categories_android = freq_table(android_final, 1)
for category in categories_android:
    total = 0
    len_category = 0
    for app in android_final:
        category_app = app[1]
        if category_app == category:
            n_installs = app[5]
            n_installs = n_installs.replace(',', '')
            n_installs = n_installs.replace('+', '')
            total += float(n_installs)
            len_category += 1
    avg_n_installs = total / len_category
    print(category, ':', avg_n_installs)


# ##### Most Popular Apps by Genre on the App Store (IOS Apps)
# 
# On average, communication apps have the most installs: 38,456,119. This number is heavily skewed up by a few apps that have over one billion installs (WhatsApp, Facebook Messenger, Skype, Google Chrome, Gmail, and Hangouts), and a few others with over 100 and 500 million installs. If we removed all the communication apps that have over 100 million installs, the average would be reduced roughly ten times. 
# 
# 
# We see the same pattern for the video players category, which is the runner-up with 24,727,872 installs. The market is dominated by apps like Youtube, Google Play Movies & TV, or MX Player. The pattern is repeated for social apps (where we have giants like Facebook, Instagram, Google+, etc.), photography apps (Google Photos and other popular photo editors), or productivity apps (Microsoft Word, Dropbox, Google Calendar, Evernote, etc.).
# 
# Again, the main concern is that these app genres might seem more popular than they really are. Moreover, these niches seem to be dominated by a few giants who are hard to compete against.
# 
# The game genre seems pretty popular, but previously we found out this part of the market seems a bit saturated, so we'd like to come up with a different app recommendation if possible.
# 
# The books and reference genre looks fairly popular as well, with an average number of installs of 8,767,811. It's interesting to explore this in more depth, since we found this genre has some potential to work well on the App Store, and our aim is to recommend an app genre that shows potential for being profitable on both the App Store and Google Play.
# 
# The book and reference genre includes a variety of apps: software for processing and reading ebooks, various collections of libraries, dictionaries, tutorials on programming or languages, etc. It seems there's still a small number of extremely popular apps that skew the average:
# 
# 
# Google Play Books : 1,000,000,000+
# Bible : 100,000,000+
# Amazon Kindle : 100,000,000+
# Wattpad Free Books : 100,000,000+
# Audiobooks from Audible : 100,000,000+
# 
# However, it looks like there are only a few very popular apps, so this market still shows potential. 
# 
# We also notice there are quite a few apps built around the book Quran, which suggests that building an app around a popular book can be profitable. It seems that taking a popular book (perhaps a more recent book) and turning it into an app could be profitable for both the Google Play and the App Store markets.
# 
# However, it looks like the market is already full of libraries, so we need to add some special features besides the raw version of the book. This might include daily quotes from the book, an audio version of the book, quizzes on the book, a forum where people can discuss the book, etc.

# ### Conclusion
# 
# #### Validation Strategy (Steps): 
# 1. Build a minimal Android version of the app, and add it to Google Play.
# 2. If the app has a good response from users, we then develop it further.
# 3. If the app is profitable after six months, we also build an iOS version of the app and add it to the App Store.
# 
# The above steps would assist:
# 1. in finding out app profiles that are successful on both Apple Store and Google Play. 
# 2. the company to minimize risks and overhead.
# 
# In this project, we analyzed data about the App Store and Google Play mobile apps with the goal of recommending an app profile that can be profitable for both markets.
# 
# We conclude that taking a popular book (perhaps a more recent book) and turning it into an app could be profitable for both the Google Play and the App Store markets. The markets are already full of libraries, so we need to add some special features besides the raw version of the book. This might include daily quotes from the book, an audio version of the book, quizzes on the book, a forum where people can discuss the book, etc.
# 
