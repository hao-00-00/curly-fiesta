from app.agents.content_agent import ContentAgent
from app.agents.marketing_agent import MarketingAgent
from app.agents.customer_agent import CustomerAgent

class AgentRouter:

    def __init__(self):

        self.agents = {
            "content": ContentAgent("Content Agent"),
            "marketing": MarketingAgent("Marketing Agent"),
            "customer": CustomerAgent("Customer Agent")
        }

    async def dispatch(self, agent_type, task):

        agent = self.agents.get(agent_type)

        if not agent:
            return {"error": "agent not found"}

        return await agent.execute(task)