import wikipedia
import os



os.makedirs("HADOOP/mapper-reducer/doc1-5", exist_ok=True)
os.makedirs("HADOOP/mapper-reducer/doc6-10", exist_ok=True)

# Choose 10 random articles from Wikipedia
articles = wikipedia.random(10)


# Create a file that contains the URL of the article
URL = open("HADOOP/mapper-reducer/URL.txt", "w")
# Save the articles in a file
n = 1
for i in articles:
    if n <= 5:
        # Verify if the article exists so it doesn"t overwrite the file
        if os.path.exists("HADOOP/mapper-reducer/doc1-5/File" + str(n) + ".txt") == False:
            file = open("HADOOP/mapper-reducer/doc1-5/File" + str(n) + ".txt", "w", encoding="utf-8")
            
            # Write the URL of the article in the file
            URL.write("File" + str(n) + ".txt" + "\t" + wikipedia.page(i).url + "\n")
            # Extract the content of the page in plain text
            file.write(wikipedia.page(i).content)
            file.close()
    elif n > 5 and n <= 10:
                # Verify if the article exists so it doesn"t overwrite the file
        if os.path.exists("HADOOP/mapper-reducer/doc6-10/File" + str(n) + ".txt") == False:
            file = open("HADOOP/mapper-reducer/doc6-10/File" + str(n) + ".txt", "w", encoding="utf-8")
                    
            URL.write("File" + str(n) + ".txt" + "\t" + wikipedia.page(i).url + "\n")
                    # Extract the content of the page in plain text
            file.write(wikipedia.page(i).content) 
            file.close()
    n += 1
URL.close