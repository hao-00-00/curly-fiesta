class WorkflowEngine:

    def __init__(self, router):
        self.router = router

    async def run(self, workflow):

        results = []

        for step in workflow:

            result = await self.router.dispatch(
                step["agent"],
                step["task"]
            )

            results.append(result)

        return results