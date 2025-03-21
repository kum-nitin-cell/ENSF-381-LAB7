import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter

def fetch_webpage():
    # Comment out if not required
    # use any url but as required by this lab copy and paste this url:https://en.wikipedia.org/wiki/University_of_Calgary
    url = input("Enter a Url to work with:")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"Successfully fetched content from {url}")
        return soup         # using the Soup as variable to fetch the entire html documents.
    except Exception as e:
        print(f"Error fetching content: {e}")
        return None

def analyze_elements(soup):
    headings = 0
    for i in range(1, 7):
        headings = headings + len(soup.find_all(f'h{i}')) # using it as h(i): h1,h2,h3,h4,h5,h6

    links = len(soup.find_all('a'))
    paragraphs = len(soup.find_all('p'))
    
    print("\nElement Counts:")
    print(f"Number of headings (h1-h6): {headings}")
    print(f"Number of links (a tags): {links}")
    print(f"Number of paragraphs (p tags): {paragraphs}")
    
    return headings, links, paragraphs

def keyword_analysis(soup):
    keyword = input("\nEnter a keyword to search for: ").lower()
    text = soup.get_text().lower()
    count = text.count(keyword)
    print(f"\nKeyword Analysis:")
    print(f"Number of counts for the {keyword}: {count}")

def word_frequency(soup):
    text = soup.get_text()
    words = text.lower().split()
    word_counts = Counter(words)
    top_5 = word_counts.most_common(5)
    
    print("\nTop 5 Most Frequent Words:")
    for word, count in top_5:
        print(f"'{word}': {count} times")

def find_longest_paragraph(soup):
    paragraphs = soup.find_all('p')
    longest_para = ""
    max_words = 0
    
    for p in paragraphs:
        text = p.get_text().strip()
        words = text.split()
        if len(words) >= 5 and len(words) > max_words:
            max_words = len(words)
            longest_para = text
    
    print("\nLongest Paragraph Analysis:")
    print(f"Word count: {max_words}")
    print(f"Content: {longest_para[:100]}..." if len(longest_para) > 100 else longest_para)

def visualize_results(headings, links, paragraphs):
    labels = ['Headings', 'Links', 'Paragraphs']
    values = [headings, links, paragraphs]
   
    plt.bar(labels, values, color = 'violet' ) # changed colour for the bar.
    plt.title('Group # 48 ')  
    plt.ylabel('Count')
    plt.show()

def main():
    soup = fetch_webpage()
    if soup:
        # printing the entire html structure.
        # can be comment out to display the entire structure of the html page
        #print(soup.prettify())
        
        # retrieving headings, links, paragragh using the function below
        headings, links, paragraphs = analyze_elements(soup)
        
        # retrieving the keyword analysis results.
        keyword_analysis(soup)
        
        # Word frequency analysis
        word_frequency(soup)
        
        # retrieving longest_paragraph results.
        find_longest_paragraph(soup)
        
        # Visualization
        visualize_results(headings, links, paragraphs)

if __name__ == "__main__":
    main()