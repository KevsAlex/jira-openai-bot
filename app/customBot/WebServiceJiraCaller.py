import requests


class WebServiceJiraCaller:
    def __init__(self, base_url, auth_token):
        """
        Initializes the WebServiceJiraCaller with the base URL of the JIRA instance
        and the authorization token.

        :param base_url: The base URL of the JIRA instance.
        :param auth_token: The personal access token for authorization.
        """
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Basic {auth_token}',
            'Content-Type': 'application/json',
        }

    def search_tickets(self, fields, jql):
        """
        Searches for JIRA tickets based on the given fields and JQL query.

        :param fields: A string of comma-separated field names to include in the response.
        :param jql: The JQL query string to use for the search.

        :return: A response object from the requests library.
        """
        params = {
            'fields': fields,
            'jql': jql
        }
        response = requests.get(f'{self.base_url}/rest/api/3/search', headers=self.headers, params=params)

        return response.text


# Example usage
if __name__ == "__main__":
    # Substitute your_actual_base_url and your_actual_auth_token with your actual JIRA base URL and API token
    jira_caller = WebServiceJiraCaller('https://CHANGE_ME.atlassian.net', 'your_actual_auth_token')
    fields = 'description'
    jql = 'assignee IN (currentUser()) AND statusCategory in ("To Do", "In Progress") ORDER BY created DESC'
    response = jira_caller.search_tickets(fields, jql)
    if response.status_code == 200:
        print(response.json())  # Print the JSON response if successful
    else:
        print('Failed to fetch JIRA tickets:', response.status_code)
