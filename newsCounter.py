'''
Electric Electronic Engineering.
Mert Palaoğlu(2221241008), 
Yemliha Altıntas(2221241009), 
Muhammed Mustafa Sağlam(2221241551).

API'S LINK=https://newsapi.org/

'''

import requests # Lib to get information from websites, In this code we get info from "news API".
import matplotlib.pyplot as plt # Library used to visualize information graphically
import tkinter as tk # Lib to create an User Interface with Tkinter.

api_key = '83b63be78c57485b924e9ac757bee322' #User's API key.
keywords = [] #We created an empty list where the keywords that the user will enter will be stored here.

def take_keyword():
    keyword = entry.get().strip()  # Remove leading/trailing spaces from the keyword.
    if keyword:  # Check if the keyword is not empty
        keywords.append(keyword)
        label_result.config(text="Keyword added: {}".format(keyword))
        entry.delete(0, tk.END)
    else:
        label_result.config(text="Please enter a valid keyword.")

''' User interface for getting the keywords: '''
root = tk.Tk()
root.title('News Counter 2023')
root.geometry("400x200")# We set the size of the window.

label = tk.Label(root, text="Enter Keyword:") # We create a label.
label.pack() # We place the label in the window.

entry = tk.Entry(root)# We create an entry box.
entry.pack()# We place the input box in the window.

button = tk.Button(root, text="Add Keyword", command=take_keyword) #First button for getting keywords.
button.pack()
button2= tk.Button(root, text='Find Articles', command=root.destroy) #Second button for closing this tab and starting the graph part.
button2.pack()

label_result = tk.Label(root, text="")
label_result.pack() # We create a result label and put it in the window.

root.mainloop() # We start the window to get input from the user.


'''Loop and count part with API's URL '''

sources = ['bbc-news', 'cnn', 'reuters', 'google-news'] #We use 4 main new sources for this API. 
source_count = {}

for source in sources:
    try: # Construct the URL for the API request by joining the keywords and source with appropriate parameters
        url = f'https://newsapi.org/v2/everything?q={" OR ".join(keywords)}&sources={source}&apiKey={api_key}'
        # Send a GET request to the API and store the response.
        response = requests.get(url) 
        # Extract the JSON data from the response
        data = response.json()
        #print(data) if you wanna see the articles you open here.
       
        articles = data['articles']
        source_count[source] = len(articles)
        # Store the count of articles for the current news source in the source_count dictionary.
    except requests.RequestException as e:
        print("An error occurred while fetching data:", e)
        # If an error occurs while fetching data, print the error message


'''Matplotlib part for Graphic'''
x = list(source_count.keys())
y = list(source_count.values())


plt.bar(x, y)
# Set the labels and title for the chart
plt.xlabel('News Sources')
plt.ylabel('News Count')
plt.title('News Count by Source for Keywords: {}'.format(', '.join(keywords)))
plt.xticks(rotation=0) # Rotate the x-axis labels if necessary we didn't.
plt.show() # Display the chart
