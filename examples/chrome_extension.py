from lavague.core import WorldModel, ActionEngine
from lavague.core.agents import WebAgent
from lavague.drivers.driverserver import DriverServer
from lavague.server import AgentServer, AgentSession

def create_agent(session: AgentSession):
    world_model = WorldModel()
    driver = DriverServer(session)
    action_engine = ActionEngine(driver)
    return WebAgent(world_model, action_engine)

server = AgentServer(create_agent)
server.serve()