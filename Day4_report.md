# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: Тен Владимир Александрович
- Group: IB-23-5B
- Token: D1-IB-23-5b-24-0A7D
- Repo: https://github.com/kto-to111/devnet-day1-IB-23-5B-Ten

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: **Exists**
- artifacts/day4/docker/sampleapp_token_proof.txt: **Exists**
- artifacts/day4/docker/sampleapp_docker_ps.txt: **Exists**
- artifacts/day4/docker/sampleapp_build_log.txt: **Exists**

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt: **Exists**
- artifacts/day4/jenkins/buildapp_console.txt: **Exists**
- artifacts/day4/jenkins/testapp_console.txt: **Exists**
- artifacts/day4/jenkins/pipeline_script.groovy: **Exists**
- artifacts/day4/jenkins/pipeline_console.txt: **Exists**
- artifacts/day4/jenkins/jenkins_url.txt: **Exists**

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt: **Exists**
- artifacts/day4/ansible/ansible_hello.txt: **Exists**
- artifacts/day4/ansible/ansible_playbook_install.txt: **Exists**
- artifacts/day4/ansible/ports_conf_after.txt: **Exists**
- artifacts/day4/ansible/curl_apache_8081.txt: **Exists**

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt: **Exists**
- artifacts/day4/security/login_v1.txt: **Exists**
- artifacts/day4/security/signup_v2.txt: **Exists**
- artifacts/day4/security/login_v2.txt: **Exists**
- artifacts/day4/security/db_tables.txt: **Exists**
- artifacts/day4/security/db_user_hash_sample.txt: **Exists**

## 3) Commands output
```bash
(.venv) devasc@labvm:~/Desktop/day1/devnet-day1-IB-23-5B-Ten$ python3 src/day4_summary_builder.py
{
  "schema_version": "4.1",
  "generated_utc": "2026-03-13T00:21:58.736866+00:00",
  "student": {
    "token": "D1-IB-23-5b-24-0A7D",
    "token_hash8": "9307fb77",
    "name": "Тен Владимир Александрович",
    "group": "IB-23-5b"
  },
  "checks": {
    "docker_token_in_page": true,
    "docker_tokenproof": true,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": true,
    "security_db_has_tables": true
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "613c372bdc25a729b6d1547ba54075a3d2cebbc8ced940582e6531c42a90bb28",
    "docker_ps": "867591d6ff1c61f47f49d414c10ba56aeee2120a0c2bfc7f7b2d53a00769dd80",
    "docker_build_log": "ccc74a0456164a04412a7673ccd35d7ba9faaf34711d47a50376558e2c129a92",
    "docker_token_proof": "613c372bdc25a729b6d1547ba54075a3d2cebbc8ced940582e6531c42a90bb28",
    "jenkins_docker_ps": "0ec6e33599495c08f338a2385a2f1755727e26acbbff23226536492ba0744687",
    "buildapp_console": "6db598ba53e9fe4278d8cc5a75eed8e8bd6d553f12e7557b78f3d71490a6ef05",
    "testapp_console": "abe7aa6a97a821ab03dd1f7f96270553c6b2b63c034ed5789e139dcc5def39ba",
    "pipeline_script": "0bb99d3b872f8b729d3a03e375e8926ed8c0499f27097e77448d699a6b073da5",
    "pipeline_console": "0b65c3b4d1517de091c5bc6666bbc3340a431a33fc2bf87e3b4fb05913f4c535",
    "jenkins_url": "185f195598830dbc315eb3a6741f97eace245e9d9d2a7225c5da77b87f27f3fc",
    "ansible_ping": "3013fd2ffe5a5734968d58204af7d4d50dcd5ba11be1cba123c8b7f684274fe0",
    "ansible_hello": "58bb784bf78fcac95c276184b5f2f0e0ad287c0908a29e9f23683821e603bc81",
    "ansible_playbook_install": "0a7439d6acabbff6e4ffd0d3312df3b97466e71d807c7aefa89915ab5e6035f5",
    "ports_conf_after": "04318de8d8ad3588c063121e90ed1e511fae1c0eccc77a04cdbb8273e875f7ea",
    "curl_apache_8081": "e870932d034a48187d6685a82452e2dfbd36db1ae9840a89275eaab07b73a009",
    "signup_v1": "bb4bd8dae047efb0cd225d6a258c641b9f488263cede19fc271db1ea4eb4640b",
    "login_v1": "67f30acea7c7caadadf0e90651bd8c196f939046b9c5398cd4733a118e5e53ca",
    "signup_v2": "45c8aa8f5e375aeda003c1afbd5c6ef2400962f8c9c86073193d2883385065a2",
    "login_v2": "ef63064b8c1207eb5e70677bbcbef59e07f98696f2a604a3accecd9dfbec4d71",
    "db_tables": "1b18c3a0cc1d524ad3ac7f735210994dd3bff9393a2b65ba894ccb72ae42fb7e",
    "db_user_hash_sample": "dc590cf9cb51eefd210a6f6bcffe192bb6f89f370085aeefc94c11d73e4e1fec"
  },
  "validation_passed": true,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}
```
```bash
(.venv) devasc@labvm:~/Desktop/day1/devnet-day1-IB-23-5B-Ten$ pytest -q
....                                                                                                                                                    [100%]
4 passed in 1.22s
```

## 4) Short reflection
- Самой сложной частью оказалась настройка Flask внутри Docker для работы в однопоточном режиме, так как на лабораторной VM возникала ошибка нехватки ресурсов для новых потоков. Я реализовал полноценную эволюцию методов хранения паролей: от опасного открытого текста (v1) до безопасного хеширования SHA-256 (v2) с использованием SQLite.

- One security mistake you avoided (or made and fixed): Изначально я допустил ошибку в синтаксисе Python при объединении функций безопасности в основной файл app.py. Контейнер падал с SyntaxError. Я исправил ошибку, пересобрал образ и убедился, что пароли в БД хранятся в виде хешей, а не в открытом виде.

## 5) Problems & fixes

### Problem 1:
Контейнер day4_app постоянно падал сразу после запуска со статусом Exited (1). Команда docker logs показала ошибку SyntaxError: unmatched ')'.

- Fix:
Отредактировал файл app.py, удалив лишнюю закрывающую скобку в блоке инициализации базы данных. После этого пересобрал образ через docker build.

- Proof:
Команда docker ps стала показывать статус Up, а curl к порту 8080 начал возвращать корректные ответы от API.

### Problem 2:
При попытке выгрузить данные из SQLite внутри Docker возникла ошибка: sqlite3: executable file not found.

- Fix:
Вместо прямой команды sqlite3 я использовал docker exec с вызовом Python-кода python -c "import sqlite3; ...", который прочитал данные из БД средствами встроенной библиотеки.

- Proof:
Файл db_user_hash_sample.txt был успешно заполнен реальными захешированными данными пользователя.