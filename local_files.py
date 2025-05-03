import requests


url = 'https://www.google.com/imgres?q=chat%20gpt%20&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fe%2Fef%2FChatGPT-Logo.svg&imgrefurl=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2FChatGPT&docid=UNO7k-zT8Sb3tM&tbnid=emdo_EWia6Y9nM&vet=12ahUKEwiropup_IeNAxXiQVUIHY_MEiwQM3oECBoQAA..i&w=800&h=800&hcb=2&ved=2ahUKEwiropup_IeNAxXiQVUIHY_MEiwQM3oECBoQAA'

response = requests.get(url)

with open('spring.jpeg', mode='wb') as file:
    content = response.content
    content += b'23235656 Lev'
    file.write(content)

with open('spring.jpeg', mode='rb') as f:
    print(f.read())
