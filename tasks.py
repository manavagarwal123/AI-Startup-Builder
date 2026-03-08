#when token is limited

from crewai import Task
from agents import ceo, market_analyst, product_manager, cto, engineer, pitch_writer


idea_task = Task(
    description="""
Generate a detailed startup idea in the industry: {industry}

Include:
- Startup name
- Problem statement
- Solution
- Target users
- Unique value proposition

Limit response to 220 words.
""",
    expected_output="Startup idea with name, problem, solution, and target users",
    agent=ceo
)


market_task = Task(
    description="""
Analyze the market for this startup idea.

Include:
- Market size (TAM / SAM / SOM if possible)
- 3 major competitors
- Key market trends
- Growth opportunities

Limit response to 280 words.
""",
    expected_output="Market analysis including competitors and opportunities",
    agent=market_analyst
)


product_task = Task(
    description="""
Define the product plan for this startup.

Include:
- Core product features
- MVP feature set
- Future roadmap features
- Basic user flow

Limit response to 220 words.
""",
    expected_output="Product plan and roadmap",
    agent=product_manager
)


tech_task = Task(
    description="""
Suggest a scalable system architecture.

Include:
- Frontend framework
- Backend architecture
- AI model usage
- Database
- Deployment infrastructure

Limit response to 220 words.
""",
    expected_output="Technology stack and architecture design",
    agent=cto
)


landing_task = Task(
    description="""
Generate a clean HTML landing page.

Sections required:
- Hero section
- Features section
- Pricing section
- Contact section

Use semantic HTML.

Limit to 120 lines of HTML code.
""",
    expected_output="HTML landing page structure",
    agent=engineer
)


pitch_task = Task(
    description="""
Write a compelling investor pitch.

Include:
- Problem
- Solution
- Market opportunity
- Revenue model
- Why this startup will succeed

Limit response to 200 words.
""",
    expected_output="Investor pitch summary",
    agent=pitch_writer
)