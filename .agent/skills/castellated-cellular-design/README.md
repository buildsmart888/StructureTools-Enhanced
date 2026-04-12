# Castellated and Cellular Beam Design Skill

**AISC Design Guide 31 전문가 시스템 - 허니컴보 설계 자동화**

## 개요

이 스킬은 AISC Design Guide 31 (Castellated and Cellular Beam Design)을 기반으로 한 종합 설계 자동화 시스템입니다. 캐스텔레이티드보(hexagonal openings)와 셀룰러보(circular openings)의 검색, 설계계산, 워크플로우를 제공합니다.

## 스킬 정보

- **이름**: `castellated-cellular-design`
- **버전**: 1.0.0
- **기준 코드**: AISC Design Guide 31 (2016)
- **AISC Specification**: AISC 360-16
- **설계 방법**: LRFD & ASD

## 주요 기능

### 1. 문서 검색 및 조회
- AISC DG31 전체 내용 통합 (Introduction, Use Cases, Design Procedures, Examples)
- 7가지 워크플로우 지원 (공식 질의, 예제 질의, 계산 질의 등)
- 카테고리 기반 스마트 검색
- 수식 추출 및 컨텍스트 제공

### 2. 구조 계산 자동화
- **기하학 계산**: 모재 단면 → 확장 단면 특성
- **Vierendeel 굽힘**: 개구부 위치에서의 국부 굽힘 계산
- **웹포스트 좌굴**: 개구부 간격 검증 및 좌굴강도 산정
- **상호작용 검증**: AISC H1-1a/b 상호작용 방정식

### 3. 설계 보조 자료
- 8개 참고 문서 (symbols, glossary, geometry-guide, failure-modes-guide 등)
- 4개 상세 설계 예제
- 단계별 설계 체크리스트
- 200+ 참고문헌 데이터베이스

## 디렉토리 구조

```
.claude/skills/castellated-cellular-design/
├── SKILL.md                          # 메인 스킬 파일 (워크플로우 정의)
├── README.md                         # 이 파일
│
├── data/                             # 핵심 설계 문서
│   ├── design-guide/                 # 3개 챕터 파일
│   │   ├── Chapter_1_Introduction.md
│   │   ├── Chapter_2_Use_Cases.md
│   │   └── Chapter_3_Design_Procedures.md
│   └── examples/                     # 4개 상세 예제
│       ├── Example_4-1_Noncomposite_Castellated.md
│       ├── Example_4-2_Noncomposite_Cellular.md
│       ├── Example_4-3_Composite_Castellated.md
│       └── Example_4-4_Composite_Cellular.md
│
├── references/                       # 빠른 참고 자료
│   ├── symbols.md                    # 기호 및 표기법 (100+ symbols)
│   ├── glossary.md                   # 용어 사전 (40+ terms)
│   ├── abbreviations.md              # 약어 정리 (50+ abbreviations)
│   ├── examples-index.md             # 예제 빠른 참조
│   ├── failure-modes-guide.md        # 6가지 파괴모드 요약
│   ├── geometry-guide.md             # CB/LB 기하학 가이드
│   ├── design-workflow-summary.md    # 15단계 설계 체크리스트
│   └── bibliography.md               # 100+ 참고문헌
│
└── scripts/                          # 자동화 Python 스크립트
    ├── README.md                     # 스크립트 사용 가이드
    ├── geometry_calculator.py        # 기하학 계산기 (16 KB)
    ├── vierendeel_calculator.py      # Vierendeel 굽힘 계산 (21 KB)
    ├── webpost_checker.py            # 웹포스트 좌굴 검증 (19 KB)
    ├── smart_search.py               # 스마트 검색 (13 KB)
    ├── formula_finder.py             # 수식 추출기 (11 KB)
    └── example_matcher.py            # 예제 매칭 (12 KB)
```

## 파일 통계

| 항목 | 수량 | 크기 |
|------|------|------|
| **총 파일** | 24개 | 608 KB |
| **설계 문서** | 7개 (3 chapters + 4 examples) | ~280 KB |
| **참고 자료** | 8개 | ~80 KB |
| **Python 스크립트** | 6개 + README | ~100 KB |
| **기타** | 3개 (SKILL.md, README.md, etc.) | ~148 KB |

## Python 스크립트 사용법

### 1. geometry_calculator.py - 기하학 계산기

**용도**: 모재 W형강 단면으로부터 확장된 CB/LB 단면 특성 계산

```bash
# 캐스텔레이티드보 (CB) 계산
python3 scripts/geometry_calculator.py W18x35 --type CB --opening-height 5.9 --spacing 12

# 셀룰러보 (LB) 계산
python3 scripts/geometry_calculator.py W18x35 --type LB --diameter 11.8 --spacing 17.7

# 대화형 모드
python3 scripts/geometry_calculator.py --interactive
```

**출력**:
- 확장 깊이 (dg)
- T형 단면 특성 (A, I, S, centroid)
- 명명법 (e.g., CB24x35, LB27x35)
- 개구부 기하학 상세

### 2. vierendeel_calculator.py - Vierendeel 굽힘 계산

**용도**: 개구부 위치에서의 축력 및 Vierendeel 모멘트 계산

```bash
# 비합성보 Vierendeel 계산
python3 scripts/vierendeel_calculator.py \
  --shear 50 \
  --opening-param 12 \
  --tee-area 5.96 \
  --composite no

# 합성보 Vierendeel 계산 (콘크리트 슬래브 포함)
python3 scripts/vierendeel_calculator.py \
  --shear 50 \
  --opening-param 12 \
  --tee-area 5.96 \
  --composite yes \
  --concrete-strength 4.0
```

**출력**:
- 축력 T0, T1 (kips)
- Vierendeel 모멘트 Mvt (kip-in)
- AISC H1-1a/b 상호작용비
- Pass/Fail 판정

### 3. webpost_checker.py - 웹포스트 좌굴 검증

**용도**: 개구부 간격 및 웹포스트 좌굴강도 검증

```bash
# 캐스텔레이티드보 웹포스트 검증
python3 scripts/webpost_checker.py \
  --type CB \
  --opening-param 5.9 \
  --spacing 12 \
  --web-thickness 0.3 \
  --yield-strength 50

# 셀룰러보 웹포스트 검증
python3 scripts/webpost_checker.py \
  --type LB \
  --opening-param 11.8 \
  --spacing 17.7 \
  --web-thickness 0.3 \
  --yield-strength 50
```

**출력**:
- s/dp 또는 S/Do 비율 검증
- 웹포스트 좌굴강도 (LRFD & ASD)
- Minimum spacing 권장사항
- Pass/Fail 판정

### 4. smart_search.py - 스마트 검색

**용도**: 키워드 기반 카테고리별 문서 검색

```bash
# Vierendeel 굽힘 관련 검색
python3 scripts/smart_search.py "Vierendeel bending"

# 웹포스트 좌굴 관련 검색
python3 scripts/smart_search.py "web post buckling" --category webpost

# 챕터 3만 검색
python3 scripts/smart_search.py "deflection" --chapter 3

# 예제만 검색
python3 scripts/smart_search.py "composite" --examples-only
```

**출력**:
- 관련도 순위 (relevance score)
- 파일 위치 및 라인 번호
- 컨텍스트 (전후 3줄)

### 5. formula_finder.py - 수식 추출기

**용도**: 특정 수식을 컨텍스트와 함께 추출

```bash
# 방정식 번호로 검색
python3 scripts/formula_finder.py "3-3"

# 변수 패턴으로 검색
python3 scripts/formula_finder.py "Mvr ="

# 컨텍스트 라인 수 조정
python3 scripts/formula_finder.py "web post" --context 10
```

**출력**:
- 수식 (LaTeX 형식 보존)
- 변수 정의 ("where" 섹션)
- 전후 컨텍스트

### 6. example_matcher.py - 예제 매칭

**용도**: 설계 조건에 맞는 적절한 예제 찾기

```bash
# 대화형 모드로 예제 선택
python3 scripts/example_matcher.py --interactive

# 예제 비교표 출력
python3 scripts/example_matcher.py --compare
```

**출력**:
- 추천 예제 파일
- 예제 요약 (보 타입, 합성작용, 주요 검증 항목)
- 4개 예제 비교표

## 7가지 워크플로우

SKILL.md에 정의된 7가지 워크플로우:

1. **Formula Query (공식 질의)** - "Vierendeel 모멘트 공식은?"
2. **Design Example Query (예제 질의)** - "합성 셀룰러보 설계 예제 보여줘"
3. **Calculation Query (계산 질의)** - "W18x35 기반 CB27의 Vierendeel 강도 계산"
4. **Geometry/Nomenclature Query** - "CB27x35는 무슨 의미?"
5. **Comparison Query (비교 질의)** - "캐스텔레이티드와 셀룰러의 차이는?"
6. **Failure Mode Query (파괴모드 질의)** - "웹포스트 좌굴이란?"
7. **Application/Use Case Query** - "주차장 구조물에 셀룰러보 사용 가능?"

## 주요 기술 고려사항

### 1. Vierendeel 굽힘 (Vierendeel Bending)
- **현상**: 개구부로 인해 웹 전단전달이 차단되어 T형 단면에 국부 굽힘 발생
- **설계**: 축력 + 굽힘모멘트 상호작용 검증 (AISC H1-1a/b)
- **핵심 방정식**: Equations 3-3 to 3-18

### 2. 웹포스트 좌굴 (Web Post Buckling)
- **현상**: 개구부 사이 웹 부분의 압축좌굴
- **임계비**: s/dp ≥ 1.25~1.5 (castellated), S/Do ≥ 1.08 (cellular)
- **핵심 방정식**: Equations 3-22 to 3-36

### 3. 처짐 계산 (Deflection)
- **특징**: 개구부로 인한 강성 감소를 90% Ix 감소계수로 반영
- **공식**: δ = 5wL⁴/(384 × E × 0.9Ix)

### 4. 기하학 의존성
- **CB (Castellated)**: 육각형 개구부, 지그재그 절단, θ = 45°~60°
- **LB (Cellular)**: 원형 개구부, 이중 원형 절단
- **확장비**: dg ≈ 1.5d (표준)

### 5. 설계 방법
- **LRFD**: φ factors (φb=0.90, φc=0.90, φv=1.00)
- **ASD**: Ω factors (Ωb=1.67, Ωc=1.67, Ωv=1.50)
- **Both**: 모든 예제와 스크립트에서 병행 지원

## 트리거 키워드

### English
- castellated beam, cellular beam, honeycomb beam
- Vierendeel bending, Vierendeel moment
- web post buckling, web post spacing
- hexagonal opening, circular opening
- CB beam, LB beam
- AISC Design Guide 31, AISC DG31
- expanded beam, depth expansion
- tee section, WT section
- opening layout, opening spacing
- composite cellular, noncomposite castellated

### Korean
- 캐스텔레이티드보, 셀룰러보, 허니컴보
- 비렌딜굽힘, 비렌딜모멘트
- 웹포스트좌굴, 개구부간격
- 육각형개구부, 원형개구부
- 합성보, 비합성보
- 확장깊이, 깊이확장
- T형단면, WT단면

## 통합 워크플로우 예시

### 예시 1: 완전 설계 프로세스

```bash
# Step 1: 기하학 계산
python3 scripts/geometry_calculator.py W18x35 --type CB --opening-height 5.9 --spacing 12
# 출력: CB24x35, Atee=5.96 in², Itee=87.6 in⁴

# Step 2: Vierendeel 굽힘 검증
python3 scripts/vierendeel_calculator.py --shear 50 --opening-param 12 --tee-area 5.96 --composite no
# 출력: Interaction ratio = 0.75 < 1.0 ✓ PASS

# Step 3: 웹포스트 좌굴 검증
python3 scripts/webpost_checker.py --type CB --opening-param 5.9 --spacing 12 --web-thickness 0.3 --yield-strength 50
# 출력: s/dp = 2.03 > 1.5 ✓ PASS, φMn = 125 kip-in
```

### 예시 2: 정보 검색 워크플로우

```bash
# Step 1: 주제 검색
python3 scripts/smart_search.py "composite cellular beam"
# 출력: Example_4-4_Composite_Cellular.md (relevance: 35)

# Step 2: 관련 예제 확인
python3 scripts/example_matcher.py --interactive
# 선택: composite=yes, type=LB → Example 4.4

# Step 3: 수식 추출
python3 scripts/formula_finder.py "3-17"
# 출력: Equation 3-17 with variable definitions
```

## 2025OFFICEWORK 생태계 통합

이 스킬은 **2025OFFICEWORK** 종합 구조설계 자동화 스위트의 일부입니다:

1. **Code_Engineer** (KDS) - 한국 건축구조기준 검색 및 계산
2. **mgt_maker** - midas Gen 구조모델링 (.mgt 파일 생성)
3. **ADM_Engineer** - 알루미늄 구조 설계 (ADM 2020)
4. **HONEYCOMB_Beam_Engineer** - 특수 철골보 설계 (AISC DG31) ✨

→ **완성된 구조설계 자동화 플랫폼**

## 개발 히스토리

- **2025-11-14**: 스킬 생성 및 Phase 1-2 완료
  - 117개 마크다운 페이지 → 7개 통합 문서
  - 8개 참고 자료 생성
  - 6개 Python 스크립트 개발
  - SKILL.md 작성 (7 workflows)

## 기술 스택

- **언어**: Python 3.12.9
- **의존성**: 표준 라이브러리만 사용 (no external packages)
- **문서 형식**: Markdown with LaTeX equations
- **설계 기준**: AISC 360-16, AISC Design Guide 31

## 라이선스 및 저작권

- **AISC Design Guide 31**: Copyright © American Institute of Steel Construction
- **스킬 구현**: 2025OFFICEWORK Project
- **사용 목적**: 교육 및 구조설계 실무 보조

## 기여 및 피드백

이 스킬은 ADM Aluminum Design 스킬과 KDS Korean Building Standards 스킬의 구조를 참고하여 개발되었습니다.

개선 제안 및 버그 리포트는 프로젝트 저장소로 제출해주세요.

---

**Last Updated**: 2025-11-14
**Version**: 1.0.0
**Status**: Production Ready ✓
