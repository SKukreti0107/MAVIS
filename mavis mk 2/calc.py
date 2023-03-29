import wolframalpha
#app_id = "EUA7EU-73QT69E7E5"



# Define the chatbot function
def chatbot(user_input):
    # Initialize the Wolfram Alpha client
    client = wolframalpha.Client('EUA7EU-73QT69E7E5')
    
    #print("Hello! I'm a math chatbot. How can I help you today?")

   
    # Get user input
    user_input = input().lower()

        

    # Query the Wolfram Alpha API
    res = client.query(user_input)

    # Print the result
    try:
        result = next(res.results).text
        print("The answer is:", result)

    # Handle errors
    except StopIteration:
        print("I'm sorry, I didn't understand your question.")

