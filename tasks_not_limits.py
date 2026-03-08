from crewai import Task
from agents import ceo, market_analyst, product_manager, cto, engineer, pitch_writer


idea_task = Task(
    description="Generate a startup idea in the industry: {industry}. Include problem, solution, and target users.",
    expected_output="Detailed startup idea including problem, solution and target audience.",
    agent=ceo
)

market_task = Task(
    description="Analyze the market and competitors for this startup.",
    expected_output="Market analysis including competitors and opportunities.",
    agent=market_analyst
)

product_task = Task(
    description="Define product features and MVP roadmap.",
    expected_output="List of product features and MVP plan.",
    agent=product_manager
)

tech_task = Task(
    description="Suggest system architecture and technology stack.",
    expected_output="Technical architecture and recommended technologies.",
    agent=cto
)

landing_task = Task(
    description="Generate HTML structure for a startup landing page.",
    expected_output="Simple HTML landing page layout.",
    agent=engineer
)

pitch_task = Task(
    description="Write an investor pitch for the startup.",
    expected_output="Compelling startup pitch.",
    agent=pitch_writer
)

