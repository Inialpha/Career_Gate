#!/bin/node

url = 'https://newsapi.org/v2/everything?apikey=a73a26f264ce491d9d5769d880731b2e'


const apiKey = 'a73a26f264ce491d9d5769d880731b2e';
const query = 'job and career'; 

// Make API request using your preferred method (e.g., fetch, axios, etc.)
fetch(`https://api.cognitive.microsoft.com/bing/v7.0/news/search?q=${query}`, {
  headers: {
    'Ocp-Apim-Subscription-Key': apiKey,
  },
})
  .then(response => response.json())
  .then(data => {
    // Accessing the first news article's URL
    const firstArticleUrl = data.value[0].url;

    // Now you can fetch the content of the news article using the obtained URL
    fetch(firstArticleUrl)
      .then(response => response.text())
      .then(articleContent => {
        // 'articleContent' now contains the HTML or text content of the news article
        console.log(articleContent);
      })
      .catch(error => {
        console.error('Error fetching article content:', error);
      });
  })
  .catch(error => {
    console.error('Error fetching news:', error);
  });

