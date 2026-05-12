from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from databases import SessionLocal, engine, Base
import model, schemas, utils

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten", response_model=schemas.URLResponse)
def shorten_url(request: schemas.URLRequest, db: Session = Depends(get_db)):
    short_code = utils.generate_short_code()

    db_url = model.URL(
        short_code=short_code,
        original_url=str(request.original_url)   # IMPORTANT FIX
    )

    db.add(db_url)
    db.commit()

    return {"short_url": f"http://localhost:8000/{short_code}"}

# Redirect
@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = db.query(model.URL).filter(model.URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url.original_url)