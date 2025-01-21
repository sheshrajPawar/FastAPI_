from fastapi import Body, FastAPI, HTTPException

app = FastAPI()

# Cricket match data
MATCHES = [
    {'match_id': 1, 'team_1': 'India', 'team_2': 'Australia', 'date': '2024-02-15', 'venue': 'Melbourne'},
    {'match_id': 2, 'team_1': 'England', 'team_2': 'South Africa', 'date': '2024-03-10', 'venue': 'London'},
    {'match_id': 3, 'team_1': 'Pakistan', 'team_2': 'New Zealand', 'date': '2024-04-05', 'venue': 'Karachi'},
]

@app.get("/matches")
async def read_all_matches():
    return MATCHES


@app.get("/matches/{match_id}")
async def read_match(match_id: int):
    for match in MATCHES:
        if match['match_id'] == match_id:
            return match
    raise HTTPException(status_code=404, detail="Match not found")


@app.post("/matches/create_match")
async def create_match(new_match=Body()):
    MATCHES.append(new_match)
    return {"message": "Match added successfully", "match": new_match}


@app.put("/matches/update_match/{match_id}")
async def update_match(match_id: int, updated_match=Body()):
    for i in range(len(MATCHES)):
        if MATCHES[i]['match_id'] == match_id:
            MATCHES[i] = updated_match
            return {"message": "Match updated successfully", "match": updated_match}
    raise HTTPException(status_code=404, detail="Match not found")


@app.delete("/matches/delete_match/{match_id}")
async def delete_match(match_id: int):
    for i in range(len(MATCHES)):
        if MATCHES[i]['match_id'] == match_id:
            MATCHES.pop(i)
            return {"message": "Match deleted successfully"}
    raise HTTPException(status_code=404, detail="Match not found")
