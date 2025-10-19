from fastmcp import FastMCP

mcp= FastMCP.as_proxy("https://bewildered-turquoise-aphid.fastmcp.app/mcp",name="ExpenseTrackerProxy",version="1.0.0")
                      
if __name__ == "__main__":
    mcp.run()                     