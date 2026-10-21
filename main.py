from src.pipeline.pipeline import run_research_pipeline
from rich import print

topic = "The impact of artificial intelligence on the job market and employment trends"
result = run_research_pipeline(topic)
print(result)