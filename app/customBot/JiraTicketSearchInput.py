from pydantic import BaseModel, Field


class JiraTicketSearchInput(BaseModel):

    jql: str = Field(
        ...,
        description="The JQL string to define the search criteria. Example: 'project = MYPROJECT AND status = \"In Progress\"'"
    )