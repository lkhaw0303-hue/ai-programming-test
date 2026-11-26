# ai-programming-test
# 성적 CSV 검증 프로그램

## 1. 무엇을 하나요

성적 CSV를 읽어 유효한 이름과 점수를 모으고, 제외한 행의 이유를 기록합니다.

## 2. 왜 만들었나요

예제 성적 CSV에는 점수가 비어 있는 행과 105점처럼 허용 범위를 벗어난 행이 섞여 있었습니다. 점수를 집계하기 전에 유효한 기록을 골라내고, 잘못된 데이터는 나중에 원본에서 찾아 수정할 수 있어야 했습니다. 그래서 유효한 이름과 점수는 따로 모으고, 건너뛴 행은 줄 번호와 이유를 기록하도록 만들었습니다.

## 3. 어떻게 쓰나요

저장소 폴더에서 아래 명령을 실행합니다.

```powershell
python -m pip install pytest pytest-cov
python load_scores.py scores.csv
```

## 4. 어떻게 테스트하나요

```powershell
python -m pytest test_load_scores.py --cov=load_scores --cov-report=term-missing
```

```text
collected 10 items

Name              Stmts   Miss   Cover   Missing
------------------------------------------------
load_scores.py       45      9     80%   77-86
------------------------------------------------
TOTAL                45      9     80%

10 passed in 0.19s
```

## 5. 파일 구성

| 파일 | 역할 |
|---|---|
| `load_scores.py` | 성적 CSV를 읽고 유효한 행과 제외한 행을 반환합니다. |
| `test_load_scores.py` | 정상 입력, 예외 상황, 점수 경계값을 검사합니다. |
| `scores.csv` | 성적 데이터 예제입니다. |
| `empty.csv` | 헤더만 있는 예제입니다. |
| `weird.csv` | 이름이나 점수가 잘못된 행이 포함된 예제입니다. |

## 6. 만든 사람과 AI 사용

- 만든 사람 — [임동원 2026100279]
- AI 사용 — ChatGPT의 도움을 받아 pytest 테스트를 작성하고 실행 방법을 확인했습니다.
- 직접 확인한 내용 — 테스트를 실행하고, 통과·실패 건수와 커버리지를 기록했습니다.