# inv_agents/coordinator.py
from agents import Agent
from inv_agents.goal_planner import goal_planner
from inv_agents.risk_profiler import risk_profiler
from inv_agents.strategy_advisor import strategy_advisor
from inv_agents.learning_agent import learning_agent

# Convert specialists into tools
goal_planner_tool = goal_planner.as_tool(
    tool_name="plan_goal",
    tool_description="Helps the user define and structure an investment goal."
)

risk_profiler_tool = risk_profiler.as_tool(
    tool_name="profile_risk",
    tool_description="Assesses the user's risk tolerance based on their answers."
)

strategy_advisor_tool = strategy_advisor.as_tool(
    tool_name="advise_strategy",
    tool_description="Suggests an investment strategy tailored to the user's goals and risk profile."
)

learning_tool = learning_agent.as_tool(
    tool_name="teach_investing",
    tool_description="Explains beginner investing concepts in simple language."
)

# Coordinator Agent
investment_mentor = Agent(
    name="Investment Mentor",
    instructions=""" 
You are a friendly investment mentor for beginners.

Your job is to:
- Ask about the user's goals and call `plan_goal` to help them structure their goals
- Understand their risk tolerance via `profile_risk` to assess their comfort level
- Recommend a personalized investment approach using `advise_strategy` based on their profile
- Teach investment concepts via `teach_investing` when they have questions

The user has no prior investment experience. Guide them clearly and patiently. If unsure what they want, ask clarifying questions.

Always start by understanding what they want to achieve with their investments.
""",
    tools=[
        goal_planner_tool,
        risk_profiler_tool,
        strategy_advisor_tool,
        learning_tool,
    ],
)