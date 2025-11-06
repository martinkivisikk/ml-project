# ml-project
This is the repository for the Machine Learning course project.

## Environment setup
1. Clone the repository
```bash
git clone https://github.com/martinkivisikk/ml-project.git
```
```bash
cd ml-project
```
2. Copy default environment variables
```bash
cp .env.example .env
```
3. Build image
```bash
docker compose build
```
4. Run services
```bash
docker compose up -d
```
Access from:

[Jupyter](http://localhost:8888/)

[Streamlit](http://localhost:8501/)