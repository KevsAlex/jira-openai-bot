from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel

from .WebServiceJiraCaller import WebServiceJiraCaller
from .JiraTicketSearchInput import *
import dotenv
import os
class JiraTicketTool(BaseTool):
    name = "get_jira_tickets"
    description = "Used to find tickets assign to current user"
    args_schema: Optional[Type[BaseModel]] = JiraTicketSearchInput

    def _run(self,jql):
        print("request to Jira !")
        base_url = 'https://CHANGE_ME.atlassian.net'

        dotenv.load_dotenv()
        token=os.getenv('JIRA_TOKEN')
        service_caller = WebServiceJiraCaller(base_url, token)
        response = service_caller.search_tickets('summary,created,reporter', jql)
        return response


    def _arun(self, location: str, unit: str):
        raise NotImplementedError("This tool does not support async")
