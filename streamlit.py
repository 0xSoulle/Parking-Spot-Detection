# Copied from https://docs.ultralytics.com/guides/streamlit-live-inference/#advantages-of-live-inference


from ultralytics import solutions

inf = solutions.Inference(
    model="best.pt",  
)

inf.inference()

# run using `streamlit run path/to/file.py`