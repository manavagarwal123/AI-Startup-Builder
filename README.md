# AI Startup Builder 🚀

A multi-agent Streamlit app powered by CrewAI and Meta LLaMA 3. Enter an industry and watch six specialized agents collaborate to produce a complete startup plan, including idea generation, market research, product roadmap, tech architecture, landing page HTML and an investor pitch.

![Architecture](assets/architecture.png)

---

## 🧩 Project Overview

The system orchestrates the following agents:

| Agent | Responsibility |
|-------|----------------|
| Startup CEO | Ideation & business concept |
| Market Research Analyst | Market sizing & competitor analysis |
| Product Manager | Feature definition & roadmap |
| CTO | Technical architecture & stack |
| Software Engineer | Landing page HTML generation |
| Pitch Writer | Investor pitch narrative |

Agents run sequentially within a CrewAI crew, sharing context automatically.

## 🏛 Architecture

As shown above, the Streamlit UI (`app.py`) accepts user input and triggers a CrewAI pipeline defined in `crew.py`. Agent roles and LLM settings live in `agents.py` and tasks in `tasks.py`.

The output is displayed in interactive tabs; the landing page HTML is rendered, and the entire report is downloadable as Markdown.

## 🔄 Agent Workflow

1. User submits an industry.
2. `startup_crew.kickoff(inputs={"industry": industry})` fires.
3. Each task executes in order, updating session state and UI.
4. Results are shown in six tabs; download and preview options are available.

## 🚀 Installation

```bash
git clone <repo-url>
cd ai-startup-builder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # add your keys
```

## ▶️ Running the App

```bash
streamlit run app.py
```

Once the browser opens, type a target industry and click **Launch Crew**.

## 📂 Example Output

The report includes clearly separated sections for each agent. The landing page HTML tab shows formatted markup, and you can click a download button to save the full startup plan.

---

Feel free to extend or deploy the app using Streamlit Cloud, Docker, or your preferred platform.