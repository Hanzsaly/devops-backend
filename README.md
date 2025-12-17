# DevOps Backend Project

## Описание
Простой backend на FastAPI с Docker и CI/CD через GitHub Actions.

## Структура
- `app/` – код приложения
- `tests/` – тесты
- `Dockerfile` – контейнеризация
- `.github/workflows/ci.yml` – CI/CD

## Запуск локально
1. Собрать Docker образ:
```bash
docker build -t devops-backend .
