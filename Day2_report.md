# Day 2 Report — Git + Data Formats + Tests

## 1) Student
- Name: Vladimir Ten
- Group: IB-23-5B
- Token: D1-IB-23-5b-24-0A7D
- Repo: https://github.com/kto-to111/devnet-day1-IB-23-5B-Ten
- PR link (day2): https://github.com/kto-to111/devnet-day1-IB-23-5B-Ten/pull/1

## 2) NetAcad progress
- Module 2.2 done: Yes
- Module 3.1–3.6 done: Yes (SDLC, Python Data Formats, Testing)

## 3) Git evidence
- File `artifacts/day2/git_log.txt` exists: Yes
- File `artifacts/day2/conflict_log.txt` exists: Yes
- Conflict note: Конфликт возник в README.md из-за одновременного редактирования секции Progress в ветках A и B. Разрешен путем ручного объединения изменений и фиксации Merge-коммита.

## 4) Generated artifacts (Day2)
- normalized.json: Yes
- normalized.yaml: Yes
- normalized.xml: Yes
- normalized.csv: Yes
- summary.json: Yes

## 5) Commands output
### 5.1 Generator
```bash
(.venv) devasc@labvm:~/Desktop/day1/devnet-day1-IB-23-5B-Ten$ python3 src/day2_data_formats.py --input artifacts/day1/response.json
{
  "schema_version": "2.0",
  "generated_utc": "2026-03-11T09:41:50.567196+00:00",
  "student": {
    "token": "D1-IB-23-5b-24-0A7D",
    "token_hash8": "9307fb77",
    "name": "Тен Владимир Александрович",
    "group": "IB-23-5b"
  },
  "input": {
    "path": "artifacts/day1/response.json",
    "sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "outputs": {
    "normalized_json_sha256": "647e9fcd1b4b8f9d7b42f50c1931eaf0cf714f278b031f74c1c55233614d0079",
    "normalized_yaml_sha256": "d7da5165628ecf344e9daa06ac12236968159d8f4298872519e81d5e49678614",
    "normalized_xml_sha256": "b0c29b897d2c7f5197e8212f1487dc55c37c8b6d74393e082eb93dbfec37d87e",
    "normalized_csv_sha256": "9f2e2d3ca58bc881eadc2df15cb94e7bf3d7b2ae52ebc280044890b4548fc731"
  },
  "computed": {
    "title_len": 18
  }
}
```
### 5.2 Tests
```bash
(.venv) devasc@labvm:~/Desktop/day1/devnet-day1-IB-23-5B-Ten$ pytest -q
..                                                                     [100%]
2 passed in 0.52s
```

## 6) What I learned

- **Advanced Git Workflow:** Освоил процесс работы с ветками (feature branching), создание Pull Request и разрешение Merge Conflict через ручное редактирование конфликтных маркеров.
- **Data Serialization:** Научился преобразовывать сложные объекты Python в форматы JSON, YAML, XML и CSV с использованием соответствующих стандартных и сторонних библиотек.
- **Data Integrity & Security:** Реализовал механизм вычисления хеш-сумм (SHA-256) для верификации студенческого токена и контроля целостности генерируемых артефактов.
- **Automated Validation:** Внедрил автоматическую проверку структуры данных с помощью JSON Schema (библиотека `jsonschema`) внутри тестовых сценариев `pytest`.
- **Cross-Format Testing:** Разработал тесты для проверки эквивалентности данных в разных форматах (например, сравнение структуры JSON и YAML).
