from crewai import Crew
from agents import ceo, market_analyst, product_manager, cto, engineer, pitch_writer
from tasks import idea_task, market_task, product_task, tech_task, landing_task, pitch_task


startup_crew = Crew(
    agents=[
        ceo,
        market_analyst,
        product_manager,
        cto,
        engineer,
        pitch_writer
    ],

    tasks=[
        idea_task,
        market_task,
        product_task,
        tech_task,
        landing_task,
        pitch_task
    ],

    verbose=True,
    memory=False
)