###Step 1: Ingest retail dataset composed of product images and production description. Ingest pipeline in OpenSearch Service generates embeddings from both text and images via the ML connector and store the embedding vectors and original data in OpenSearch KNN index.

###Step 2: User on the web application asks question about a specific product or style using text and image they upload into the web application. OpenSearch Service calls the remotly hosted models to generate vector embeddings for the search query.

###Step 3: OpenSearch Service runs the neural search. When running hybrid search and conversational search, the processors in the search pipelines intercept the search query results to run further processing if needed. Finally OpenSearch Service sends back the most relevant results to the end user.

###In lab 1 and lab 2 of this workshop, you will build lexical search, semantic search, multimodal search and hybrid search. After you create the search type components in OpenSearch Service, you will deploy the changes into a web application.

###The web application allows you to simulate a tooling for your search practioners and business units, a tooling that offers the option to test out different search types and analyze which type is more relevant to your end users and business.

###In the next steps, you will run a script to deploy a Streamlit  based web application for this purpose.

###Lexical search  refers to the process of searching for exact word matches within a text corpus. Lexical search is useful when you need to find documents containing specific terms or phrases, such as product names, part numbers, or unique identifiers. This type of search is beneficial when the user has a clear idea of the exact term they are looking for and wants to retrieve documents that contain that specific expression. In retail use case, let's assume the user is searching for "1080p touchscreen camera". In this example, the query contains several distinct terms - 1080p, touchscreen, and camera - that the user expects to find together in the search results.

###In lexical search, OpenSearch uses BM25 algorithm  to calculate the document's relevance score at search time.

###Lexical search is often the starting point for more advanced search techniques, such as phrase matching, fuzzy search, or relevance-based ranking. Leveraging lexical search can be particularly effective in scenarios where precision is critical, such as e-commerce product searches or legal document retrieval.

#Step 1: Index sample data using web application for Lexical search: reindex is done on the app but this is the code behind it. It loads everything from the YAML file.
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
#Opensearch client object
aos_client = OpenSearch(
    hosts = [{'host': <OpenSearchDomainEndpoint>, 'port': 443}],
    http_auth = <OpenSearch master credentials>,
    use_ssl = True,
    connection_class = RequestsHttpConnection
        )
#Load the dataset
items_ = yaml.load(open('/home/ec2-user/SageMaker/images_retail/products.yaml'))
batch = 0
count = 0
body_ = ''
batch_size = 50 # Bulk size
action = json.dumps({ 'index': { '_index': 'demostore-search-index' } })
#Iterating through the dataset
for item in items_: 
    count+=1

    # building the document json
    payload = {}
    payload['image_url'] = fileshort
    payload['product_description'] = item['description']
    payload['caption'] = item['name']
    payload['category'] = item['category']
    payload['price'] = item['price']
    payload['gender_affinity'] = payload['gender_affinity']
    payload['style'] = item['style']

    # Building the index request payload
    body_ = body_ + action + "\n" + json.dumps(payload) + "\n"

    # Calling bulk api when the batch size is met
    if(count == batch_size):
        response = aos_client.bulk(
        index = 'demostore-search-index',
        body = body_
        )
        batch += 1
        count = 0
        body_ = ""
            
#Step 2: Validate the created index using Dev tools in OpenSearch Dashboard: Check everything in cloudFoundation. These are the codes to check: 

GET demostore-search-index


GET demostore-search-index/_count


GET demostore-search-index/_search
{"query": {
    "match_all": {}
  },
  "size": 1
}

GET demostore-search-index/_search
{
  "query": {
    "match": {
      "product_description": "black jacket for men"
    }
  },
  "size": 5
}
#Step 3: Run lexical search in Dev Tools in OpenSearch Dashboard
#Step 4: Run lexical search in Web application
