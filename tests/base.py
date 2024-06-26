import unittest
import types

prompt = "This is a test prompt"


class llmBase(unittest.TestCase):
    def setUp(self):
        """Override this"""
        self.bot = None
        self.prompt = prompt

    def test_ask_non_stream(self):
        """Ask non-stream"""
        resp = self.bot.ask(self.prompt)
        self.assertIsInstance(resp, dict)

    def test_ask_stream(self):
        """Ask stream"""
        resp = self.bot.ask(self.prompt, stream=True)
        self.assertIsInstance(resp, types.GeneratorType)
        for value in resp:
            self.assertIsInstance(value, dict)

    def test_ask_stream_raw(self):
        """Ask stream raw"""
        resp = self.bot.ask(self.prompt, True, True)
        self.assertIsInstance(resp, types.GeneratorType)

        for count, value in enumerate(resp):
            self.assertIsInstance(value, str)

    def test_get_message(self):
        """Response retrieval"""
        resp = self.bot.ask(self.prompt)
        self.assertIsInstance(self.bot.get_message(resp), str)

    def test_chat_non_stream(self):
        """Chat non-stream"""
        resp = self.bot.chat(self.prompt)
        self.assertIs(type(resp), str, f"{resp} is not str")

    def test_chat_stream(self):
        """Chat stream"""
        resp = self.bot.chat(self.prompt, stream=True)
        self.assertIsInstance(resp, types.GeneratorType)
        for value in resp:
            self.assertIsInstance(value, str)

    def test_optimizer_usage(self):
        """Code optimization"""
        resp = self.bot.chat(self.prompt, optimizer="code")
        self.assertIsInstance(resp, str)

    def test_last_response(self):
        """Last response availability"""
        self.bot.chat(self.prompt)
        self.assertIsInstance(self.bot.last_response, dict)


class AsyncProviderBase(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        """Override this"""
        self.bot = None
        self.prompt = prompt

    async def test_ask_non_stream(self):
        """Aync ask non-stream"""
        resp = await self.bot.ask(self.prompt)
        self.assertIsInstance(resp, dict)

    async def test_ask_stream(self):
        """Async ask stream"""
        resp = await self.bot.ask(self.prompt, stream=True)
        self.assertIsInstance(resp, types.AsyncGeneratorType)
        async for value in resp:
            self.assertIsInstance(value, dict)

    async def test_ask_stream_raw(self):
        """Async ask stream raw"""
        resp = await self.bot.ask(self.prompt, True, True)
        self.assertIsInstance(resp, types.AsyncGeneratorType)

        async for value in resp:
            self.assertIsInstance(value, str)

    async def test_get_message(self):
        """Async response retrieval"""
        resp = await self.bot.ask(self.prompt)
        self.assertIsInstance(await self.bot.get_message(resp), str)

    async def test_chat_non_stream(self):
        """Aysnc chat non-stream"""
        resp = await self.bot.chat(self.prompt)
        self.assertIs(type(resp), str, f"{resp} is not str")

    async def test_chat_stream(self):
        """Async chat stream"""
        resp = await self.bot.chat(self.prompt, stream=True)
        self.assertIsInstance(resp, types.AsyncGeneratorType)
        async for value in resp:
            self.assertIsInstance(value, str)

    async def test_optimizer_usage(self):
        """Async code optimization"""
        resp = await self.bot.chat(self.prompt, optimizer="code")
        self.assertIsInstance(resp, str)

    async def test_last_response(self):
        """Async last response availability"""
        await self.bot.chat(self.prompt)
        self.assertIsInstance(self.bot.last_response, dict)


if __name__ == "__main__":
    unittest.main()
