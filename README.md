# LangGraph Agent 실습 자료

LangGraph를 사용한 AI Agent 만들기 실습 자료입니다.

### 1. 가상환경 생성 및 패키지 설치 (최초 1회)

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
source venv/bin/activate

# pip 업그레이드
pip install --upgrade pip

# requirements.txt로 패키지 설치
pip install -r requirements.txt

# (옵션) Playwright 브라우저 설치
playwright install
```

### 2. 가상환경 활성화 (매번 작업 시)

```bash
# 편리한 스크립트 사용
source activate_venv.sh

# 또는 직접 활성화
source venv/bin/activate
```

### 3. API 키 설정 (.env 파일 사용)

```bash
# .env.sample 파일을 .env로 복사
cp .env.sample .env

# .env 파일을 편집기로 열어서 실제 API 키 입력
# vim, nano, vscode 등 원하는 편집기 사용
nano .env
```

**.env 파일 예시:**

```bash
ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxxxx
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxxx
```

> **⚠️ 중요**:
> `.env` 파일은 `.gitignore`에 포함되어 있어 Git에 커밋되지 않습니다.
> API 키를 절대 공개 저장소에 올리지 마세요

### 4. 실습 시작

```bash
# Jupyter Notebook 실행
jupyter notebook

# 또는 Python 파일 실행
python conv/agent.py # conv 폴더 확인
```

## 📁 프로젝트 구조

```
.
├── venv/                      # 가상환경 (git에서 제외됨)
├── requirements.txt           # Python 패키지 의존성
├── .env                       # API 키 설정 (git에서 제외됨)
├── .env.sample               # API 키 템플릿
├── .gitignore                # Git 제외 파일 목록
├── ch/                        # 실습 노트북 디렉토리
│   ├── P09_CH08_01_agent.ipynb
│   ├── P09_CH08_02_AgentExecutor.ipynb
│   ├── P09_CH08_03_plan-and-execute.ipynb
│   ├── P09_CH08_04_reflection.ipynb
│   ├── P09_CH08_05_Multi-Agent.ipynb
│   ├── P09_CH08_06_web_research.ipynb
│   ├── P09_CH08_07_agent_simulation_evaluation.ipynb
│   ├── P09_CH08_08_web_voyager.ipynb
│   └── P09_CH08_09_chain_of_table.ipynb
├── conv/                      # 실습 파이썬 디렉토리
│   ├── 01-agent.py
│   ├── ...
│   └── 09-chain_of_table.py
├── simulation_utils.py        # 시뮬레이션 유틸리티
├── activate_venv.sh          # 가상환경 활성화 스크립트
├── DEPENDENCIES.md           # 의존성 상세 문서
└── README.md                 # README 문서

```

## 📚 실습 내용

### Chapter 01: 기본 Agent

- 기본 챗봇 구현
- Tool을 사용하는 Agent
- 메모리 추가하기

### Chapter 02: AgentExecutor

- LangChain Agent 만들기
- Graph State 정의
- 노드 및 엣지 설정

### Chapter 03: Plan-and-Execute Pattern

- 계획 수립 및 실행 패턴
- 작업 분해 및 순차 실행

### Chapter 04: Reflection Pattern

- 자기 반성 메커니즘
- 출력 개선 루프

### Chapter 05: Multi-Agent

- 여러 Agent 협업
- Agent 간 통신

### Chapter 06: Web Research

- 웹 검색 Agent
- 정보 수집 및 요약

### Chapter 07: Agent Simulation & Evaluation

- Agent 시뮬레이션
- 성능 평가 방법

### Chapter 08: Web Voyager

- 웹 네비게이션 Agent
- Playwright 통합

### Chapter 09: Chain of Table

- 테이블 기반 추론
- 데이터 처리 체인

## 🔧 설치된 주요 패키지

- **langgraph** (1.0.3) - Graph 기반 Agent 프레임워크
- **langchain** (1.0.8) - LangChain 핵심 프레임워크
- **langchain_anthropic** (1.1.0) - Claude/Anthropic 통합
- **langchain_openai** (1.0.3) - OpenAI 통합
- **tavily-python** (0.7.13) - Tavily 검색 API
- **playwright** (1.56.0) - 브라우저 자동화
- **pandas** (2.3.3) - 데이터 분석
- **matplotlib** (3.10.7) - 시각화

전체 목록은 [DEPENDENCIES.md](DEPENDENCIES.md)를 참조하세요.

## 🔑 API 키 발급 및 설정

### 1. API 키 발급

#### Anthropic (Claude)

1. https://console.anthropic.com/ 방문
2. 계정 생성/로그인
3. API Keys 메뉴에서 키 생성
4. `sk-ant-api03-...` 형식의 키 복사

#### OpenAI

1. https://platform.openai.com/ 방문
2. 계정 생성/로그인
3. API keys 섹션에서 키 생성
4. `sk-proj-...` 형식의 키 복사

#### Tavily

1. https://tavily.com/ 방문
2. 계정 생성
3. Dashboard에서 API 키 확인
4. `tvly-...` 형식의 키 복사

### 2. .env 파일 설정

```bash
# 1. 템플릿 파일 복사
cp .env.sample .env

# 2. .env 파일 편집 (아래 방법 중 하나 선택)
nano .env          # nano 편집기
vim .env           # vim 편집기
code .env          # VS Code
open -a TextEdit .env  # macOS 텍스트 편집기

# 3. 발급받은 API 키를 입력하고 저장
```

### 3. .env 파일 자동 로드

Python 스크립트는 자동으로 `.env` 파일을 읽습니다 (`python-dotenv` 사용).

```python
# agent.py에서 자동으로 로드됨
from dotenv import load_dotenv
load_dotenv()  # .env 파일의 환경변수를 자동으로 로드
```

### 4. 수동으로 환경변수 설정 (선택사항)

.env 파일 대신 수동으로 설정하려면:

```bash
# 현재 세션에만 적용
export ANTHROPIC_API_KEY="sk-ant-api03-xxxx"
export OPENAI_API_KEY="sk-proj-xxxx"
export TAVILY_API_KEY="tvly-xxxx"

# 또는 .bashrc / .zshrc에 추가 (영구 적용)
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-xxxx"' >> ~/.zshrc
source ~/.zshrc
```

## 🧪 테스트

```bash
# 가상환경 활성화
source venv/bin/activate

# 패키지 임포트 테스트
python -c "import langgraph; import langchain; print('✅ 설치 성공!')"

# agent.py 실행 테스트
python agent.py
```

## 📖 사용 예제

### 기본 Chatbot

```python
from agent import create_basic_chatbot, run_basic_chat

# 기본 챗봇 생성
graph = create_basic_chatbot()

# 대화형 실행
run_basic_chat(graph)
```

### Tool이 있는 Agent

```python
from agent import create_agent_with_tools, run_agent_chat

# Tool이 있는 Agent 생성
graph = create_agent_with_tools()

# 대화형 실행
run_agent_chat(graph)
```

### 메모리가 있는 Agent

```python
from agent import create_agent_with_memory, run_agent_chat

# 메모리가 있는 Agent 생성
graph = create_agent_with_memory()

# 설정 (thread_id로 대화 구분)
config = {"configurable": {"thread_id": "1"}}

# 대화형 실행
run_agent_chat(graph, config)
```

## 🐛 문제 해결

### 가상환경 활성화 안됨

```bash
# 터미널 프롬프트에 (venv)가 보여야 함
source venv/bin/activate
```

### Import 에러

```bash
# 올바른 Python 사용 확인
which python  # venv/bin/python이어야 함

# 패키지 재설치
pip install --force-reinstall langgraph langchain
```

### Playwright 브라우저 문제

```bash
# 브라우저 재설치
playwright install --force
```

### API 키 에러

```bash
# 1. .env 파일이 존재하는지 확인
ls -la .env

# 2. .env 파일 내용 확인 (키 값은 표시되지 않음)
cat .env

# 3. Python에서 환경변수 로드 테스트
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✅ API 키 로드됨' if os.getenv('ANTHROPIC_API_KEY') else '❌ API 키 없음')"

# 4. .env 파일이 없다면 생성
cp .env.sample .env
nano .env  # 실제 API 키 입력
```

## 📝 주의사항

1. **가상환경 활성화**: 작업 시작 전 반드시 `source venv/bin/activate` 실행
2. **API 키 보안**:
   - `.env` 파일에 API 키 저장 (Git에 커밋되지 않음)
   - API 키를 코드에 직접 입력하지 말 것
   - `.env` 파일을 절대 공개 저장소에 올리지 말 것
3. **비용 주의**: OpenAI, Anthropic API는 사용량에 따라 과금됨
4. **브라우저 자동화**: Playwright 사용 시 헤드리스 모드 권장
5. **.env 파일 필수**: `.env.sample`을 복사하여 `.env` 파일 생성 필요

## 🔗 참고 자료

- [LangGraph 공식 문서](https://langchain-ai.github.io/langgraph/)
- [LangChain 공식 문서](https://python.langchain.com/)
- [Anthropic Claude 문서](https://docs.anthropic.com/)
- [OpenAI API 문서](https://platform.openai.com/docs/)

## 📄 라이선스

본 실습 자료는 교육 목적으로 제공됩니다.

## 🙋‍♂️ 문의

문제가 발생하면 [DEPENDENCIES.md](DEPENDENCIES.md)의 Troubleshooting 섹션을 먼저 확인하세요.
