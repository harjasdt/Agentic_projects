from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .tools.email import EmailTool
from pydantic import BaseModel, Field

class ExercisePydantic(BaseModel):
    user_email: str = Field(description="Email id of the user")
    workout_plan:str = Field(description="Personalised workout plan based on users lifestyle and fitness goal")

class DietPydantic(BaseModel):
    user_email: str = Field(description="Email id of the user")
    diet_plan:str = Field(description="Personalised diet plan based on users lifestyle and fitness goal")

class SummaryPydantic(BaseModel):
    user_email: str = Field(description="Email id of the user")
    email_bosy:str = Field(description="summary of workout_plan and diet_plan in HTML . this will be the email body so be professional")
    email_subject:str = Field(description="motivational subject for the email")


@CrewBase
class GymTrainer():
    """GymTrainer crew"""

    agents: List[BaseAgent] #'config/agents.yaml'
    tasks: List[Task]

    @agent
    def exercise_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['exercise_planner'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def diet_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['diet_planner'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def summariser(self) -> Agent:
        return Agent(
            config=self.agents_config['summariser'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def notifier(self) -> Agent:
        return Agent(
            config=self.agents_config['notifier'], # type: ignore[index]
            verbose=True,
            tools=[EmailTool()],
            memory=True
        )


    @task
    def exercise_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['exercise_plan_task'], # type: ignore[index]
            output_pydantic=ExercisePydantic
        )

    @task
    def diet_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['diet_plan_task'], # type: ignore[index]
            output_pydantic=DietPydantic
        )
    
    @task
    def summarisation_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarisation_task'], # type: ignore[index]
            output_pydantic=SummaryPydantic
        )
    
    @task
    def notification_task(self) -> Task:
        return Task(
            config=self.tasks_config['notification_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the GymTrainer crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
