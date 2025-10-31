#imports
from  fastmcp import FastMCP

#local imports
import proxmox



#MCP
mcp = FastMCP("Proxmox")

@mcp.tool
def lxcinfo():
    proxmox.lxcinfo()
    
