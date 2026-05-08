# Multi Agent MVP

## 启动后端

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

接口地址：

http://127.0.0.1:8000/docs



## 一、系统目标

这是一个可扩展的多 Agent 协同运营自动化系统，支持：

* 多 Agent 自动协作
* 任务拆分
* 任务调度
* 消息总线
* 工作流编排
* 自动执行任务
* API 调用
* Webhook
* 数据库存储
* 日志系统
* 插件扩展
* LLM 接入（OpenAI / DeepSeek / Claude）
* 自动化运营
* 自动内容生成
* 自动客服
* 自动数据分析
* 自动营销

适合：

* AI 公司
* 自动化工作室
* 短视频运营
* 社媒运营
* 自动客服
* 自动营销
* AI SaaS
* 企业自动化

---

# 二、系统架构

```text
                ┌──────────────────┐
                │   Web Dashboard  │
                └────────┬─────────┘
                         │
                ┌────────▼─────────┐
                │   API Gateway    │
                └────────┬─────────┘
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
┌──────▼──────┐ ┌────────▼────────┐ ┌──────▼──────┐
│ Task Engine │ │ Message Broker  │ │ Agent Router│
└──────┬──────┘ └────────┬────────┘ └──────┬──────┘
       │                 │                 │
       │                 │                 │
 ┌─────▼────┐     ┌──────▼──────┐    ┌────▼─────┐
 │ Content  │     │ Marketing   │    │客服Agent │
 │ Agent    │     │ Agent       │    │           │
 └──────────┘     └─────────────┘    └──────────┘

```

---

# 三、技术栈

## 后端

* Python 3.11
* FastAPI
* Redis
* PostgreSQL
* Celery
* RabbitMQ
* SQLAlchemy
* LangChain
* OpenAI SDK

## 前端

* React
* Next.js
* TailwindCSS
* Zustand

## AI

* GPT-4o
* DeepSeek
* Claude
* Gemini

---

# 四、项目结构

```text
multi-agent-system/
│
├── app/
│   ├── agents/
│   ├── core/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── workflows/
│   ├── database/
│   ├── scheduler/
│   └── main.py
│
├── frontend/
├── docker-compose.yml
├── requirements.txt
└── .env
```
