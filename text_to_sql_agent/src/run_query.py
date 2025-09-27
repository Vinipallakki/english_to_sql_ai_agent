from .agent import get_sql_agent

# def run_query(question: str):
#     agent = get_sql_agent()
#     return agent.run(question)

# if __name__ == "__main__":
#     q = "count the names of customers"
#     print(run_query(q))

from .agent import get_sql_agent

# def run_query_with_email_format(question: str) -> str:
#     """
#     Run the SQL query using the agent and return it in an email-friendly format.
#     """
#     agent = get_sql_agent()
    
#     # Generate the SQL query
#     sql_query = agent.run(question)
    
#     # Wrap it in email format
#     email_body = f"""
#     Subject: SQL Query Result

#     Hi Team,

#     The SQL query generated for the request below:

#     User Request:
#     {question}

#     Generated SQL Query:
#     {sql_query}

#     You can execute this query in BigQuery to get the results.

#     Regards,
#     Automated SQL Agent
#     """
#     return email_body

# if __name__ == "__main__":
#     q = "count the names of customers"
#     email_content = run_query_with_email_format(q)
#     print(email_content)

from .agent import get_sql_agent

def run_query_with_email_format(question: str) -> str:
    """
    Run the SQL query using the agent and return it in an email-friendly format.
    """
    agent = get_sql_agent()
    
    # Generate the SQL query
    sql_query = agent.run(question)
    
    # Wrap it in email format
    email_body = f"""
    Subject: SQL Query Result

    Hi Team,

    The SQL query generated for the request below:

    User Request:
    {question}

    Generated SQL Query:
    {sql_query}

    You can execute this query in BigQuery to get the results.

    Regards,
    Automated SQL Agent
    """
    return email_body

if __name__ == "__main__":
    # Ask the agent to join the two tables and filter for Headphones
    q = """
    Get the cost of all products in the 'Headphones' category by joining
    product_details and products tables under the same dataset.
    """
    email_content = run_query_with_email_format(q)
    print(email_content)
