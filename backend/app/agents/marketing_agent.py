from app.core.base_agent import BaseAgent
from app.core.llm import ask_gpt

class MarketingAgent(BaseAgent):

    async def execute(self, task):

        prompt = f'''
你是营销增长专家

任务:
{task}

请输出详细营销方案
'''

        result = ask_gpt(prompt)

        return {
            "agent": self.name,
            "result": result
        }