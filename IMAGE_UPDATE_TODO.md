# 캐릭터 이미지 업데이트 작업 기록

## 현황 (2026-01-09 업데이트)
- 전체 캐릭터: 177개
- 생성된 이미지: 153개
- 남은 이미지: 24개

## 작업 순서

### Phase 1: 미생성 캐릭터 이미지 생성 (24개 남음)
- [x] Egyptian 9개 완료 (maat, sobek, hathor, nut, geb, ptah, khnum, atum, anuket)
- [x] Hindu 20개 완료
- [x] Chinese 20개 완료
- [x] Japanese 20개 완료
- [x] Korean 14개 완료
- [ ] Korean 5개 남음 (gumiho, choe_yeong, yi_bang_won, seonbi, an_jung_geun)
- [ ] World 19개 남음

**API 상태:** Google Imagen 일일 할당량 초과 (70/day) - 내일 리셋 후 계속

### Phase 2: 기존 72개 캐릭터 실사 버전 업데이트
- [ ] 기존 일러스트 스타일 → 실사 스타일로 교체 (나중에)

## 미생성 캐릭터 목록 (24개)

### Korean (5개)
- gumiho (구미호)
- choe_yeong (최영)
- yi_bang_won (이방원/태종)
- seonbi (선비)
- an_jung_geun (안중근)

### World Mythology (19개)
- anansi (아난시 - 서아프리카)
- shango (샹고 - 요루바)
- mami_wata (마미 와타 - 아프리카)
- maui (마우이 - 폴리네시아)
- pele (펠레 - 하와이)
- coyote (코요테 - 아메리카 원주민)
- white_buffalo_woman (백색 버팔로 여인 - 라코타)
- morrigan (모리건 - 켈트)
- cu_chulainn (쿠 훌린 - 아일랜드)
- inanna (이난나 - 수메르)
- gilgamesh (길가메시 - 수메르)
- quetzalcoatl (케찰코아틀 - 아즈텍)
- baba_yaga (바바 야가 - 슬라브)
- rainbow_serpent (무지개 뱀 - 호주 원주민)
- ahura_mazda (아후라 마즈다 - 조로아스터)
- vainamoinen (바이나모이넨 - 핀란드)
- oni (오니 - 일본)
- garuda (가루다 - 힌두/불교)
- merlin (멀린 - 아서왕)

## 기존 72개 캐릭터 목록 (Phase 2 대상)

### Greek (21개)
- zeus, hera, athena, apollo, artemis, ares, aphrodite, poseidon, hades, hermes
- dionysus, persephone, demeter, hephaestus, eros, pan, prometheus, hercules, helios, asclepius

### Norse (20개)
- odin, thor, freya, loki, frigg, baldur, tyr, hel, heimdall, skadi
- freyr, njord, vidar, vali, bragi, idunn, forseti, mimir, norns, jormungandr

### Biblical (20개)
- moses, david, solomon, abraham, elijah, samson, esther, daniel, ruth, noah
- job, jacob, isaiah, jonah, mary_mother, peter, paul, john_apostle, john_baptist, mary_magdalene

### Egyptian (11개)
- ra, isis, osiris, anubis, horus, bastet, sekhmet, thoth, set, nephthys, nuwa

## 진행 상황 로그

### 2026-01-09
- 기존 72개 이미지 확인 완료
- Google Imagen API로 81개 추가 생성 (총 153개)
- API 할당량 초과로 24개 남음
- Phase 1 대기 중 (API 할당량 리셋 필요 - 내일)

## 사용 API
- Google Imagen 4.0 Fast (일일 70개 제한)
- 실패 시 fallback 없음 (Gemini 이미지 생성 API 호환성 문제)
