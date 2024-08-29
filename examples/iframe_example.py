from lavague.contexts.gemini import GeminiContext
from lavague.drivers.selenium import SeleniumDriver

from lavague.core import ActionEngine, WorldModel
from lavague.core.agents import WebAgent

context = GeminiContext()
selenium_driver = SeleniumDriver(headless=False)
world_model = WorldModel()
action_engine = ActionEngine.from_context(context, selenium_driver)
agent = WebAgent(world_model, action_engine)
agent.get("https://selectorshub.com/iframe-scenario/")
agent.run("Fill the 3 inputs bar with Hop")
