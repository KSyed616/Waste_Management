from fastapi import FastAPI
from pydantic import BaseModel
import random
from Neighbourhood import Neighbourhood
from WasteDept import WasteDept
from Schedule import waste_collections
from Schedule import get_hour

app = FastAPI()

neighbourhoods = [Neighbourhood(50), Neighbourhood(75), Neighbourhood(50)]
recycle_unit = WasteDept("recycle")
organics_unit = WasteDept("organics")
garbage_unit = WasteDept("garbage")
waste_units = {
    "recycle": recycle_unit,
    "organics": organics_unit,
    "garbage": garbage_unit
}


class WasteCollectionRequest(BaseModel):
    neighbourhoods: int


@app.post("/collect_waste/")
async def collect_waste(request: WasteCollectionRequest):
    num_neighbourhoods_to_collect = request.neighbourhoods
    # Collect waste from the specified number of neighbourhoods
    for _ in range(num_neighbourhoods_to_collect):
        # Randomly select a neighbourhood to collect waste from
        neighbourhood = random.choice(neighbourhoods)
        # Check if any waste unit has reached its capacity
        for waste_type, waste_unit in waste_units.items():
            if waste_unit.current == waste_unit.capacity:
                return {"message": f"Dispose of waste: {waste_type} has reached capacity"}
        # Collect waste from the selected neighbourhood
        if waste_collections([neighbourhood], waste_units):
            return {"message": "Waste collection initiated"}
        elif not waste_collections([neighbourhood], waste_units):
            return {"message": "Not within operating hours"}


@app.get("/status/")
async def get_status():
    status = {}
    # Get the status of waste collection
    for waste_type, waste_unit in waste_units.items():
        status[waste_type] = {
            "current": waste_unit.current,
            "capacity": waste_unit.capacity
        }
    # Add status for each neighbourhood
    for idx, neighbourhood in enumerate(neighbourhoods, start=1):
        status[f"neighbourhood_{idx}"] = {
            "residents": neighbourhood.residents(),
            "houses": neighbourhood.total,
        }
    return status


@app.get("/hours/")
async def hours():
    return {"current_hour": get_hour()}


@app.post("/dispose_waste/")
async def dispose_waste():
    garbage_unit.current = 0  # Reset the current waste collection amount for garbage
    organics_unit.current = 0  # Reset the current waste collection amount for organics
    recycle_unit.current = 0  # Reset the current waste collection amount for recycling
    return {"message": "Waste disposal successful"}


@app.post("/dispose_garbage/")
async def dispose_garbage():
    garbage_unit.current = 0  # Reset the current waste collection amount for garbage
    return {"message": "Garbage disposal successful"}


@app.post("/dispose_organics/")
async def dispose_organics():
    organics_unit.current = 0  # Reset the current waste collection amount for organics
    return {"message": "Organics disposal successful"}


@app.post("/dispose_recycle/")
async def dispose_recycle():
    recycle_unit.current = 0  # Reset the current waste collection amount for recycling
    return {"message": "Recycling disposal successful"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
