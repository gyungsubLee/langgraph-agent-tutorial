# 설치 가이드

## 빠른 설치 (4단계)

### 1단계: 가상환경 생성 및 활성화

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate

# 가상환경 활성화 (Windows)
venv\Scripts\activate
```

### 2단계: 패키지 설치

```bash
# pip 업그레이드
pip install --upgrade pip

# requirements.txt로 모든 패키지 설치
pip install -r requirements.txt

# Playwright 브라우저 설치
playwright install
```

### 3단계: API 키 설정

```bash
# .env.sample 파일을 .env로 복사
cp .env.sample .env

# .env 파일 편집하여 실제 API 키 입력
nano .env  # 또는 vim, code 등 선호하는 편집기 사용
```

**.env 파일 예시:**
```bash
ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxxxx
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxxx
```

### 4단계: 설치 확인

```bash
# 패키지 임포트 테스트
python -c "import langgraph; import langchain; print('✅ 설치 완료!')"

# API 키 로드 테스트
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✅ API 키 로드됨' if os.getenv('ANTHROPIC_API_KEY') else '❌ API 키 없음')"
```

## 상세 설치 과정

### Python 버전 확인

```bash
# Python 3.8 이상 필요
python --version
# 또는
python3 --version
```

### 의존성 패키지 목록

`requirements.txt`에는 다음과 같은 주요 패키지들이 포함되어 있습니다:

- **langgraph** - Agent 그래프 프레임워크
- **langchain** - LangChain 핵심
- **langchain_anthropic** - Claude API
- **langchain_openai** - OpenAI API
- **tavily-python** - 검색 API
- **playwright** - 브라우저 자동화
- **pandas, matplotlib** - 데이터 분석 및 시각화

전체 120개 패키지가 자동으로 설치됩니다.

### 디스크 공간 요구사항

- Python 패키지: 약 400MB
- Playwright 브라우저: 약 380MB
- **총 필요 공간: 약 800MB**

### 설치 시간

- 패키지 설치: 2-5분
- 브라우저 설치: 1-3분
- **총 소요 시간: 약 3-8분** (인터넷 속도에 따라 다름)

## 문제 해결

### pip가 없는 경우

```bash
# macOS/Linux
python -m ensurepip --upgrade

# Ubuntu/Debian
sudo apt-get install python3-pip

# macOS (Homebrew)
brew install python3
```

### venv 모듈이 없는 경우

```bash
# Ubuntu/Debian
sudo apt-get install python3-venv

# Fedora/CentOS
sudo yum install python3-venv
```

### 권한 오류 (Permission denied)

```bash
# sudo 사용하지 말고 가상환경 사용
# 가상환경 안에서는 sudo 불필요
source venv/bin/activate
pip install -r requirements.txt
```

### 설치 중 오류

```bash
# 캐시 삭제 후 재설치
pip cache purge
pip install -r requirements.txt --no-cache-dir
```

### Playwright 브라우저 설치 실패

```bash
# 시스템 의존성 설치 (Ubuntu/Debian)
sudo apt-get install libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
  libcups2 libdrm2 libdbus-1-3 libxkbcommon0 libxcomposite1 \
  libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2

# 브라우저 재설치
playwright install --force
```

## macOS 전용 팁

### Apple Silicon (M1/M2/M3)

```bash
# Rosetta 없이 네이티브 ARM64로 설치됨
# 별도 설정 불필요
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Xcode Command Line Tools 필요

```bash
# 설치되어 있지 않은 경우
xcode-select --install
```

## Windows 전용 팁

### PowerShell 실행 정책

```powershell
# 가상환경 활성화 오류 시
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 가상환경 활성화
venv\Scripts\Activate.ps1
```

### Long Path 지원 활성화

```powershell
# 관리자 권한으로 실행
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
  -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

## Linux 전용 팁

### Ubuntu/Debian

```bash
# 필요한 시스템 패키지 설치
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv

# 가상환경 생성 및 패키지 설치
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install-deps  # 시스템 의존성
playwright install       # 브라우저
```

### Fedora/RHEL/CentOS

```bash
# 필요한 시스템 패키지 설치
sudo yum install python3 python3-pip

# 가상환경 생성 및 패키지 설치
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

## 오프라인 설치

### 1. 온라인 환경에서 패키지 다운로드

```bash
# 패키지 다운로드
pip download -r requirements.txt -d ./packages

# 다운로드한 packages 폴더를 오프라인 환경으로 복사
```

### 2. 오프라인 환경에서 설치

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate

# 다운로드한 패키지로 설치
pip install --no-index --find-links=./packages -r requirements.txt
```

## 업데이트

### 모든 패키지 업데이트

```bash
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

### 특정 패키지만 업데이트

```bash
source venv/bin/activate
pip install --upgrade langgraph langchain
```

### requirements.txt 업데이트

```bash
# 현재 설치된 패키지로 requirements.txt 갱신
source venv/bin/activate
pip freeze > requirements.txt
```

## 가상환경 삭제 및 재설치

```bash
# 가상환경 비활성화
deactivate

# 가상환경 폴더 삭제
rm -rf venv

# 새로 설치
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
playwright install
```

## 추가 도구 (선택사항)

### Jupyter Notebook

```bash
pip install jupyter
jupyter notebook
```

### IPython (대화형 Python)

```bash
pip install ipython
ipython
```

### Black (코드 포맷터)

```bash
pip install black
black agent.py
```

## 검증 체크리스트

설치 후 다음을 확인하세요:

- [ ] 가상환경 활성화 성공 (`(venv)` 프롬프트 표시)
- [ ] Python 버전 3.8 이상 (`python --version`)
- [ ] `.env` 파일 생성 완료 (`ls -la .env`)
- [ ] `.env` 파일에 API 키 입력 완료
- [ ] langgraph 임포트 성공
- [ ] langchain 임포트 성공
- [ ] langchain_anthropic 임포트 성공
- [ ] langchain_openai 임포트 성공
- [ ] python-dotenv 설치 및 로드 성공
- [ ] playwright 브라우저 설치 완료
- [ ] API 키 환경 변수 로드 성공

## 도움이 필요하신가요?

1. [DEPENDENCIES.md](DEPENDENCIES.md) - 상세 의존성 정보
2. [README.md](README.md) - 프로젝트 전체 가이드
3. [LangGraph 공식 문서](https://langchain-ai.github.io/langgraph/)
