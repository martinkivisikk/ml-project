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

## Structure

```
ml-project/
│
├── README.md                 
├── requirements.txt           
├── .env              
├── Dockerfile 
├── compose.yml
│
├── data/
│   ├── raw/                   # Original input data 
│   ├── processed/             # Cleaned and preprocessed datasets
│   └── README.md              # Description of datasets and sources
│
├── notebooks/
│   └── 01_exploratory_analysis.ipynb     # Initial analysis
│
├── src/
│   ├── data/
│   │   └── .. .py            
│   │
│   ├── models/
│   │   └── .. .py            
│   │
│   ├── visualization/
│   │   └── .. .py            
│   │
│   └── config/
│       └── settings.py      
│
└── reports/
```