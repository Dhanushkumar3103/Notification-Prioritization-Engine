from fastapi import FastAPI

app = FastAPI()

@app.post("/notify")
def notify(event: dict):
    priority = event.get("priority_hint", "low")

    if priority == "critical":
        return {"decision": "NOW", "reason": "Critical priority"}
    
    return {"decision": "LATER", "reason": "Deferred due to low priority"}
