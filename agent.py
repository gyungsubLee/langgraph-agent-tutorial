"""
LangGraph Agent Implementation
This script demonstrates creating an agent with tools using LangGraph and Anthropic's Claude.
"""

import getpass
import os
from pathlib import Path
from typing import Annotated

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import BaseMessage
from typing_extensions import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


# ============================================================================
# Environment Setup
# ============================================================================

def _set_env(var: str):
    """Set environment variable if not already set."""
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


def setup_environment():
    """
    Setup required API keys.
    Loads from .env file first, then prompts for missing keys.
    """
    # Load environment variables from .env file
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
        print(f"✅ Loaded environment variables from {env_path}")
    else:
        print(f"⚠️  .env file not found at {env_path}")
        print("💡 Create one by copying: cp .env.sample .env")

    # Check for required API keys, prompt if missing
    _set_env("ANTHROPIC_API_KEY")
    _set_env("TAVILY_API_KEY")


# ============================================================================
# Visualization Helper
# ============================================================================

def visualize_graph(graph):
    """Visualize the graph structure (requires additional dependencies)."""
    from IPython.display import Image, display
    try:
        display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
    except Exception as e:
        print(f"Graph visualization not available: {e}")


# ============================================================================
# State Definition
# ============================================================================

class State(TypedDict):
    """
    Graph state definition.

    The `add_messages` function in the annotation defines how this state key
    should be updated (appends messages to the list rather than overwriting).
    """
    messages: Annotated[list, add_messages]


# ============================================================================
# Basic Chatbot (Part 1)
# ============================================================================

def create_basic_chatbot():
    """
    Create a basic chatbot without tools.

    Returns:
        Compiled graph for basic chatbot
    """
    # Initialize state graph
    graph_builder = StateGraph(State)

    # Initialize LLM
    llm = ChatAnthropic(model="claude-3-haiku-20240307")

    # Define chatbot node
    def chatbot(state: State):
        return {"messages": [llm.invoke(state["messages"])]}

    # Build graph
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.set_entry_point("chatbot")
    graph_builder.set_finish_point("chatbot")

    return graph_builder.compile()


# ============================================================================
# Agent with Tools (Part 2)
# ============================================================================

def create_agent_with_tools():
    """
    Create an agent with tool-calling capabilities.

    Returns:
        Compiled graph for agent with tools
    """
    # Initialize state graph
    graph_builder = StateGraph(State)

    # Initialize tools
    tool = TavilySearchResults(max_results=2)
    tools = [tool]

    # Initialize LLM with tools
    llm = ChatAnthropic(model="claude-3-haiku-20240307")
    llm_with_tools = llm.bind_tools(tools)

    # Define chatbot node
    def chatbot(state: State):
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

    # Add nodes
    graph_builder.add_node("chatbot", chatbot)

    # Add tool node
    tool_node = ToolNode(tools=[tool])
    graph_builder.add_node("tools", tool_node)

    # Add conditional edges
    graph_builder.add_conditional_edges(
        "chatbot",
        tools_condition,
    )

    # Return to chatbot after tool execution
    graph_builder.add_edge("tools", "chatbot")
    graph_builder.set_entry_point("chatbot")

    return graph_builder.compile()


# ============================================================================
# Agent with Memory (Part 3)
# ============================================================================

def create_agent_with_memory(memory_path=":memory:"):
    """
    Create an agent with persistent memory using checkpointing.

    Args:
        memory_path: Path to SQLite database (default: in-memory)

    Returns:
        Compiled graph with memory
    """
    # Initialize state graph
    graph_builder = StateGraph(State)

    # Initialize tools
    tool = TavilySearchResults(max_results=2)
    tools = [tool]

    # Initialize LLM with tools
    llm = ChatAnthropic(model="claude-3-haiku-20240307")
    llm_with_tools = llm.bind_tools(tools)

    # Define chatbot node
    def chatbot(state: State):
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

    # Add nodes
    graph_builder.add_node("chatbot", chatbot)

    # Add tool node
    tool_node = ToolNode(tools=[tool])
    graph_builder.add_node("tools", tool_node)

    # Add conditional edges
    graph_builder.add_conditional_edges(
        "chatbot",
        tools_condition,
    )

    # Return to chatbot after tool execution
    graph_builder.add_edge("tools", "chatbot")
    graph_builder.set_entry_point("chatbot")

    # Initialize memory/checkpointer
    memory = SqliteSaver.from_conn_string(memory_path)

    # Compile with checkpointer
    return graph_builder.compile(checkpointer=memory)


# ============================================================================
# Interactive Chat Functions
# ============================================================================

def run_basic_chat(graph):
    """
    Run interactive chat with basic chatbot.

    Args:
        graph: Compiled graph
    """
    print("Basic Chatbot - Type 'quit', 'exit', or 'q' to end")
    print("-" * 50)

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("대화 종료.")
            break

        for event in graph.stream({"messages": ("user", user_input)}):
            for value in event.values():
                print("Assistant:", value["messages"][-1].content)


def run_agent_chat(graph, config=None):
    """
    Run interactive chat with agent (tools enabled).

    Args:
        graph: Compiled graph
        config: Optional configuration dict with thread_id for memory
    """
    print("Agent Chat - Type 'quit', 'exit', or 'q' to end")
    print("-" * 50)

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("대화 종료!")
            break

        # Stream events
        stream_kwargs = {"messages": [("user", user_input)]}
        if config:
            events = graph.stream(stream_kwargs, config, stream_mode="values")
        else:
            events = graph.stream(stream_kwargs)

        for event in events:
            message = event["messages"][-1]
            if isinstance(message, BaseMessage):
                print("Assistant:", message.content)


# ============================================================================
# Example Usage
# ============================================================================

def main():
    """Main function demonstrating different agent configurations."""
    # Setup environment (loads .env file)
    setup_environment()

    print("\n" + "=" * 50)
    print("LangGraph Agent Examples")
    print("=" * 50)

    # Example 1: Basic Chatbot
    print("\n[Example 1] Basic Chatbot (no tools)")
    print("-" * 50)
    basic_graph = create_basic_chatbot()
    # Uncomment to run: run_basic_chat(basic_graph)

    # Example 2: Agent with Tools
    print("\n[Example 2] Agent with Tools")
    print("-" * 50)
    agent_graph = create_agent_with_tools()
    # Uncomment to run: run_agent_chat(agent_graph)

    # Example 3: Agent with Memory
    print("\n[Example 3] Agent with Memory")
    print("-" * 50)
    memory_graph = create_agent_with_memory()

    # Configuration for memory-enabled agent
    config = {"configurable": {"thread_id": "1"}}

    # Example interaction with memory
    print("\nFirst message:")
    events = memory_graph.stream(
        {"messages": [("user", "안녕 나는 Liam이야.")]},
        config,
        stream_mode="values"
    )
    for event in events:
        event["messages"][-1].pretty_print()

    print("\nSecond message (testing memory):")
    events = memory_graph.stream(
        {"messages": [("user", "내 이름 기억해?")]},
        config,
        stream_mode="values"
    )
    for event in events:
        event["messages"][-1].pretty_print()

    # Check state
    print("\nCurrent state snapshot:")
    snapshot = memory_graph.get_state(config)
    print(f"Number of messages: {len(snapshot.values['messages'])}")
    print(f"Next nodes: {snapshot.next}")

    # Uncomment to run interactive chat with memory:
    # run_agent_chat(memory_graph, config)


if __name__ == "__main__":
    main()
