from app.core.base_agent import BaseAgent
from app.core.llm import ask_gpt

class ContentAgent(BaseAgent):

    async def execute(self, task):

        prompt = f'''
你是专业内容运营专家

任务:
{task}

请输出:
1. 标题
2. 视频脚本
3. 标签
'''

        result = ask_gpt(prompt)

        return {
            "agent": self.name,
            "result": result
        }