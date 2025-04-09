Agents for Amazon Bedrock  empowers you to build agentic workflows that break down user-requested tasks into multiple steps. These Agents use developer-provided instructions to create orchestration plans and execute them by invoking APIs and tools, ultimately providing a final response to the end user.

An action group  defines actions/tools that the agent can call to perform user's task. You can define action groups by setting up a lambda function  with the parameters that the agent needs to elicit from the user. With this option, you can simplify the action group creation process and set up the agent to elicit a set of parameters that you define. You can then pass the parameters on to your application and customize how to use them to carry out the action in your own systems.

In part 2 of this lab, you will leverage OpenSearch ML search types(e.g. Lexical search, vector search, multimodal search), use them as actions for Bedrock agent and build a shopping assistant. This shopping assistant, through a streamlit UI, will give recommendations for your product searches using multimodal retrieval capabilities of OpenSearch Service and generative capabilities of large language models.

The Bedrock agent and the corresponding lambda function have been already created for you by the CloudFormation template.

The following depicts the solution workflow from left to right,

The Streamlit Web application is hosted on Amazon SageMaker instance. Once you ask your question on the web application, the application invokes the Bedrock agent with the user query.
The Bedrock agent decides on the right action to perform in order to answer user's query and pass the required parameters as an event to the action. Here, an action is nothing but a subset of code inside the lambda function. Every action has its respective definiton that the agent uses to decide which action to call based on the user's query.
The Lambda function calls the back-end services based on the subset of code: OpenSearch for executing a search (text or multimodal or hybrid search) OR other services like Amazon Bedrock when there is a need to use foundation models like Titan Image Generator.
The Lambda function collects the response from the respective service and returns the response to the Bedrock agent.
The agent, using the response as the context, prepares the final answer based on the user query and returns it to the web application. When the agent finds the lambda response is not relevant to the user query, it repeats steps 2-4 until it decides whether the response matches the user's query. Additionally, the agent stores the user's questions and the responses as conversational memory that it looks up when required for the further user's questions.
In this lab, Amazon Bedrock Agent has an action group with multiple actions defined in the group. Each action will run a specific task and establish a business logic. All these actions are defined in the handler method  of the same lambda function.

The Bedrock agent used in this lab have been already created for you by the CloudFormation template. Learn more about Bedrock Agent configurations like instructions, action groups and definitions.

On AWS Console, navigate to Bedrock Agents 

Click on the existing agent ai-shopping-assistant.  
Navigate through the different action group functions, learn about the related instructions and parameters defined for each action. The following are the defined action group functions and their high level descriptions,
get_relevant_items_for_image: Retrieves relevant products based on the provided image and text query by running a multimodal search.
generate_image: Generates images based on the provided text description.
get_product_details: Retrieves details about a specific product by looking up the opensearch index.
get_relevant_items_for_text: Retrieves relevant products based on the provided text query by running a semantic search.
get_any_general_recommendation: Provide fashion related recommendations related to a specific product or in general.
retrieve_with_keyword_search: Retrieves relevant products based on the provided text query by running a lexical search
