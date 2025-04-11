from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel

class Categorization(BaseModel):
    category: str

@CrewBase
class L1AgentCrew:
    """L1 Agent Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def L1_agent(self) -> Agent:
        llm = LLM(
            model="gemini/gemini-1.5-flash",
            temperature=0.7,
        )
        return Agent(
            config=self.agents_config["L1_agent"],
            verbose=True,
            llm=llm
        )

    @task
    def categorize_issue_task(self) -> Task:
        return Task(
            config=self.tasks_config["categorize_issue_task"],
            output_pydantic=Categorization,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the L1 Agent Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
