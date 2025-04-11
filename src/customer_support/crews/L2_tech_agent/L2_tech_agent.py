from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel

class Resolution(BaseModel):
    resolution: str

@CrewBase
class L2TechAgentCrew:
    """L2 Tech Agent Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def L2_tech_agent(self) -> Agent:
        llm = LLM(
            model="gemini/gemini-1.5-flash",
            temperature=0.7,
        )
        return Agent(
            config=self.agents_config["L2_tech_agent"],
            verbose=True,
            llm=llm
        )

    @task
    def issue_resolution_task(self) -> Task:
        return Task(
            config=self.tasks_config["issue_resolution_task"],
            output_pydantic=Resolution,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the L2 Tech Agent Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
