# Example: Customer Support Flow with structured processing
from crewai.flow.flow import Flow, listen, router, start, or_
from crewai import LLM

from textwrap import dedent
from pydantic import BaseModel
from typing import List, Dict
import time

# Define structured state
class SupportTicketState(BaseModel):
    ticket_id: str = ""
    customer_name: str = ""
    issue_description: str = ""
    category: str = ""
    priority: str = "medium"
    resolution: str = ""
    resolution_details: str = ""
    satisfaction_score: int = 0


def gather_inputs():
    print("## Welcome to Customer Support")
    print('-------------------------------')
    customer = input(
        dedent("""
        Please type your name?
        """))
    issue = input(
        dedent("""
        Please type the issue description:
        """))
    return {
        'customer': customer,
        'issue': issue
    }

class CustomerSupportFlow(Flow[SupportTicketState]):
    @start()
    def receive_ticket(self):
        # In a real app, this might come from an API
        self.state.ticket_id = "TKT-12345"
        inputs = gather_inputs()
        self.state.customer_name = inputs["customer"] # "Alex Johnson"
        self.state.issue_description = inputs["issue"] # "Unable to access premium features after payment"
        return "Ticket received"

    @listen(receive_ticket)
    def categorize_ticket(self, _):
        # Use a direct LLM call for categorization
        llm = LLM(model="gemini/gemini-1.5-flash")

        prompt = f"""
        Categorize the following customer support issue into one of these categories:
        - Billing
        - Account Access
        - Technical Issue
        - Feature Request
        - Other

        Issue: {self.state.issue_description}

        Return only the category name.
        """

        self.state.category = llm.call(prompt).strip()
        return self.state.category

    @router(categorize_ticket)
    def route_by_category(self, category):
        # Route to different handlers based on category
        return category.lower().replace(" ", "_")

    @listen("billing")
    def handle_billing_issue(self):
        # Handle billing-specific logic
        self.state.priority = "high"
        # More billing-specific processing using BillingCrew
        time.sleep(3)  # Add 3 second delay
        return "Billing issue handled"

    @listen("account_access")
    def handle_access_issue(self):
        # Handle access-specific logic
        self.state.priority = "high"
        # More access-specific processing using AccountMgmtCrew
        time.sleep(3)  # Add 3 second delay

        return "Access issue handled"

    @listen("technical_issue")
    def handle_technical_issue(self):
        # Handle access-specific logic
        self.state.priority = "medium"
        # More access-specific processing using ITCrew

       # Use a direct LLM call for categorization
        llm = LLM(model="gemini/gemini-1.5-flash")

        prompt = f"""
        Here is a Technical issue customer is facing

        Issue: {self.state.issue_description}

        Return only the issue resolution in a single line.
        """

        self.state.resolution_details = llm.call(prompt).strip()
    
        return "Technical Issue handled"

    # Additional category handlers...

    @listen(or_("billing", "account_access", "technical_issue", "feature_request", "other"))
    def resolve_ticket(self, resolution_info):
        # Final resolution step
        self.state.resolution = f"Issue resolved: {resolution_info}"
        return self.state.resolution


def kickoff():
    support_flow = CustomerSupportFlow()
    result = support_flow.kickoff()
    print(f"\n\nHello {support_flow.state.customer_name}, here is status of your issue: {support_flow.state.issue_description}")
    print(f"Status: {support_flow.state.resolution}")
    print(f"Resolution Details: {support_flow.state.resolution_details}")


def plot():
    support_flow = CustomerSupportFlow()
    support_flow.plot()
