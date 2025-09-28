from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items")
def read_items():
    return {"items": ["item1", "item2", "item3"]}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    items = ["item1", "item2", "item3"]
    try:
        if item_id < 1 or item_id > len(items):
            raise HTTPException(status_code=404, detail="Item not found")
        return {"item_id": item_id, "name": items[item_id - 1]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/items")
def create_item(name: str):
    try:
        if not name:
            raise HTTPException(status_code=400, detail="Name is required")
        return {"message": f"Item '{name}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/weather/{city}")
def get_weather(city: str):
    try:
        if not city:
            raise HTTPException(status_code=400, detail="City name is required")
        # Dummy response for demonstration
        return {
            "city": city,
            "temperature": "25°C",
            "conditions": "Sunny",
            "humidity": "50%",
            "wind_speed": "10 km/h"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))