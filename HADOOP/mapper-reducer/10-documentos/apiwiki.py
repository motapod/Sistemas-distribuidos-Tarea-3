import wikipedia
import os

os.makedirs('HADOOP/mapper-reducer/10-documentos/doc1-5', exist_ok=True)
os.makedirs('HADOOP/mapper-reducer/10-documentos/doc6-10', exist_ok=True)

# Choose 10 random articles from Wikipedia
articles = wikipedia.random(10)
# print(articles)

# Create a file that contains the URL of the article
URL = open('HADOOP/mapper-reducer/10-documentos/URL.txt', 'w')
# Save the articles in a file
n = 1
for i in articles:
    if n <= 5:
        # Verify if the article exists so it doesn't overwrite the file
        if os.path.exists('HADOOP/mapper-reducer/10-documentos/doc1-5/File' + str(n) + '.txt') == False:
            file = open('HADOOP/mapper-reducer/10-documentos/doc1-5/File' + str(n) + '.txt', 'w')
            # Extract the content of the page in plain text
            file.write(wikipedia.page(i).content)
            # Write the URL of the article in the file
            URL.write('File' + 'str(n)' + '.txt' + '\t' + wikipedia.page(i).url + '\n')

            file.close()

        elif n > 5 and n <= 10:
                # Verify if the article exists so it doesn't overwrite the file
                if os.path.exists('HADOOP/mapper-reducer/10-documentos/doc6-10/File' + str(n) + '.txt') == False:
                    file = open('HADOOP/mapper-reducer/10-documentos/doc6-10/File' + str(n) + '.txt', 'w')
                    # Extract the content of the page in plain text
                    file.write(wikipedia.page(i).content) 
                    URL.write('File' + 'str(n)' + '.txt' + '\t' + wikipedia.page(i).url + '\n')
             
                    file.close()
                    n += 1
URL.close