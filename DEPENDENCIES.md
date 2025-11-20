# Dependencies Installation Guide

All required dependencies for the LangGraph Agent tutorials in the `ch/` directory have been installed in a virtual environment.

## Virtual Environment Setup ✅

A Python virtual environment has been created at `./venv/` with all required packages installed.

## Installed Packages

### Core Frameworks
- **langgraph** (1.0.3) - Graph-based agent framework
- **langchain** (1.0.8) - LangChain core framework
- **langchain-core** (1.0.7) - Core abstractions
- **langchain-community** (0.4.1) - Community integrations
- **langchain-classic** (1.0.0) - Classic components
- **langchain_experimental** (0.4.0) - Experimental features

### LLM Integrations
- **langchain_anthropic** (1.1.0) - Claude/Anthropic integration
- **langchain_openai** (1.0.3) - OpenAI integration
- **langchain-fireworks** (1.0.0) - Fireworks AI integration
- **anthropic** (0.74.1) - Anthropic Python SDK
- **openai** (2.8.1) - OpenAI Python SDK
- **fireworks-ai** (0.19.20) - Fireworks AI SDK

### Tools & Search
- **tavily-python** (0.7.13) - Tavily search API
- **duckduckgo-search** (8.1.1) - DuckDuckGo search
- **wikipedia** (1.4.0) - Wikipedia API

### Utilities
- **langchainhub** (0.1.21) - LangChain Hub integration
- **langsmith** (0.4.44) - LangSmith tracing
- **langgraph-checkpoint** (3.0.1) - Checkpointing support
- **langgraph-prebuilt** (1.0.4) - Prebuilt components
- **langgraph-sdk** (0.2.9) - LangGraph SDK

### Data Science & ML
- **pandas** (2.3.3) - Data manipulation
- **scikit-learn** (1.7.2) - Machine learning
- **scipy** (1.16.3) - Scientific computing
- **matplotlib** (3.10.7) - Plotting library

### Web Automation
- **playwright** (1.56.0) - Browser automation
- **beautifulsoup4** (4.14.2) - HTML parsing
- **lxml** (6.0.2) - XML/HTML processing

### Supporting Libraries
- **tiktoken** (0.12.0) - Token counting
- **httpx** (0.28.1) - HTTP client
- **aiohttp** (3.13.2) - Async HTTP
- **pydantic** (2.12.4) - Data validation
- **pyyaml** (6.0.3) - YAML support

## Playwright Browsers

The following browsers have been installed for Playwright:
- **Chromium** 141.0.7390.37 (build v1194)
- **Firefox** 142.0.1 (build v1495)
- **WebKit** 26.0 (build v2215)
- **FFMPEG** (build v1011)

## Quick Start

### Activate Virtual Environment

```bash
# Method 1: Using the activation script
source activate_venv.sh

# Method 2: Manual activation
source venv/bin/activate
```

### Deactivate

```bash
deactivate
```

## Required API Keys

To use the notebooks, you'll need to set up the following API keys:

### Environment Variables
```bash
export ANTHROPIC_API_KEY="your-key-here"
export OPENAI_API_KEY="your-key-here"
export TAVILY_API_KEY="your-key-here"
export FIREWORKS_API_KEY="your-key-here"  # Optional
```

### Getting API Keys
- **Anthropic (Claude)**: https://console.anthropic.com/
- **OpenAI**: https://platform.openai.com/api-keys
- **Tavily**: https://tavily.com/
- **Fireworks AI**: https://fireworks.ai/ (optional)

## Installation Commands

### Fresh Virtual Environment Setup

If you need to set up on another machine or recreate the environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install all dependencies
pip install langgraph langchain langchain-core langchain-community \
  langchain_anthropic langchain_openai langchain-fireworks langchainhub \
  tavily-python pandas langchain_experimental matplotlib playwright \
  duckduckgo-search wikipedia scikit-learn

# Install Playwright browsers
playwright install
```

### Requirements File (Alternative)

You can also create a `requirements.txt` file:

```bash
# Generate requirements file from current environment
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

## Verification

To verify the installation, activate the virtual environment and run:

```bash
# Activate environment
source venv/bin/activate

# Check Python version
python --version

# Verify key packages
python -c "import langgraph; import langchain; import langchain_anthropic; import langchain_openai; from playwright.sync_api import sync_playwright; print('✅ All packages imported successfully!')"
```

## Notebook Overview

The `ch/` directory contains the following tutorials:

1. **P09_CH08_01_agent.ipynb** - Basic agent creation with tools
2. **P09_CH08_02_AgentExecutor.ipynb** - LangChain AgentExecutor
3. **P09_CH08_03_plan-and-execute.ipynb** - Plan-and-execute pattern
4. **P09_CH08_04_reflection.ipynb** - Reflection pattern
5. **P09_CH08_05_Multi-Agent.ipynb** - Multi-agent systems
6. **P09_CH08_06_web_research.ipynb** - Web research agent
7. **P09_CH08_07_agent_simulation_evaluation.ipynb** - Agent evaluation
8. **P09_CH08_08_web_voyager.ipynb** - Web navigation agent
9. **P09_CH08_09_chain_of_table.ipynb** - Chain-of-table reasoning

## Troubleshooting

### Common Issues

**Virtual Environment Not Active**: Make sure to activate before running code
```bash
source venv/bin/activate
# You should see (venv) in your terminal prompt
```

**Import Errors**: Ensure all packages are installed in the virtual environment
```bash
# Activate first
source venv/bin/activate

# Check installed packages
pip list | grep langchain
pip list | grep langgraph
```

**Playwright Browser Issues**: Reinstall browsers in the virtual environment
```bash
source venv/bin/activate
playwright install --force
```

**API Key Errors**: Verify environment variables are set
```bash
echo $ANTHROPIC_API_KEY
echo $OPENAI_API_KEY
echo $TAVILY_API_KEY
```

**Wrong Python Version**: Ensure you're using the virtual environment Python
```bash
which python  # Should show: .../venv/bin/python
python --version  # Should be 3.8+
```

## System Requirements

- Python 3.8 or higher (3.12.6 recommended)
- macOS 11.0 or higher (for Playwright browsers)
- 2GB free disk space (for browsers)
- Internet connection (for API calls)

## Additional Notes

- All installations completed successfully on macOS ARM64 (Apple Silicon)
- Total installation size: ~400MB (excluding browsers)
- Playwright browsers: ~380MB additional space
