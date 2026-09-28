# CausalGround 01 — 구성 타당성 검증 및 후보 우선순위 v3

Date: 2026-09-29 (Asia/Seoul)
Repository baseline: `0b0b8d672fa8138b4972731b8ee6340627c5db8c`
Decision: **R3a를 다음 프로토콜 작성의 우선 후보로 추천. 연구자의 최종 선택·H1 동결·교수 승인은 아직 없음.**
Gate: HOLD_FOR_NOVELTY_AND_SELECTION. 세션 01 유지.

## 1. 이번에 실제 완료한 일

기존 준비서 T1의 표적 문헌 비교를 보강하고, T2/T3의 수학적 부분을 구현했다.
`validate_research_fixtures.py`는 Python 표준 라이브러리만 사용한다. R2 수치 fixture 10개, R3 fixture 12개를 검증했고, 단위시험 12개가 통과했다. R3의 정답 계산은 Fraction 기반 꼭짓점 열거와 별도 닫힌형 공식을 121개 확률 조합에서 대조했다. ChatGPT 작업 컨테이너 Python 3.13.5 CPU에서 실행했으며 사용자 PC나 GitHub Actions의 실행 결과가 아니다.

**이는 문제 구성·코드 점검이다. LLM 호출 0회, GPU 시험 0회, 학습 0회. 어떤 H1도 실증적으로 지지하거나 기각하지 않았다.** 자연어 렌더러·응답 파서·token-matching·모델 버전 선택·검정력 계산은 미완료다. 문서의 이전 후보 기록을 삭제하거나 실험 결과에 맞춰 변경하지 않았다.

## 2. 문헌의 내용과 우리 판단을 분리한다

| 1차 출처 / 확인 범위 | 실제 지원하는 내용 | 이번 후보와의 비교 — 연구자의 판단 |
|---|---|---|
| CausalDS, arXiv:2607.08093v1, 본문 §3.7 및 관련 과제/채점 설명 | SCM에서 만든 자료·질문과 식별/비식별 및 보류를 포함하는 평가 | 단순 비식별성 QA는 중복이다. 같은 질문의 식별 집합을 고정하고 새로운 유효 개입정보를 추가하는 paired 조작이 좁힌 후보의 차이이다. 이번 확인 절에서 동일 조작은 확인하지 못했지만 부재의 증명은 아니다. |
| The Information Shadow, arXiv:2607.18305v1, §5 | 두 규칙에 동시에 일치하는 학습자료와 두 규칙이 갈라지는 시험, 식별 가능 대조 | R3a는 학습 분포의 규칙 추정이 아니라 동결 모델의 증거 증가 전후 '점식별 주장'을 비교한다. 두 가능한 세계 자체는 신규성이 아니다. |
| GSM-IC / Large Language Models Can Be Easily Distracted by Irrelevant Context, arXiv:2302.00093, 공식 초록 | 무관한 문맥을 추가했을 때 산술 문제 성능 악화 | R3a의 추가 정보는 동일 결과변수의 다른 개입 확률이며 호환 SCM 집합을 실제로 줄인다. 그래도 단순 문맥 길이·산술 난이도 효과를 반드시 통제해야 한다. |
| AbstentionBench, NeurIPS 2025 Datasets and Benchmarks, 공식 논문 페이지·초록 | 다양한 답할 수 없는 질문에서 답변 보류 평가 | '모르면 보류'는 새롭지 않다. R3a는 정답 집합 불변의 paired 증거 조작을 묻는다. |
| ToolMaze, arXiv:2606.05806v1, 실패 분류 및 implicit-explicit trust gap 절 | 도구 실패와 형식이 정상인 의미 오류의 탐지·복구 | R2의 일반 도구 과신은 선행이다. 정당한 계산 보증의 노출 효과만을 분리해야 한다. |
| Who Do LLMs Trust?, arXiv:2602.13568v1, 실험 설계 본문 | 동일 문제 조언의 출처·집단 크기 조작과 잘못된 조언 추종 | R2가 '권위 표시 편향을 인과 문제에서 재현'하는 데 그칠 위험은 여전히 높다. |
| Partial Identification from LLM Prompts, arXiv:2606.15031, 공식 초록 | LLM 보고를 관측치로 사용해 잠재 참값 비율의 식별 집합을 분석 | 모델이 원인 확률 문제의 충분성을 판단하는 R3a와 과제는 다르다. 제목의 partial identification만으로 직접 중복이라고 단정하지 않는다. |
| CounterBench, AAAI 2026, 공식 논문 초록 | 형식적 반사실 추론, 그래프·난이도·이름 변형 평가 | 단순 반사실 벤치마크를 만들었다는 주장도 신규성 근거가 아니다. 추가 세부 조작 확인은 남아 있다. |
| Tian & Pearl, Probabilities of Causation: Bounds and Identification, 2000 원 연구 / arXiv 재게시 1301.3898 | 원인 확률의 sharp bounds와 식별 | 아래 PNS 공식·비식별성은 알려진 이론이다. 새 이론으로 주장하지 않는다. |

Sources:
- https://arxiv.org/html/2607.08093v1
- https://arxiv.org/html/2607.18305v1
- https://arxiv.org/abs/2302.00093
- https://proceedings.neurips.cc/paper_files/paper/2025/hash/fb122bfc3f0127a94ded048b5b03496f-Abstract-Datasets_and_Benchmarks_Track.html
- https://arxiv.org/html/2606.05806v1
- https://arxiv.org/html/2602.13568v1
- https://arxiv.org/abs/2606.15031
- https://ojs.aaai.org/index.php/AAAI/article/view/40287
- https://arxiv.org/abs/1301.3898
- https://escholarship.org/uc/item/44s6x4c7

검색은 targeted/bounded review이며 체계적 전수검색이 아니다. CausalVerify arXiv abstract/HTML은 이번에도 접근 실패했다. 이 논문의 2차 소개만으로 세부 중복 판정을 내리지 않는다. 추가 발견한 Evidence Sufficiency Benchmark와 CounterBench의 전체 조작 비교는 남아 있다. 이 접근 공백을 신규성 PASS로 바꾸지 않는다.

## 3. 우선 후보 H1-R3a — 정확한 두 번째 개입정보와 점식별 과장

R3를 버리거나 다른 주제로 바꾼 것이 아니라, 실제 정답을 검증할 수 있는 이진 반응유형 문제로 좁혔다.

> 같은 질문에서 가능한 반사실 확률의 집합을 그대로 유지하면서, 같은 결과변수에 관한 정확하고 비중복인 두 번째 개입 확률을 추가하면, LLM의 근거 없는 '단일값으로 결정된다'는 응답률이 증가한다.

Status: **RECOMMENDED_FOR_PROTOCOL / NOT_SELECTED / NOT_FROZEN / NOT_EMPIRICALLY_TESTED**.

대상 q는 우선 `P(Y0=0,Y1=1)`로 제한한다. 이는 집단 중 설정 0에서는 실패하고 설정 1에서는 성공할 비율(PNS)이다. 개별 장비의 숨겨진 실제 결과를 맞히는 과제가 아니다. p0,p1은 표본 추정치가 아니라 같은 모집단의 정확한 개입 확률이다. 모집단 변화, 측정 잡음, finite-sample CI를 이번 최소 구성에 섞지 않는다.

모델 클래스는 U=(Y0,Y1)가 00/01/10/11인 모든 연속 확률분포다. Y=Y_X이며 SUTVA/일관된 설정과 모집단을 전제한다. 단조성, Y0와 Y1의 독립성, 균질 효과는 주지 않는다. 정답용 전체 반응유형 분포는 모델 입력에 노출하지 않는다.

## 4. 정답 집합 불변의 손검산 및 완전한 구성

p1=P(Y1=1)만 알면 q는 [0,p1]에 있다.
p0=P(Y0=1)도 알면 q는 [max(0,p1-p0), min(p1,1-p0)]에 있다.
따라서 0<p1<=1/2이고 p1<=p0<=1-p1이면 추가 정보 전후 q의 범위가 정확히 [0,p1]로 같다.

네 반응유형 확률은 q를 이용해 다음처럼 쓸 수 있다.

```
p00 = 1-p0-q
p01 = q
p10 = p0-p1+q
p11 = p1-q
```

위 범위의 모든 q에서 네 확률이 음수가 아니고 합이 1이다. 따라서 두 끝점만 예로 드는 것이 아니라 사이의 모든 값도 실제로 달성 가능하다. 네 비음수 조건은 동시에 해당 하한·상한이 필요함을 보인다. 이 구성이 sharpness를 보장한다. 추가 p0가 호환 모델 집합을 엄격히 줄인다는 것은 원래 꼭짓점 중 새 제약을 위반하는 점을 찾아 별도로 확인했다.

### 설명용 예시: p1=30%, 새 정보 p0=40%

| 같은 장비의 잠재 결과 | 세계 A | 세계 B |
|---|---:|---:|
| 설정 0 실패, 설정 1 실패 | 60% | 30% |
| 설정 0 실패, 설정 1 성공 — 목표 q | 0% | 30% |
| 설정 0 성공, 설정 1 실패 | 10% | 40% |
| 설정 0 성공, 설정 1 성공 | 30% | 0% |

두 세계 모두 p1=30%, p0=40%다. q는 다르며 중간 값도 가능하다. D0에서도 D0+D1에서도 정확한 답은 [0%,30%]다. 새 정보는 모형에 대한 진짜 제약이지만 목표 q를 더 좁히지는 않는다. **이 표는 수학적 예시이지 LLM이 틀렸다는 관측 결과가 아니다.**

### 중요한 해석 제한

식별 집합 불변은 '새 정보가 베이지안 사후분포를 전혀 바꾸지 않는다'는 뜻이 아니다. 추가 정보로 점추정이나 주관적 신뢰가 합리적으로 바뀔 수 있다. 그래서 과제는 최선의 추정치를 묻지 않고 **주어진 가정·정보로 점식별되는지**를 묻는다. 가정 의존 추정치를 명확히 구분한 답변을 무조건 부당한 확신으로 채점하지 않는다. 사전분포나 단조성 등을 몰래 추가해서 유일한 정답이라고 단정한 경우만 구분한다.

## 5. 검증한 fixture와 범위

R3 12개: 정답 범위 불변 6개, 실제 범위 축소 2개, 점식별 3개, 모순된 단조성 1개. 이 중 단조성 추가는 대조군이며 주 비교의 가정은 고정한다. R3의 여섯 invariant 사례는 같은 작은 모형 클래스의 수치 예시로, 서로 다른 인과 구조에 대한 일반화 증거가 아니다.

R2 10개: 수치가 서로 다른 부적용 5개와, 같은 질문·관측/개입 교환 가능·무관한 개입·수치 동률·인과효과 없음 대조 5개. 수치만 우연히 같을 때 최종 답의 숫자로 잘못된 근거 채택을 판정할 수 없으므로 주 분석에서 제외했다. 전체 SCM을 아는 조건에서는 그 숫자가 정답일 수 있으므로 이를 자동 오답으로 만들지 않는다.

R2 scope label은 손으로 설계한 규약이고 코드는 수치를 검사한다. 이 코드는 일반 기호 의미 검증기나 자연어 파서가 아니다. aliases/paraphrases, 검증 표시 위치·길이·내용 통제, 비인과 산술 대조는 아직 구현하지 않았다. 'R2 fixture 수치 검증'을 'R2 실험 구성 완성'으로 해석하지 않는다.

## 6. 왜 R2에서 R3a로 우선순위를 옮기는가

R2의 효과 방향은 미검증이며 일반 권위 편향과 분리할 부담이 크다. R3a는 이번에 정답 집합 불변·새 제약의 비중복성·대조군을 직접 계산할 수 있게 됐다. 따라서 다음 프로토콜 작성에 R3a를 우선 추천한다. 이는 성공확률 추정, 논문 게재 보장, H1 신규성 최종 판정이 아니다. R2는 대안으로 보존한다.

## 7. 다음 프로토콜 초안 — 실행 승인 아님

| 조건 | 모델에 보이는 정보 | 역할 |
|---|---|---|
| D0 | 정확한 p1 + 고정 가정 + 같은 반사실 질문 | 기준 |
| D0+new | 위 정보 + 정확한 p0; oracle로 범위 불변 보장 | 주 비교 |
| D0+repeat | p1을 의미 보존해 반복, 길이 맞춤 | 반복·길이 대조 |
| D0+irrelevant | 목표와 무관한 정보, 길이 맞춤 | 일반 distraction 대조 |
| informative control | 실제 범위 축소/점식별을 만드는 추가 정보 | 항상 보류 전략 방지 |

새 정보와 무관한 정보의 정확한 token matching은 모델 tokenizer를 정한 뒤 검사한다. 여러 수치·표현·순서를 사용하고, 동일 기본 사례에서 만든 변형은 같은 분할에 묶는다. 이것들이 독립 표본이나 독립 그래프 가족인 것처럼 세지 않는다. 주 효과는 동일 기본 사례의 부당한 점식별 주장률 차이이며 분모는 gold 비식별 항목으로 고정한다.

주 비교의 기호: Delta=Pr(false_point_claim|D0+new)-Pr(false_point_claim|D0). H1은 Delta>0이다. 최소 의미 효과 delta와 정상 성능 손실 허용치 epsilon은 아직 미정이다. 탐색/확증 분할과 임계값을 결과를 보고 바꾸지 않는다. 반대 방향·동등성·넓은 CI를 각각 구분한다. p>0.05만으로 무효과를 주장하지 않는다.

응답은 점식별/범위식별/정보부족/모순을 구분하고 수치·범위·추가 가정 선언을 함께 기록하는 형식이 필요하다. 모든 숫자 응답을 오답으로 판정하지 않는다. 정확한 범위, 단순 보류, 조건부 추정, 잘못된 점식별, 파싱 실패를 분리한다. 일부러 정답 범위 라벨을 프롬프트에 넣어 개선을 주장하지 않는다.

후속 grounding 비교는 텍스트 설명·명시 그래프·계산 결과·그래프+계산을 역할별로 나누고, 표현 효과를 주장할 때 같은 사실을 제공한다. 계산 엔진의 범위 출력을 받는 시스템은 solver-only와 비교하며, 그것을 LLM 내부 능력의 향상으로 과장하지 않는다.

## 8. 코드 재사용 및 다음 세션 조건

DoVerifier 원격 최상위 목록을 이번에 읽었다. README와 causal_equiv.py, find_proof.py, probability.py, tests가 있었고 최상위 LICENSE/패키지 명세는 보이지 않았다. 전체 코드의 라이선스·실행·완전성은 확인하지 않았으며 원본 코드를 복사하지 않았다. R3a의 response-type sharp bounds는 DoVerifier의 식 동치 검증과 다른 역할이므로 설치를 선행 필수 단계로 만들지 않는다. 채택 범위가 바뀌면 다시 점검한다.

현재 미완료: 좁힌 후보의 연구자 선택, CounterBench/증거 충분성 인접 연구의 세부 비교, 자연어 구성·파싱 시험, 모델/버전, 효과 임계값·검정력, 교수 승인 상태. 따라서 세션 02로 넘어가지 않는다. 다음 구체 작업은 **R3a의 문제/응답 계약과 제출용 프로토콜 작성**이다. 새로운 후보를 무한히 추가하는 대신 이 후보의 남은 차별성/측정 가능성을 판정한다.

Reproduce from repository root:

```bash
python -m unittest discover -s tests -v
python scripts/validate_research_fixtures.py --output results/validation/session01_fixture_report.json
# Existing output should only be replaced deliberately:
# python scripts/validate_research_fixtures.py --output results/validation/session01_fixture_report.json --overwrite
```

첫 명령은 단위시험, 두 번째는 전체 fixture·꼭짓점·정답을 JSON으로 내보낸다. 어떤 명령도 LLM을 호출하거나 GPU를 사용하지 않는다. 현재 커밋의 요약은 `results/validation/session01_validation_summary.json`에 기록한다.
