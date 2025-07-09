# types.py
from pydantic import BaseModel
from typing import Optional, List

# Financial Goal model
class Goal(BaseModel):
    name: str  # e.g., "Buy a house", "Save for retirement"
    target_amount: Optional[float] = None
    timeline_years: Optional[int] = None
    priority: Optional[str] = "medium"  # low, medium, high

# Risk profile categories
class RiskProfile(BaseModel):
    category: str  # e.g., "Conservative", "Moderate", "Aggressive"
    description: Optional[str] = None

# Investment strategy recommendation
class Strategy(BaseModel):
    name: str  # e.g., "Index Funds", "ETFs", "Retirement Plan"
    description: str
    suitable_for: List[str]  # e.g., ["Moderate", "Conservative"]

# Learning resource recommendation
class LearningResource(BaseModel):
    title: str
    type: str  # e.g., "Article", "Video", "Book"
    url: Optional[str] = None
    description: Optional[str] = None

# Aggregated result format (optional for coordinator)
class InvestmentPlan(BaseModel):
    goals: List[Goal]
    risk_profile: RiskProfile
    recommended_strategies: List[Strategy]
    learning_resources: List[LearningResource]

class LearningRequest(BaseModel):
    topic: str
    user_question: Optional[str] = None

class LearningResponse(BaseModel):
    topic: str
    explanation: str
    tips: Optional[List[str]] = None

class StrategyRecommendation(BaseModel):
    strategy_name: str
    overview: str
    recommended_assets: List[str]
    rationale: str