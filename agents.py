from dotenv import load_dotenv

from crewai import Agent

load_dotenv()

MODEL = "huggingface/meta-llama/Meta-Llama-3-8B-Instruct"

ceo = Agent(
    role="Startup CEO",
    goal="Generate innovative startup ideas",
    backstory="Serial entrepreneur who builds successful startups.",
    llm=MODEL,
    verbose=True
)

market_analyst = Agent(
    role="Market Research Analyst",
    goal="Analyze market opportunities and competitors",
    backstory="Expert in startup market research.",
    llm=MODEL,
    verbose=True
)

product_manager = Agent(
    role="Product Manager",
    goal="Define product features and MVP",
    backstory="Specialist in digital product development.",
    llm=MODEL,
    verbose=True
)

cto = Agent(
    role="Chief Technology Officer",
    goal="Design system architecture and tech stack",
    backstory="Expert AI architect.",
    llm=MODEL,
    verbose=True
)

engineer = Agent(
    role="Software Engineer",
    goal="Generate landing page HTML",
    backstory="Frontend engineer skilled in web development.",
    llm=MODEL,
    verbose=True
)

pitch_writer = Agent(
    role="Investor Pitch Writer",
    goal="Create a compelling startup pitch",
    backstory="Expert in startup fundraising.",
    llm=MODEL,
    verbose=True
)