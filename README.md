# 주의 사항 
깃으로 다운받을 경우, .env 파일이 없습니다.
.env 파일 생성하시고 아래 내용 붙여넣기 해주시고 본인 키 넣어주시면 됩니다.
```
# API Keys
# OPENAI_API_KEY=YOUR_OPENAI_KEY
OPENAI_API_KEY=YOUR_OPENAI_KEY
GEMINI_API_KEY=YOUR_GEMINI_KEY

# Vector DB (로컬 chroma 경로)
CHROMA_PATH=./chroma_store
```

# LlamaIndex Workshop Hands-on Package (v2)

## 폴더 구조
```
llamaindex_workshop_v2/
├─ data/
│  ├─ txt/
│  ├─ csv/
│  └─ images/
├─ notebooks/
├─ src/
├─ .env.example
└─ requirements.txt
```

## 빠른 시작
1) Python 3.10+ 설치
2) 가상환경 생성 및 활성화
3) 의존성 설치: `pip install -r requirements.txt`
4) `.env.example` → `.env`로 복사하고 API 키 입력
5) `notebooks/01_quickstart.ipynb`부터 실행
