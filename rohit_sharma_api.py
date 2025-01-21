from fastapi import Body, FastAPI, HTTPException

app = FastAPI()

# Personal and career details of Rohit Sharma
ROHIT_SHARMA = {
    'name': 'Rohit Sharma',
    'date_of_birth': '1987-04-30',
    'nationality': 'Indian',
    'batting_style': 'Right-hand bat',
    'bowling_style': 'Right-arm offbreak',
    'role': 'Batsman',
    'total_runs': 9115,  # Updated total runs
    'total_100s': 8,     # Updated total centuries
    'total_50s': 43,     # Updated total half-centuries
    'matches_played': 200,  # Updated matches played
    'average': 48.96,       # Updated batting average
}

# Notable innings against Australia and Sri Lanka
NOTABLE_INNINGS = [
    # Australia innings
    {
        'date': '2013-11-02',
        'opponent': 'Australia',
        'runs': 209,
        'balls': 158,
        'fours': 12,
        'sixes': 16,
        'match_type': 'ODI',
        'location': 'M Chinnaswamy Stadium, Bengaluru',
        'description': 'Rohit Sharma scored a record-breaking 209 runs off 158 balls, including 12 fours and 16 sixes, leading India to a mammoth total and securing a series win against Australia.',
        'video_link': 'https://www.youtube.com/watch?v=Nebv9ZT2e74'
    },
    {
        'date': '2016-01-23',
        'opponent': 'Australia',
        'runs': 171,
        'balls': 163,
        'fours': 13,
        'sixes': 1,
        'match_type': 'ODI',
        'location': 'WACA Ground, Perth',
        'description': 'Rohit Sharma played a resilient knock of 171* runs off 163 balls, anchoring the innings and guiding India to a competitive total against Australia.',
        'video_link': 'https://www.youtube.com/watch?v=QJpry7zMR0Y'
    },
    {
        'date': '2013-10-19',
        'opponent': 'Australia',
        'runs': 141,
        'balls': 123,
        'fours': 11,
        'sixes': 5,
        'match_type': 'ODI',
        'location': 'Sawai Mansingh Stadium, Jaipur',
        'description': 'Rohit Sharma\'s explosive 141* runs off 123 balls, including 11 fours and 5 sixes, propelled India to a formidable total against Australia.',
        'video_link': 'https://www.youtube.com/watch?v=QJpry7zMR0Y'
    },
    # Sri Lanka innings
    {
        'date': '2017-11-13',
        'opponent': 'Sri Lanka',
        'runs': 208,
        'balls': 153,
        'fours': 13,
        'sixes': 12,
        'match_type': 'ODI',
        'location': 'Eden Gardens, Kolkata',
        'description': 'Rohit Sharma scored 208 runs off 153 balls, which included 13 fours and 12 sixes, becoming the first player to score two double centuries in One Day Internationals.',
        'video_link': 'https://www.youtube.com/watch?v=QJpry7zMR0Y'
    },
    {
        'date': '2014-11-13',
        'opponent': 'Sri Lanka',
        'runs': 264,
        'balls': 173,
        'fours': 33,
        'sixes': 9,
        'match_type': 'ODI',
        'location': 'Eden Gardens, Kolkata',
        'description': 'Rohit Sharma created history by scoring 264 runs off 173 balls against Sri Lanka, setting the record for the highest individual score in an ODI.',
        'video_link': 'https://www.youtube.com/watch?v=wIj2gDoL0d0'
    }
]

@app.get("/rohit")
async def get_rohit_details():
    return ROHIT_SHARMA

@app.put("/rohit/update_details")
async def update_rohit_details(updated_details=Body()):
    global ROHIT_SHARMA
    ROHIT_SHARMA.update(updated_details)
    return {"message": "Rohit Sharma details updated successfully", "details": ROHIT_SHARMA}

@app.get("/rohit/notable_innings")
async def get_notable_innings():
    return NOTABLE_INNINGS

@app.post("/rohit/add_inning")
async def add_inning(inning=Body()):
    NOTABLE_INNINGS.append(inning)
    return {"message": "Inning added successfully", "inning": inning}

@app.put("/rohit/update_inning/{inning_date}")
async def update_inning(inning_date: str, updated_inning=Body()):
    for i in range(len(NOTABLE_INNINGS)):
        if NOTABLE_INNINGS[i]['date'] == inning_date:
            NOTABLE_INNINGS[i].update(updated_inning)
            return {"message": "Inning updated successfully", "inning": NOTABLE_INNINGS[i]}
    raise HTTPException(status_code=404, detail="Inning not found")

@app.delete("/rohit/delete_inning/{inning_date}")
async def delete_inning(inning_date: str):
    for i in range(len(NOTABLE_INNINGS)):
        if NOTABLE_INNINGS[i]['date'] == inning_date:
            NOTABLE_INNINGS.pop(i)
            return {"message": "Inning deleted successfully"}
    raise HTTPException(status_code=404, detail="Inning not found")
