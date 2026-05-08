from app.core.base_agent import BaseAgent
from app.core.llm import ask_gpt

class CustomerAgent(BaseAgent):

    async def execute(self, task):

        prompt = f'''
你是专业客服

用户消息:
{task}

请输出回复
'''

        result = ask_gpt(prompt)

        return {
            "agent": self.name,
            "result": result
        }