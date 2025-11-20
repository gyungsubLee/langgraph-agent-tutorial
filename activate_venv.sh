#!/bin/bash
# Virtual Environment Activation Script for LangGraph Agent Tutorial

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🚀 Activating LangGraph virtual environment...${NC}"

# Check if venv exists
if [ ! -d "venv" ]; then
    echo -e "${RED}❌ Virtual environment not found!${NC}"
    echo -e "${YELLOW}💡 Create it with: python -m venv venv${NC}"
    return 1
fi

# Activate virtual environment
source venv/bin/activate

echo -e "${GREEN}✅ Virtual environment activated!${NC}"
echo ""

# Check Python
echo -e "${BLUE}Python Information:${NC}"
echo "  Path: $(which python)"
echo "  Version: $(python --version)"
echo ""

# Check installed packages
echo -e "${BLUE}📦 Installed packages:${NC}"
if command -v pip &> /dev/null; then
    echo "  - langgraph $(pip show langgraph 2>/dev/null | grep Version | cut -d' ' -f2 || echo 'not installed')"
    echo "  - langchain $(pip show langchain 2>/dev/null | grep Version | cut -d' ' -f2 || echo 'not installed')"
    echo "  - langchain_anthropic $(pip show langchain_anthropic 2>/dev/null | grep Version | cut -d' ' -f2 || echo 'not installed')"
    echo "  - langchain_openai $(pip show langchain_openai 2>/dev/null | grep Version | cut -d' ' -f2 || echo 'not installed')"
    echo "  - python-dotenv $(pip show python-dotenv 2>/dev/null | grep Version | cut -d' ' -f2 || echo 'not installed')"
fi
echo ""

# Check .env file
echo -e "${BLUE}🔑 API Keys Configuration:${NC}"
if [ -f ".env" ]; then
    echo -e "${GREEN}  ✅ .env file found${NC}"

    # Check if API keys are set (without showing values)
    if grep -q "ANTHROPIC_API_KEY=sk-ant" .env 2>/dev/null; then
        echo -e "${GREEN}  ✅ ANTHROPIC_API_KEY configured${NC}"
    else
        echo -e "${YELLOW}  ⚠️  ANTHROPIC_API_KEY not configured${NC}"
    fi

    if grep -q "OPENAI_API_KEY=sk-" .env 2>/dev/null; then
        echo -e "${GREEN}  ✅ OPENAI_API_KEY configured${NC}"
    else
        echo -e "${YELLOW}  ⚠️  OPENAI_API_KEY not configured${NC}"
    fi

    if grep -q "TAVILY_API_KEY=tvly-" .env 2>/dev/null; then
        echo -e "${GREEN}  ✅ TAVILY_API_KEY configured${NC}"
    else
        echo -e "${YELLOW}  ⚠️  TAVILY_API_KEY not configured${NC}"
    fi
else
    echo -e "${RED}  ❌ .env file not found${NC}"
    echo -e "${YELLOW}  💡 Create it with:${NC}"
    echo "     cp .env.sample .env"
    echo "     nano .env"
fi
echo ""

# Quick tips
echo -e "${BLUE}📚 Quick Commands:${NC}"
echo "  python agent.py              - Run agent demo"
echo "  jupyter notebook             - Start Jupyter"
echo "  playwright install           - Install browsers"
echo "  pip install -r requirements.txt  - Reinstall packages"
echo "  deactivate                   - Exit virtual environment"
echo ""

echo -e "${GREEN}🎉 Ready to code!${NC}"
